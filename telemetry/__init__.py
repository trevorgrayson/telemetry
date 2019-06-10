import os
from .statsd_client import Statsd
from time import time_ns


SERVICES = {
  'statsd': Statsd
}


class Telemeter:

    def __init__(self):
      self._services = {
        k: klass(os.environ.get(("%s_HOST" % k).upper())) for k, klass in SERVICES.items()
      }
        
    def service(self, name):
        return self._services[name]

    def gauge(self, service_name, name, value):
        self.service(service_name).gauge(name, value)


class benchmark():
    def __init__(self, service, report_name):
        self.service = service
        self.report_name = report_name

    def __enter__(self):
        self.start = time_ns() // 1000000 

    def __exit__(self, type, value, traceback):
        end = time_ns() // 1000000 

        elapsed = end - self.start
        get_client().gauge(self.service,
                           self.report_name, 
                           elapsed)


_client = Telemeter()


def set_client(client):
    global _client
    _client = client


def get_client():
    return _client
