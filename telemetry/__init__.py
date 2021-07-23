import time  # datetime may have more precision

from .clients.graphite import Statsd 
from .clients.default import Default
from .telemeter import Telemeter

__all__ = [
  'Telemeter', 'runtime'
]

SERVICES = {
    'statsd': Statsd,
    'default': Default
}


_telemeters = {
    "default": Telemeter()
}


def get_telemeter(name=None):
    global _telemeters
    meter = _telemeters.get(name, _telemeters['default'])

    return meter


class runtime():

    def __init__(self, report_name, service='statsd'):
        self.service = service
        self.report_name = report_name

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, type, value, traceback):
        end = time.time()

        elapsed = (end - self.start) * 1000


