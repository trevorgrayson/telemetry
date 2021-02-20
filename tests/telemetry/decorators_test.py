from pytest import fixture, raises

import telemetry
from telemetry.decorators import runtime, catch
from tests.unit.telemetry import TelemetryProbe


PROBE = TelemetryProbe()
REPORT_NAME = 'some.key'
telemetry.add_handler(PROBE)


@runtime(REPORT_NAME)
def a_slow_function(a, b):
      return a + b


class TestRuntime:
    def test_constants(self):
        a, b = 1, 2
        result = a_slow_function(a, b)

        assert result == a + b
        assert REPORT_NAME == PROBE.name
        assert PROBE.value != 0 


@catch('some_report')
def exception_prone(ii):
    return 1/ii

class TestsExcept:
    def test_catch_pass(self):
        assert exception_prone(2) == 0.5

    def test_catch_throws(self):
        with raises(ZeroDivisionError):
            exception_prone(0)
        assert 'ZeroDivisionError' in PROBE.name
        assert PROBE.value == 1
