import os
from .statsd_client import Statsd


SERVICES = {
  'statsd': Statsd
}


class Telemeter:

    def __init__(self):
      self._services = {
        k: klass(os.environ.get(("%s_HOST" % k).upper())) for k, klass in SERVICES.items()
      }
        
    def service(self, name):
        return self._services[name]

    def gauge(self, service_name, name, value):
        self.service(service_name).gauge(name, value)


_client = Telemeter()


def set_client(client):
    global _client
    _client = client


def get_client():
    return _client
