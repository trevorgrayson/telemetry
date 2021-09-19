import time  # datetime may have more precision

from .clients.slack import SlackTelemeter
from .clients.pagerduty import PagerDutyTelemeter
from .telemeter import Telemeter

# backwards compat
from .wrappers import runtime
from .deprecated import *
from .load_utils import env_handlers

REGISTRY = [
    PagerDutyTelemeter,
    SlackTelemeter
]
ACTIVE_TELEMETERS = []


def is_configured(meter: Telemeter):
    return all([req in environ for req in meter.__requires__])


def is_logger(meter: Telemeter):
    return hasattr(loggers, meter.__name__)


def env_loggers():
    for meter in REGISTRY:
        if is_configured(meter) and is_logger(meter):
            yield meter


def load_env(logger=None):
    global ACTIVE_TELEMETERS
    ACTIVE_TELEMETERS = []  # TODO scan if each telemeter is loaded already.
    for meter in REGISTRY:
        if is_configured(meter):
            m = meter()
            ACTIVE_TELEMETERS.append(m)
            if logger is not None and is_logger(meter):
                logger.addHandler(m)
