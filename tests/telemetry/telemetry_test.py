from pytest import fixture

import telemetry


class TestTelemetry:
  
  @fixture
  def telem(self):
      return telemetry.Telemetry()

  def test_constants(self, telem):
      assert(len(telemetry.SERVICES) == 1)

  def test_init(self, telem):
      assert(telem.service('statsd').__class__.__name__ == 'Statsd')

  def test_gauge(self, telem):
      telem.gauge('statsd', 'some.gauge.name', 123)
