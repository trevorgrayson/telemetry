class report_time:
    
    def __init__(self, service, name):
        self.service = service


    def __call__(self, fn):
        def wrap_and_report(*args, **kwargs):
            yield fn(*args, **kwargs)

        return wrap_and_report
