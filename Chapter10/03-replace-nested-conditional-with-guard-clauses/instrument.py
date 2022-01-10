class Instrument:
    def __init__(self, data) -> None:
        self._capital = data["capital"]
        self._interest_rate = data["interest_rate"]
        self._duration = data["duration"]
        self._income = data["income"]
        self._adjustment_factor = data["adjustment_factor"]

    @property
    def capital(self):
        return self._capital

    @property
    def interest_rate(self):
        return self._interest_rate

    @property
    def duration(self):
        return self._duration

    @property
    def income(self):
        return self._income

    @property
    def adjustment_factor(self):
        return self._adjustment_factor
