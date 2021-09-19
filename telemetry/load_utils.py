from os import environ
from .telemeter import Telemeter
from .registry import REGISTRY
from telemetry import loggers


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


def env_handlers(loggers=False):
    """
    params:
        loggers: will only return Logger Telemeters when true.
    returns:
        list of Telemeters
    """
    meters = []  # TODO scan if each telemeter is loaded already.
    for meter in REGISTRY:
        if is_configured(meter):
            m = meter()
            if loggers and not is_logger(meter):
                continue
            meters.append(m)
    return meters
