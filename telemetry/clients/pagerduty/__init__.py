from os import environ
import socket
import logging
from json import dumps
from http.client import HTTPSConnection
from datetime import datetime
from telemetry.telemeter import TelemeterConfigException, decorators

PAGERDUTY_KEY = environ.get("PAGERDUTY_KEY")
PAGERDUTY_HOST = "events.pagerduty.com"
EVENT_PATH = "/v2/enqueue"
PAGERDUTY_LEVEL = getattr(logging, environ.get("PAGERDUTY_LEVEL", "ERROR"))
# TODO PAGERDUTY_CHANGE = "INFO"

HOSTNAME = socket.gethostname()


class PagerDutyTelemeter(logging.StreamHandler, decorators.Decorators):
    __requires__ = ['PAGERDUTY_KEY']

    def __init__(self, **kwargs):
        logging.StreamHandler.__init__(self)
        raises = kwargs.get("raises", False)
        self.routing_key = kwargs.get("routing_key", PAGERDUTY_KEY)
        self._conn = None  # lazy loading - occasional use!
        self.source = kwargs.get("source", "telemetry")
        self.client = kwargs.get("client", "Telemetry")
        self.client_url = kwargs.get("client_url", "https://pypi.org/project/telemetry")
        if raises and not self.routing_key:
            raise TelemeterConfigException(f"PagerDutyTelemeter requires {self.__requires__}")

    # def alert(self, msg):
    # def change(self, msg):
    def dedupe_key(self):
        """
        - ideally the deployment + the error message
        - or the "unique" application name  + the error message
        - else the error message
        """
        if self.source is None:
            return socket.gethostname()

        return self.source

    def emit(self, record):
        if record.levelno >= PAGERDUTY_LEVEL:
            msg = self.format(record)
            return self.message(msg)

    def message(self, msg, **kwargs):
        self.conn.request("POST", EVENT_PATH,
                          body=dumps(self.payload(msg, **kwargs)),
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

    def payload(self, msg, dedupe_key=None, source=None, **kwargs):
        if isinstance(msg, Exception):
            msg = f"{str(msg.__class__.__name__)}: {str(msg)}"

        if dedupe_key is None:
            if isinstance(msg, Exception):
                dedupe_key = f"{msg.__class__.__name__}"
            else:
                dedupe_key = ''
            dedupe_key = "-".join((HOSTNAME, msg)).replace(" ", "")

        return {
            "routing_key": self.routing_key,
            "event_action": "trigger",
            "payload": {
                "summary": str(msg).split("\n\n")[0][0:1024],  # truncates
                "source": source or self.source,
                "severity": "error"
                # "timestamp": datetime.now().isoformat() + "+0000",
            },
            "dedup_key": dedupe_key,
            "client": self.client,
            "client_url": self.client_url
        }
