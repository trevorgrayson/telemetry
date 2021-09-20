Remote measuring abstraction for software applications.

`telemetry` serves as a simple facade or abstraction for various telemetry frameworks (e.g. pagerduty, slack, graphite) 
allowing the end user to plug in the desired telemetry framework at deployment time. Think [slf4j](http://www.slf4j.org/)
but for events and numbers.  This library borrows from their example (and copy.)

As your projects grow, their telemetry requirements will change.  The purpose of this library is to simplify
implementation, provide easy configuration, encourage testing, and avoid vendor lock.

## Supported Services:

Setting up a new service should be as easy as adding your API Keys.

* [pagerduty](https://www.pagerduty.com/) - get your `PAGERDUTY_KEY` from https://{yourorg}.pagerduty.com/api_keys
* [slack](https://api.slack.com/apps) - only needs a `SLACK_ROOM_ID` from your [Slack Webhook App](https://api.slack.com/apps)

Telemeters preference to being configurable, but don't require more than
credentials to get working. For instance, slack can be implemented with
the following:

```SLACK_ROOM_ID=Txxx/Byyy/Zzzz python
import logging
from telemetry import SlackTelemeter

logging.basicConfig(level=logging.INFO)
logging.getLogger().addHandler(SlackTelemeter())
logging.info("hello room!")
```

or 

```SLACK_ROOM_ID=Txxx/Byyy/Zzzz python

from telemetry import SlackTelemeter
meter = SlackTelemeter()
meter.message("your message!")
```

Clients are written using core python libraries, so `telemetry` is light weight.

## Python Wrapper

You can instantiate Telemeters by using environment variables.

If you'd like to completely remove reference of `telemetry` 
from your app, you can use the python wrapper.

```sh
python -m telemetry your.module

# or if you installed scripts

telemetry your.module
```
