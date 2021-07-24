import timeit


class Runtime:
    def __init__(self, report_name, meter):
        self.report_name = report_name
        self.meter = meter

    def __call__(self, fn):
        def wrapper_bench(*args, **kwargs):
            start = timeit.timeit()
            result = fn(*args, **kwargs)
            end = timeit.timeit()

            elapsed = end - start

            report_name = self.report_name
            if isinstance(report_name, type(lambda:1)):
                report_name = self.report_name(*args, **kwargs)

            # get_client().timing(report_name, elapsed)

            return result

        return wrapper_bench


class Catch:
    def __init__(self, report_name, meter):
        self.report_name = report_name
        self.meter = meter

    def __call__(self, fn):
        def wrapper_catch(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except Exception as err:
                self.meter.message(err)
                raise err

        return wrapper_catch


class Decorators:
    def runtime(self, report_name):
        """wrapper method for functions"""
        return Runtime(report_name, self)

    def catch(self, report_name):
        """wrapper method for functions"""
        return Catch(report_name, self)

