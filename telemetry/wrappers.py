import timeit
import telemetry


class report_time:
    
    def __init__(self, service, report_name):
        self.service = service
        self.report_name = report_name

    def __call__(self, fn):
        def wrapper_bench(*args, **kwargs):
            start = timeit.timeit()
            result = fn(*args, **kwargs)
            end = timeit.timeit()

            elapsed = end - start
            telemetry.get_client().gauge(self.service, 
                                         self.report_name, 
                                         elapsed)

            return result

        return wrapper_bench
