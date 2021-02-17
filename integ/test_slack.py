from os import environ
from pytest import fixture
from telemetry.clients import SlackTelemeter
from telemetry.clients.slack import SLACK_TOKEN

SLACK_SECRET = environ.get("SLACK_SECRET")
SLACK_CLIENT_ID = environ.get("SLACK_CLIENT_ID")
REASON = "Telemetry Library test was run."

class TestSlack:
    @fixture
    def client(self):
        return SlackTelemeter(token=SLACK_TOKEN)

    def test_exception(self, client):
        client.exception(REASON)