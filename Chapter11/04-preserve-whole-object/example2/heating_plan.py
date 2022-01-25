class HeatingPlan:
    def __init__(self, temperature_range) -> None:
        self._temperature_range = temperature_range

    def within_range(self, bottom, top):
        return (
            bottom >= self._temperature_range.low
            and top <= self._temperature_range.high
        )

    def new_within_range(self, temp_range):
        low = temp_range.low
        high = temp_range.high
        is_within_range = self.within_range(low, high)
        return is_within_range
