from .clients.default import Default
from .telemeter import Telemeter

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

