import statsd

class Statsd:
    """ Implementation of StatsD protocol
    """

    def __init__(self, host, port=8125):
        self._client = statsd.StatsClient(host, port)

    def gauge(self, name, value):
        self._client.gauge(name, value)

    def report_time(self, fn):
        pass

