import os
import time  # datetime may have more precision

from .clients.graphite import Statsd 
from .clients.default import Default

__all__ = [
  'Telemeter', 'runtime', 'get_client', 'set_client'
]


SERVICES = {
    'statsd': Statsd,
    'default': Default
}


class Telemeter:

    def __init__(self):
      self._services = {
        k: klass(os.environ.get(("TELEM_%s" % k).upper())) for k, klass in SERVICES.items()
      }
        
    def service(self, name):
        return self._services[name]

    def gauge(self, name, value, service='statsd'):
        self.service(service).gauge(name, value)


_client = Telemeter()


def set_client(client):
    global _client
    _client = client


def get_client():
    return _client


class runtime():

    def __init__(self, report_name, service='statsd'):
        self.service = service
        self.report_name = report_name

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, type, value, traceback):
        end = time.time()

        elapsed = (end - self.start) * 1000
        get_client().gauge(self.report_name, 
                           elapsed)

