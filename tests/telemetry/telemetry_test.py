from pytest import fixture

import telemetry
from telemetry import runtime
from time import sleep
from unit.telemetry import TelemetryProbe


class TestTelemetry:

    @fixture
    def probe(self):
        return TelemetryProbe()
    @fixture
    def telem(self, probe):
        telem = telemetry.Telemeter()
        telem.add_handler(probe)
        return telem

    def test_gauge(self, telem, probe):
        metric = 'some.gauge.name'
        value = 123

        telem.gauge(metric, value)

        assert(metric == probe.name)
        assert(value == probe.value)

    def test_incr(self, telem, probe):
        metric = 'some.incr.name'
        telem.incr(metric)

        assert(probe.name == metric)
        assert(probe.value == 1)

    def test_decr(self, telem):
        metric = 'some.decr.name'
        telem.decr(metric)

    # TODO fix these wrappers
    # def test_runtime(self):
    #     report_name = "stats.runtime.name"

    #     with runtime(report_name):
    #         sleep(1)
    #
    #     assert(telemetry.get_client().name == report_name)
    #     assert(telemetry.get_client().value // 1000 == 1)

    # def test_runtime_micro(self):
    #     report_name = "stats.runtime.name"

    #     with runtime(report_name):
    #         sleep(0.25)
    #
    #     value = telemetry.get_client().value // 10
    #     assert(telemetry.get_client().name == report_name)
    #     assert(value == 25)
