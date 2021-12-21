class Course:
    def __init__(self, name, is_advanced) -> None:
        self._name = name
        self._is_advanced = is_advanced

    def __eq__(self, other):
        return self.name == other.name and self.is_advanced == other.is_advanced

    def __hash__(self):
        return hash((self._name, self._is_advanced))

    @property
    def name(self):
        return self._name

    @property
    def is_advanced(self):
        return self._is_advanced
