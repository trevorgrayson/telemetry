from pytest import fixture

import telemetry
from telemetry import runtime
from time import sleep


class TestTelemetry:
  
    @fixture
    def telem(self):
        return telemetry.Telemeter()
    
    def test_constants(self, telem):
        assert(len(telemetry.SERVICES) > 1)
    
    def test_init(self, telem):
        assert(telem.service('statsd').__class__.__name__ == 'Statsd')
    
    def test_gauge(self, telem):
        telem.gauge('statsd', 'some.gauge.name', 123)

    def test_benchmark(self):
        report_name = "stats.runtime.name"

        with runtime('statsd', report_name):
            sleep(1)
        
        assert(telemetry.get_client().name == report_name)
        assert(int(telemetry.get_client().value/1000) == 1)
