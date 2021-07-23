import logging


class Telemeter:
    def __init__(self):
        self.handlers = []

    def addHandler(self, handler):
        self.handlers.append(handler)

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
