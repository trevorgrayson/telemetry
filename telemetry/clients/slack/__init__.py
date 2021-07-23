from os import environ
from json import dumps
from http.client import HTTPSConnection

SLACK_HOST = 'hooks.slack.com'
SLACK_PATH = '/services/%s'
SLACK_ROOM_ID = environ.get("SLACK_ROOM_ID")


class SlackTelemeter:
    __requires__ = ['SLACK_ROOM_ID']

    def __init__(self, room_id):
        self.room_id = room_id
        if self.room_id is None:
            self.room_id = SLACK_ROOM_ID
        self.conn = HTTPSConnection(SLACK_HOST)

    def body(self, text):
        return dumps({"text": text})

    def message(self, msg):
        self.conn.request("POST", SLACK_PATH % self.room_id, self.body(msg))
        # TODO this is blocking
        response = self.conn.getresponse()
        return response.status == 200
