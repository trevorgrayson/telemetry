import os
import functools
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

METHODS = [
   'gauge', 'incr', 'decr', 'timing', 'log', 'exception'
]


def prefix_function(function, prefunction):
    @functools.wraps(function)
    def run(*args, **kwargs):
        prefunction(*args, **kwargs)
        return function(*args, **kwargs)
    return run


class Telemeter:

    def __init__(self):
        self._services = {
          k: klass(os.environ.get(("TELEM_%s" % k).upper())) for k, klass in SERVICES.items()
        }

    def add_service(self, *services):
        for service in services:
            for method in METHODS:
                if hasattr(service, method):
                    meth = getattr(service, method)
                    functools.wraps(getattr(self, method))(meth)

    def service(self, name):
        return self._services[name]

    def gauge(self, name, value, service='statsd'):
        self.service(service).gauge(name, value)

    def incr(self, name, value=1, rate=1, service='statsd'):
        self.service(service).incr(name, value, rate)

    def decr(self, name, value=1, rate=1, service='statsd'):
        self.service(service).incr(name, -value, rate)

    def timing(self, name, value=1, rate=1, service='statsd'):
        self.service(service).timing(name, value, rate)

    def exception(self, reason):
        pass


_client = Telemeter()


def set_client(client, key='statsd'):
    _client._services[key] = client


def get_client(key='statsd'):
    return _client._services[key]


def add_service(service):
    _client.add_service(service)


def gauge(metric, value, service='statsd'):
    _client.gauge(metric, value, service)


def incr(metric, value=1, rate=1, service='statsd'):
    _client.incr(metric, value, rate, service)


def decr(metric, value=1, rate=1, service='statsd'):
    _client.decr(metric, value, rate, service)


def exception(reason):
    _client.exception(reason)


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

