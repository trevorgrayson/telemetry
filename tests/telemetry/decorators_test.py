from pytest import fixture

import telemetry
from telemetry.decorators import runtime
from telemetry import get_client


PROBE = get_client()
REPORT_NAME = 'some.key'


@runtime(REPORT_NAME)
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
        assert PROBE.name == REPORT_NAME
        assert PROBE.value != 0 

