from pytest import fixture, raises
from telemetry import PagerDutyTelemeter
from telemetry.clients.pagerduty import HOSTNAME

CLIENT_DEFAULT = "client_default"


class TestPagerDutySource:
    @fixture
    def client(self):
        return PagerDutyTelemeter(source=CLIENT_DEFAULT)

    def test_client_default(self, client):
        source = client.payload("test")['payload']['source']
        assert source == CLIENT_DEFAULT

    def test_payload(self, client):
        expectation = "passed_value"
        source = client.payload("test",
                                source=expectation)['payload']['source']
        assert source == expectation

    def test_no_value(self, client):
        assert PagerDutyTelemeter().payload("test")['payload']['source'] is None


class TestPagerDutySummary:
    @fixture
    def client(self):
        return PagerDutyTelemeter(source=CLIENT_DEFAULT)

    def test_client_default(self, client):
        summary = client.payload(CLIENT_DEFAULT)['payload']['summary']
        assert summary == CLIENT_DEFAULT

    def test_payload(self, client):
        expectation = "ArithmeticError: failure"
        summary = client.payload(ArithmeticError("failure"),
                                 source=expectation)['payload']['summary']
        assert summary == expectation

    def test_no_value(self, client):
        assert PagerDutyTelemeter().payload("test")['payload']['summary'] == 'test'

    def test_dedupe_key_default(self, client):
        result = client.payload(ArithmeticError("test"))['dedup_key']

        assert result == f"{HOSTNAME}-ArithmeticError:test"

    def test_dedupe_key_value(self, client):
        result = client.payload(ArithmeticError("test"),
                                dedupe_key="dedupe")['dedup_key']

        assert result == "dedupe"

    def test_catches(self, client):
        @client.catch("test")
        def test():
            raise ArithmeticError("test")