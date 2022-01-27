class Candidate:
    def __init__(self, state) -> None:
        self._origin_state = state

    @property
    def origin_state(self):
        return self._origin_state
