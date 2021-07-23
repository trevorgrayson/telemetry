class TelemeterLogging:
    def message(self, msg):
        [handler.message(msg) for handler in self.handlers
         if getattr(handler, 'message')]

