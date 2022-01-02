class Person:
    def __init__(self, name, photo) -> None:
        self._name = name
        self._photo = photo

    @property
    def name(self):
        return self._name

    @property
    def photo(self):
        return self._photo
