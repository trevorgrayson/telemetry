import time  # datetime may have more precision
from os import environ

from .clients.default import Default
from .clients.slack import SlackTelemeter
from .clients.pagerduty import PagerDutyTelemeter
from .telemeter import Telemeter
from telemetry import loggers

SERVICES = {
    'default': Default
}

REGISTRY = [
    PagerDutyTelemeter,
    SlackTelemeter
]
ACTIVE_TELEMETERS = []


_telemeters = {
    "default": Telemeter()
}


def is_configured(meter: Telemeter):
    return all([req in environ for req in meter.__requires__])


def is_logger(meter: Telemeter):
    return hasattr(loggers, meter.__name__)


def load_env(logger=None):
    global ACTIVE_TELEMETERS
    ACTIVE_TELEMETERS = []  # TODO scan if each telemeter is loaded already.
    for meter in REGISTRY:
        if is_configured(meter):
            m = meter()
            ACTIVE_TELEMETERS.append(m)
            if logger is not None and is_logger(meter):
                logger.addHandler(m)


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
