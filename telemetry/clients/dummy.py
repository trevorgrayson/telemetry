class DummyTelemeter:
    _messages = []

    def message(self, msg):
        self._messages.append(msg)
