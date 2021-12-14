class Customer:
    def __init__(self, name, location) -> None:
        self._name = name
        self._location = location

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location
