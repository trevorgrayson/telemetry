from pytest import fixture
import telemetry

REASON = "TEST PASSED"


class NoOpTelemeter:
    def __init__(self):
        self.calls = 0

    def log(self, message):
        self.calls += 1


class TestHandlers:
    @fixture
    def probe(self):
        return NoOpTelemeter()

    @fixture
    def telemeter(self, probe):
        telem = telemetry.Telemeter()
        telem.add_handler(probe)
        return telem

    def test_default(self, probe):
        telemetry.add_handler(probe)
        telemetry.log(REASON)
        assert probe.calls == 1

    def test_unregistered_meter(self, telemeter, probe):
        telemeter.exception(REASON)
        assert probe.calls == 0

    def test_registered_meter(self, telemeter, probe):
        telemeter.log(REASON)
        assert probe.calls == 1
