class Address:
    def __init__(self, state):
        self._state = state

    @property
    def state(self):
        return self._state
