import os
from time import time_ns

from telemetry.clients.default import Default
from telemetry.clients.graphite import Statsd

CLIENT_NAME = 'default'

HOST = os.environ.get("STATSD_HOST")

if HOST is not None:
    CLIENT_NAME = 'statsd'

CLIENTS = {
    'statsd': Statsd,
    'default': Default
}

_client = CLIENTS.get(CLIENT_NAME)(HOST)


def set_client(client):
    global _client
    _client = client


def get_client():
    return _client


def report(service, name, value):
    result = get_client().gauge(name, value)

class benchmark():
    def __init__(self, report_name):
        self.report_name = report_name

    def __enter__(self):
        self.start = time_ns() // 1000000 

    def __exit__(self, type, value, traceback):
        end = time_ns() // 1000000 

        elapsed = end - self.start
        get_client().gauge(self.report_name, elapsed)

