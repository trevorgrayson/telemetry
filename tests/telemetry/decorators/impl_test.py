from telemetry.decorators import runtime

INSTANCE = 'instance'


@runtime(lambda arg1, arg2: f"bar.value.{arg1}.{arg2}")
def method_with_args(arg1, arg2):
    pass


class FooClass:
    def __init__(self, inst):
        self.instance = inst

    @runtime(lambda self, *args: f"bar.{self.instance}.value.{args[0]}.{args[1]}")
    def run(self, arg1, arg2):
        pass


class TestImplDecorators:
    def test_decorator_with_self(self):
        foo = FooClass(INSTANCE)
        foo.run(1, 2)

        # assert PROBE.name == f"bar.instance.value.1.2"

    def test_decorator_with_args(self):
        method_with_args(1,2)
        # assert PROBE.name == f"bar.value.1.2"
