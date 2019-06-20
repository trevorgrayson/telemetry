from pytest import fixture

import telemetry
from telemetry import runtime
from time import sleep
from unit.telemetry import TelemetryProbe


class TestTelemetry:
  
    @fixture
    def telem(self):
        return telemetry.Telemeter()
    
    def test_constants(self, telem):
        assert(len(telemetry.SERVICES) > 1)
    
    def test_init(self, telem):
        assert(telem.service('statsd').__class__.__name__ == 'Statsd')
    
    def test_gauge(self):
        metric = 'some.gauge.name'
        value = 123

        telemetry.gauge(metric, value)

        assert(telemetry.get_client().name == metric)
        assert(telemetry.get_client().value == value)

    def test_incr(self):
        metric = 'some.incr.name'
        telemetry.incr(metric)

        assert(telemetry.get_client().name == metric)
        # assert(telemetry.get_client().value == 1)

    def test_decr(self):
        metric = 'some.decr.name'
        telemetry.decr(metric)

    def test_runtime(self):
        report_name = "stats.runtime.name"

        with runtime(report_name):
            sleep(1)
        
        assert(telemetry.get_client().name == report_name)
        assert(telemetry.get_client().value // 1000 == 1)

    def test_runtime_micro(self):
        report_name = "stats.runtime.name"

        with runtime(report_name):
            sleep(0.25)
        
        value = telemetry.get_client().value // 10 
        assert(telemetry.get_client().name == report_name)
        assert(value == 25)
