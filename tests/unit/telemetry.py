"""
Mock Probes for testing
"""


class TelemetryProbe:
    def __init(self):
        self.name = None
        self.value = None

    def gauge(self, service, name, value):
        self.service = service
        self.name = name
        self.value = value
