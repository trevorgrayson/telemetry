from pytest import raises
from extras import not_important
not_important('numpy')
not_important('garbage')


class TestExtrasGetters:
    def test_import_module(self):
        arr = numpy.array([0,1,2,3,4,5]) 

        assert arr[0] == 0


    def test_non_existing_module(self):
        assert garbage is None
