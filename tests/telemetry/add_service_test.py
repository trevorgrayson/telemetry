from pytest import fixture
import telemetry

WHOOPS = 'whoops'


class FakeService:
    def __init__(self):
        self.reasons = []

    def exception(self, reason):
        self.reasons.append(reason)


class TestAddService:
    @fixture
    def fake(self):
        return FakeService()

    def test_not_mounted(self, fake):
        telemetry.exception(WHOOPS)
        assert fake.reasons == []


    def test_mounted(self, fake):
        telemetry.add_service(fake)
        telemetry.exception(WHOOPS)
        assert fake.reasons == [WHOOPS]
