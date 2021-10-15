import time  # datetime may have more precision

from .clients.slack import SlackTelemeter
from .clients.pagerduty import PagerDutyTelemeter
from .clients.statsd_ import StatsdTelemeter
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
