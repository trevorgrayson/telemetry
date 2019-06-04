from statsd_client import Statsd

SERVICES = {
  'statsd': Statsd
}


class Telemetry:

    def __init__(self):
      self._services = {
        k: klass() for k, klass in SERVICES.items()
      }
        
    def service(self, name):
        return self._services[name]

    def report(self, service_name, name, value):
        self.service(service_name).report(name, value)

