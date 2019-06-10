class Default:
    """ No-op Implementation """

    def __init__(self, *args, **kwargs):
        pass

    def gauge(self, name, value):
        pass

    def report_time(self, fn):
        pass

