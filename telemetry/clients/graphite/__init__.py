import statsd


class Statsd:

    def __init__(self, host, port=8125):
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

