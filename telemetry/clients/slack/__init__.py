from os import environ
import logging
from json import dumps
from http.client import HTTPSConnection
from telemetry.telemeter import TelemeterConfigException

SLACK_HOST = 'hooks.slack.com'
SLACK_PATH = '/services/%s'
SLACK_ROOM_ID = environ.get("SLACK_ROOM_ID")


class SlackTelemeter(logging.StreamHandler):
    __requires__ = ['SLACK_ROOM_ID']

    def __init__(self, room_id=None, raises=False):
        logging.StreamHandler.__init__(self)
        self.room_id = room_id
        if self.room_id is None:
            self.room_id = SLACK_ROOM_ID
        if raises and self.room_id is None:
            raise TelemeterConfigException(f"SlackTelemeter requires {self.__requires__}")
        self.conn = HTTPSConnection(SLACK_HOST)

    def body(self, text):
        return dumps({"text": text})

    def emit(self, record):
        msg = self.format(record)
        return self.message(msg)

    def message(self, msg):
        self.conn.request("POST", SLACK_PATH % self.room_id, self.body(msg))
        # TODO this is blocking
        response = self.conn.getresponse()
        if response.status == 200:
            return True
