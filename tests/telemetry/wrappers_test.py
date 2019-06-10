from pytest import fixture

import telemetry
from telemetry.wrappers import report_time


@report_time('statsd', 'some.key')
def a_slow_function(a, b):
      return a + b


class TestTelemetryWrappers:
  
  @fixture
  def telem(self):
      return telemetry.Telemeter()

  def test_constants(self, telem):
      a, b = 1, 2
      result = a_slow_function(a, b)

      assert result == a + b
