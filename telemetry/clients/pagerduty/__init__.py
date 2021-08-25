from os import environ
import logging
from json import dumps
from http.client import HTTPSConnection
from datetime import datetime
from telemetry.telemeter import TelemeterConfigException

PAGERDUTY_KEY = environ.get("PAGERDUTY_KEY")
PAGERDUTY_HOST = "events.pagerduty.com"
EVENT_PATH = "/v2/enqueue"
PAGERDUTY_LEVEL = getattr(logging, environ.get("PAGERDUTY_LEVEL", "ERROR"))
# TODO PAGERDUTY_CHANGE = "INFO"


class PagerDutyTelemeter(logging.StreamHandler):
    __requires__ = ['PAGERDUTY_KEY']

    def __init__(self, **kwargs):
        logging.StreamHandler.__init__(self)
        raises = kwargs.get("raises", False)
        self.routing_key = kwargs.get("routing_key", PAGERDUTY_KEY)
        self._conn = None  # lazy loading - occasional use!
        if raises and not self.routing_key:
            raise TelemeterConfigException(f"PagerDutyTelemeter requires {self.__requires__}")

    # def alert(self, msg):
    # def change(self, msg):

    def emit(self, record):
        if record.levelno >= PAGERDUTY_LEVEL:
            msg = self.format(record)
            return self.message(msg)

    def message(self, msg):
            self.conn.request("POST", EVENT_PATH,
                              body=dumps(self.payload(msg)),
                              headers=self.headers)
            resp = self.conn.getresponse()
            if resp.status in [202]:
                return True

    @property
    def headers(self):
        return {
            "Content-Type": "application/json",
            "Accept": "application/vnd.pagerduty+json;version=2"
        }

    @property
    def conn(self):
        if self._conn:
            return self._conn
        self._conn = HTTPSConnection(PAGERDUTY_HOST)
        return self._conn

    def payload(self, msg):
        return {
            "routing_key": self.routing_key,
            "event_action": "trigger",
            "payload": {
                "summary": msg.split("\n\n")[0][0:1024],  # title row will truncate
                "source": "recon",  # telemetry.hostname,
                "severity": "error",
                "timestamp": datetime.now().isoformat() + "+0000",
            },
            # "dedup_key": "samplekeyhere",
            "client": "Telemetry",
            "client_url": "https://pypi.org/projects/telemetry"
        }
