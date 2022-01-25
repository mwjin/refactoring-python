class Room:
    def __init__(self, days_temp_range) -> None:
        self._days_temp_range = days_temp_range

    @property
    def days_temp_range(self):
        return self._days_temp_range
