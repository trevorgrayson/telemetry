class TelemeterLogging:
    def message(self, msg):
        [handler.message(msg) for handler in self.handlers
         if getattr(handler, 'message')]

    def info(self, msg):
        self.message(f"INFO: {msg}")

    def warn(self, msg):
        self.message(f"WARNING: {msg}")

    def error(self, msg):
        self.message(f"ERROR: {msg}")
