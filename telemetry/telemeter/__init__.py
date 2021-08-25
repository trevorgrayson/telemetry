import logging
from telemetry import decorators as decor


class NoHandler(Exception):
    pass


class TelemeterConfigException(Exception):
    pass


class Telemeter(decor.Decorators):
    def __init__(self, config_errors=False):
        self.handlers = []
        self.config_errors = config_errors

    def addHandler(self, handler):
        self.handlers.append(handler)

    # def find_handlers(self, configs):
    #     for handler in registry:
    #         if all([v in configs.keys() for v in handler.__requires__]):
    #             self.addHandler(handler())

    def __getattr__(self, name):
        """
        Look for handlers that implement the method being called. Delegate
        the message to each handler.

        Consider whitelisting methods, to confirm the method being called
        fits into the API. method list: logging methods, gauges.
        """
        # TODO could cache or preprocess next line per each name to save time.
        apropos = filter(lambda handler: getattr(handler, name), self.handlers)

        def delegate(*args, **kwargs):
            for handler in apropos:
                getattr(handler, name)(*args, **kwargs)

        if apropos:
            return delegate
        else:
            logging.warning(f"No delegates for {name} method.")
            if self.config_errors:
                raise NoHandler(f"No Telemetery Handlers for method `{name}`")
