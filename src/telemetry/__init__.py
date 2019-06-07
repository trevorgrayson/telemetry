import os
from statsd_client import Statsd

SERVICES = {
  'statsd': Statsd
}


class Telemetry:

    def __init__(self):
      self._services = {
        k: klass(os.environ.get(("%s_HOST" % k).upper())) for k, klass in SERVICES.items()
      }
        
    def service(self, name):
        return self._services[name]

    def gauge(self, service_name, name, value):
        self.service(service_name).gauge(name, value)

