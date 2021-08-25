from os import environ
from pytest import raises
from telemetry import SlackTelemeter
from telemetry.telemeter import TelemeterConfigException


for req in SlackTelemeter.__requires__:
    if req in environ:
        del environ[req]


class TestSlackTelemeter:
    def test_init_fail(self):
        with raises(TelemeterConfigException) as ex:
            SlackTelemeter(raises=True)

    def test_init_silent_fail(self):
        meter = SlackTelemeter()
        assert meter.room_id is None

    def test_explicit_init_silent_fail(self):
        meter = SlackTelemeter(room_id=None)
        assert meter.room_id is None

    def test_init_room_id(self):
        room_id = 'T123/Y456/Zabc'
        meter = SlackTelemeter(room_id=room_id)
        assert meter.room_id == room_id
