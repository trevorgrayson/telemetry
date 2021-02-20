import os
import time  # datetime may have more precision

from .clients.default import Default

__all__ = [
  'Telemeter', 'runtime', 'get_client', 'set_client'
]

REGISTERED_ACTIONS = [
    'gauge', 'incr', 'decr', 'timing',
    'log', 'exception'
]

SERVICES = {
    'default': Default
}


class Telemeter:

    def __init__(self):
        self._services = {
          k: klass(os.environ.get(("TELEM_%s" % k).upper())) for k, klass in SERVICES.items()
        }
        self.registry = {}

        
    def service(self, name):
        return self._services[name]

    def gauge(self, name, value):
        for handler in self.handlers('gauge'):
            handler.gauge(name, value)

    def incr(self, name, value=1, rate=1):
        for handler in self.handlers('incr'):
            handler.incr(name, value, rate)

    def decr(self, name, value=1, rate=1):
        for handler in self.handlers('decr'):
            handler.incr(name, -value, rate)

    def timing(self, name, value=1, rate=1):
        for handler in self.handlers('timing'):
            handler.timing(name, value, rate)

    # text based

    def log(self, reason, level=0, service=None):
        for handler in self.handlers('log'):
            handler.log(reason)

    def exception(self, reason, service=None):
        for handler in self.handlers('exception'):
            handler.exception(reason)

    def add_handler(self, handler):
        for action in REGISTERED_ACTIONS:
            if hasattr(handler, action):
                actions = self.registry.get(action, [])
                actions.append(handler)
                self.registry[action] = actions

    def handlers(self, action):
        return self.registry.get(action, [])

_client = Telemeter()


def set_client(client, key='statsd'):
    _client._services[key] = client


def get_client(key='statsd'):
    return _client._services[key]


def gauge(metric, value, service='statsd'):
    _client.gauge(metric, value)


def incr(metric, value=1, rate=1, service='statsd'):
    _client.incr(metric, value, rate)


def decr(metric, value=1, rate=1, service='statsd'):
    _client.decr(metric, value, rate)


def timing(name, value=1, rate=1):
    _client.timing(name, value, rate)


def log(reason, level=0):
    _client.log(reason)


def exception(reason):
    _client.exception(reason)


def add_handler(handler):
    _client.add_handler(handler)


class runtime:
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

