class report_time:
    
    def __init__(self, service, name):
        self.service = service

    def __call__(self, fn):
        def wrap_and_report(*args, **kwargs):
            return fn(*args, **kwargs)

        return wrap_and_report


class runtime:

    def __init__(self, report_name):
        self.report_name = report_name

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, type, value, traceback):
        end = time.time()
        elapsed = (end - self.start) * 1000
