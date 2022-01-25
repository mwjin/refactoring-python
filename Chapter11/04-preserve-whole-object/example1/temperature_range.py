class TemperatureRange:
    def __init__(self, low, high) -> None:
        self._low = low
        self._high = high

    @property
    def low(self):
        return self._low

    @property
    def high(self):
        return self._high
