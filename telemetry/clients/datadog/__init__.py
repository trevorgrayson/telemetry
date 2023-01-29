from os import environ
from datadog import initialize, statsd

STATSD_HOST = environ.get("STATSD_HOST")


class DataDogStatsdTelemeter:
    __requires__ = ['STATSD_HOST']

    def __init__(self, host=None, port=8125, **options):
        if host is None:
            host = STATSD_HOST
        if host is not None and ':' in host:
            host, port = host.split(':')
        initialize(statsd_host=host, statsd_port=port, **options)
        self.client = statsd

    def gauge(self, name, value):
        self.client.gauge(name, value)

    def incr(self, name, value=1, rate=1):
        self.client.incr(name, value, rate)

    def decr(self, name, value=1, rate=1):
        self.client.incr(name, -value, rate)

    def timing(self, name, value, rate=1):
        self.client.timing(name, value, rate)

    def send(self):
        self.client.pipeline().send()
