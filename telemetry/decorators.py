from time import time_ns
from . import get_client


class benchmark():
    def __init__(self, service, report_name):
        self.service = service
        self.report_name = report_name

    def __enter__(self):
        self.start = time_ns() // 1000000 

    def __exit__(self, type, value, traceback):
        end = time_ns() // 1000000 

        elapsed = end - self.start
        get_client().gauge(self.service,
                           self.report_name, 
                           elapsed)
