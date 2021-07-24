from pytest import fixture

import telemetry
from time import sleep



class TestTelemetry:
  
    @fixture
    def meter(self):
        meter = telemetry.get_telemeter()
        meter.addHandler(telemetry.Statsd('localhost'))
        return meter

    def test_gauge(self, meter):
        metric = 'some.gauge.name'
        value = 123
        meter.gauge(metric, value)

        #assert(telemetry.get_client().name == metric)
        #assert(telemetry.get_client().value == value)

    def test_incr(self, meter):
        metric = 'some.incr.name'
        meter.incr(metric)

        # assert(telemetry.get_client().name == metric)
        # assert(telemetry.get_client().value == 1)

    def test_decr(self, meter):
        metric = 'some.decr.name'
        meter.decr(metric)

    # def test_runtime(self):
    #     report_name = "stats.runtime.name"

    #     with runtime(report_name):
    #         sleep(1)
    #
    #     # assert(telemetry.get_client().name == report_name)
    #     # assert(telemetry.get_client().value // 1000 == 1)

    # def test_runtime_micro(self):
    #     report_name = "stats.runtime.name"

    #     with runtime(report_name):
    #         sleep(0.25)
    #
    #     # value = telemetry.get_client().value // 10
    #     # assert(telemetry.get_client().name == report_name)
    #     assert(value == 25)
