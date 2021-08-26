from os import environ

if "PAGERDUTY_KEY" in environ:
    del environ["PAGERDUTY_KEY"]
