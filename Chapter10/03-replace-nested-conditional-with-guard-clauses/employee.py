class Employee:
    def __init__(self, is_separated, is_retired) -> None:
        self._is_separated = is_separated
        self._is_retired = is_retired

    @property
    def is_separated(self):
        return self._is_separated

    @property
    def is_retired(self):
        return self._is_retired
