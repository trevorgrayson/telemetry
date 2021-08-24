import time  # datetime may have more precision

from .clients.default import Default
from .clients.slack import SlackTelemeter
from .clients.pagerduty import PagerDutyTelemeter
from .telemeter import Telemeter

__all__ = [
  'Telemeter'
]

SERVICES = {
    'default': Default
}


_telemeters = {
    "default": Telemeter()
}


def get_telemeter(name=None):
    global _telemeters
    if name is None:
        name = 'default'
    _telemeters[name] = _telemeters.get(name, Telemeter())
    return _telemeters[name]


class runtime:

    def __init__(self, report_name):
        self.report_name = report_name

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, type, value, traceback):
        end = time.time()
        elapsed = (end - self.start) * 1000
