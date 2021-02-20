"""
Mock Probes for testing
"""


class TelemetryProbe:

    def __init__(self):
        self.name = None
        self.value = None

    def gauge(self, name, value):
        self.name = name
        self.value = value

    def incr(self, name, value=1, rate=1):
        self.name = name
        self.value = value

    def decr(self, name, value=1, rate=1):
        self.name = name
        self.value = value

    def timing(self, name, value, rate=1):
        self.name = name
        self.value = value

    def exception(self, reason):
        self.name = reason
        self.value = 1

