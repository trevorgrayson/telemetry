from os import environ

if "PAGERDUTY_KEY" in environ:
    del environ["PAGERDUTY_KEY"]

KEY = "SLACK_ROOM_ID"
if KEY in environ:
    del environ[KEY]
