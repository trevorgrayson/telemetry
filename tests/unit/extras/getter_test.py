from pytest import raises, mark
import extras

class TestExtrasGetters:
    def test_get_module(self):
        numpy = extras.get('numpy')
        # assert type(numpy.array([1,2,3,4,5])) == numpy.array
        arr = numpy.array([0,1,2,3,4,5]) 

        assert arr[0] == 0


    def test_get_non_existing_module(self):
        nopy = extras.get('nopy')

        assert nopy is None


    @mark.skip("nice to have, jacking module")
    def test_brackets(self):
        numpy = extras['numpy']
        assert isinstance(numpy.array([1,2,3,4,5]), numpy.array)

