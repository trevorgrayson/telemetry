import timeit
from telemetry import get_client


class runtime:
    
    def __init__(self, service, report_name):
        self.service = service
        self.report_name = report_name

    def __call__(self, fn):
        def wrapper_bench(*args, **kwargs):
            start = timeit.timeit()
            result = fn(*args, **kwargs)
            end = timeit.timeit()

            elapsed = end - start
            get_client().gauge(self.service, 
                               self.report_name, 
                               elapsed)

            return result

        return wrapper_bench
