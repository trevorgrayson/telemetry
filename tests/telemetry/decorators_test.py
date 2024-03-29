from pytest import raises

import telemetry

REPORT_NAME = 'some.key'

meter = telemetry.get_telemeter(__name__)


@meter.catch('some_report')
def exception_prone(ii):
    return 1/ii


class TestsExcept:
    def test_catch_pass(self):
        assert exception_prone(2) == 0.5
        
    def test_catch_throws(self):
        with raises(ZeroDivisionError):
            exception_prone(0)


@meter.runtime(REPORT_NAME)
def a_slow_function(a, b):
    return a + b


class TestRuntime:
    def test_constants(self):
        a, b = 1, 2
        result = a_slow_function(a, b)

        assert result == a + b
        # assert PROBE.name == REPORT_NAME
        # assert PROBE.value != 0
