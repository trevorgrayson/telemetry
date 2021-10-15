from os import environ
import statsd

STATSD_HOST = environ.get("STATSD_HOST")  # "127.0.0.1"


class StatsdTelemeter:
    __requires__ = ['STATSD_HOST']

    def __init__(self, host=None, port=8125):
        if host is None:
            host = STATSD_HOST
        if host is not None and ':' in host:
            host, port = host.split(':')
        self.client = statsd.StatsClient(host, port)

    def gauge(self, name, value):
        self.client.gauge(name, value)

    def incr(self, name, value=1, rate=1):
        self.client.incr(name, value, rate)

    def decr(self, name, value=1, rate=1):
        self.incr(name, -value, rate)

    def timing(self, name, value, rate=1):
        self.client.timing(name, value, rate)
