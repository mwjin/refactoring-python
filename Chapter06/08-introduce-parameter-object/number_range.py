class NumberRange:
    def __init__(self, min, max):
        self._data = {"min": min, "max": max}

    @property
    def min(self):
        return self._data["min"]

    @property
    def max(self):
        return self._data["max"]
