from pytest import fixture

import telemetry
from telemetry.wrappers import report_time


class TestTelemetryWrappers:
  
  @fixture
  def telem(self):
      return telemetry.Telemeter()

  def test_constants(self, telem):
      a, b = 1, 2

      @report_time('statsd', 'some.key')
      def a_slow_function(a, b):
          return a + b

      result = a_slow_function(a, b)

      assert(result, a+b)
