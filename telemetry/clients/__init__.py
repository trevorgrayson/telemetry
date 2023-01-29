from .default import Default
from .slack import SlackTelemeter
try:
    from .statsd_ import StatsdTelemeter
except ImportError:
    pass
try:
    from .datadog import DataDogStatsdTelemeter
except ImportError:
    pass