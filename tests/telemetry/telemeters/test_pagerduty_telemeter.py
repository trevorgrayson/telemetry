from pytest import raises
from telemetry import PagerDutyTelemeter
from telemetry.telemeter import TelemeterConfigException


class TestSlackTelemeter:
    def test_init_fail(self):
        with raises(TelemeterConfigException):
            PagerDutyTelemeter(raises=True)

    def test_init_silent_fail(self):
        meter = PagerDutyTelemeter()
        assert meter.routing_key is None

    def test_explicit_init_silent_fail(self):
        meter = PagerDutyTelemeter(routing_key=None)
        assert meter.routing_key is None

    def test_init_room_id(self):
        routing_key = 'T123/Y456/Zabc'
        meter = PagerDutyTelemeter(routing_key=routing_key)
        assert meter.routing_key == routing_key
