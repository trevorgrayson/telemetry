telemeters as loggers


## loggers

python `logging` is dope.  not much reason to mess with success. `telemetry`
tries to get out of the way and give you an easy way to swap in services.

Telemeters can behave like `logging.StreamHandler`s. Presently supports:

- [pagerduty.com](https://pagerduty.com) - [creating a service](https://trydave.pagerduty.com/service-directory/new)
- [slack.com](https://slack.com/) - [creating your app](https://api.slack.com/apps)

```python PAGERDUTY_KEY=123 PAGERDUTY_LEVEL=ERROR
import logging
from telemetry.loggers import PagerDutyTelemeter

logger = logging.getLogger('telemeter')
meter =  PagerDutyTelemeter()
logger.addHandler(meter)

logger.error("Alert! Error thrown!")
```


```python
import telemetry

telemetry.add(telemetry.Slack())
telemeter = telemetry.get_telemeter()

@telemetry.runtime(message=lambda *args, **kwargs: f"OK {args}")
def some_func(bob, uncle):
    return bob
```
