from .clients.slack import SlackTelemeter
from .clients.pagerduty import PagerDutyTelemeter


REGISTRY = [
    PagerDutyTelemeter,
    SlackTelemeter
]

