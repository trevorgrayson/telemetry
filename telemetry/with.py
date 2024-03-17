import time


class runtime:

    def __init__(self, report_name, meters):
        self.meters = meters
        self.report_name = report_name

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, type, value, traceback):
        end = time.time()

        elapsed = (end - self.start) * 1000
        self.meters.gauge(self.report_name,
                          elapsed)

