# https://docs.datadoghq.com/developers/dogstatsd/?tab=python
from os import environ
from datadog import initialize, statsd

STATSD_HOST = environ.get("DD_HOST", environ.get("STATSD_HOST"))


class DataDogStatsdTelemeter:
    __requires__ = []

    def __init__(self, host=None, port=8125, **options):
        if host is None:
            host = STATSD_HOST
        if host is not None and ':' in host:
            host, port = host.split(':')
        initialize(statsd_host=host, statsd_port=port, **options)
        self.client = statsd

    def gauge(self, name, value):
        self.client.gauge(name, value)

    def incr(self, name, value=1, **kwargs):
        self.client.increment(name, value, **kwargs)

    def decr(self, name, value=1, **kwargs):
        self.client.increment(name, -value, **kwargs)

    def timing(self, name, value, **kwargs):
        self.client.timing(name, value, **kwargs)
