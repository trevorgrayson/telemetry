import timeit


class runtime:
    def __init__(self, report_name, service='statsd'):
        self.service = service
        self.report_name = report_name

    def __call__(self, fn):
        def wrapper_bench(*args, **kwargs):
            start = timeit.timeit()
            result = fn(*args, **kwargs)
            end = timeit.timeit()

            elapsed = end - start

            report_name = self.report_name
            if isinstance(report_name, type(lambda:1)):
                report_name=self.report_name(*args, **kwargs)

            # get_client().timing(report_name, elapsed)

            return result

        return wrapper_bench


class catch:
    def __init__(self, report_name, service='airbrake'):
        self.service = service
        self.report_name = report_name

    def __call__(self, fn):
        def wrapper_catch(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except Exception as err:
                pass # IOU
                raise err

        return wrapper_catch
