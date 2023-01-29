import time  # datetime may have more precision

from .clients.slack import SlackTelemeter
from .clients.pagerduty import PagerDutyTelemeter
try:
    from .clients.statsd_ import StatsdTelemeter
except ImportError:
    pass
try:
    from .clients.datadog import DataDogStatsdTelemeter
except ImportError:
    pass
from .telemeter import Telemeter

# backwards compat
from .wrappers import runtime
from .deprecated import *
from .load_utils import *

REGISTRY = [
    PagerDutyTelemeter,
    SlackTelemeter
]
ACTIVE_TELEMETERS = []
