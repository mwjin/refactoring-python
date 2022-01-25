class HeatingPlan:
    def __init__(self, temperature_range) -> None:
        self._temperature_range = temperature_range

    def new_within_range(self, range):
        return (
            range.low >= self._temperature_range.low
            and range.high <= self._temperature_range.high
        )
