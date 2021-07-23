import os
import time  # datetime may have more precision

from .clients.graphite import Statsd 
from .clients.default import Default
from .logging import TelemeterLogging

__all__ = [
  'Telemeter', 'runtime', 'get_client', 'set_client'
]


SERVICES = {
    'statsd': Statsd,
    'default': Default
}


class Telemeter(TelemeterLogging):
    def __init__(self):
        self._services = {
          k: klass(os.environ.get(("TELEM_%s" % k).upper())) for k, klass in SERVICES.items()
        }
        self.handlers = []

    def addHandler(self, handler):
        self.handlers.append(handler)

    def service(self, name):
        return self._services[name]

    def gauge(self, name, value, service=None):
        self.service(service).gauge(name, value)

    def incr(self, name, value=1, rate=1, service=None):
        self.service(service).incr(name, value, rate)

    def decr(self, name, value=1, rate=1, service=None):
        self.service(service).incr(name, -value, rate)

    def timing(self, name, value=1, rate=1, service=None):
        self.service(service).timing(name, value, rate)

    # def __getattr__(self, name):
    # returns callable


_client = Telemeter()


def set_client(client, key='statsd'):
    _client._services[key] = client


def get_client(key='statsd'):
    return _client._services[key]


def gauge(metric, value, service='statsd'):
    _client.gauge(metric, value, service)


def incr(metric, value=1, rate=1, service='statsd'):
    _client.incr(metric, value, rate, service)


def decr(metric, value=1, rate=1, service='statsd'):
    _client.decr(metric, value, rate, service)


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


_telemeters = {
    "default": Telemeter()
}


def get_telemeter(name=None):
    global _telemeters
    meter = _telemeters.get(name, _telemeters['default'])

    return meter



