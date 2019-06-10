import statsd


class Statsd:

    def __init__(self, host, port=8125):
        self.client = statsd.StatsClient(host, port)

    def gauge(self, name, value):
        self.client.gauge(name, value)
