from pytest import raises
from telemetry import Telemeter


class ProbeTelemeter:
    def message(self, message):
        self.message = message


meter = Telemeter()
PROBE = ProbeTelemeter()
meter.addHandler(PROBE)


@meter.catch("some_error")
def shady_method(num):
    return 1/num


class TestExceptionThrowing:
    def test_sanity_check(self):
        result = shady_method(2)
        assert result == 0.5

    def test_catch_decorator(self):
        with raises(ZeroDivisionError):
            shady_method(0)

        assert PROBE.message == "division by zero"
