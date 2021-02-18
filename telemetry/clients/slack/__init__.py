import logging
from os import environ
from slack import WebClient
from slack.errors import SlackApiError


SLACK_TOKEN = environ.get("SLACK_TOKEN")
CHANNEL = environ.get("SLACK_CHANNEL", 'telemetry-test')
FROM = environ.get("SLACK_NAME", 'telemetry-test-bot')


class SlackTelemeter:
    def __init__(self, token=None, channel="#telemetry", from_name="telemetry"):
        self.token = token if token is not None else SLACK_TOKEN
        self.channel = channel
        self.from_name = from_name

        self.client = WebClient(token=self.token)

    def log(self, message):
        try:
            response = self.client.chat_postMessage(
                channel=self.channel,
                text=message)
            print(response)
            return True
        except SlackApiError as e:
            print(e)
            logging.exception(e)

    def exception(self, message=None):
        return self.log(message)
