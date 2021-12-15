class OperatingPlan:
    def __init__(self, temperature_floor, temperature_ceiling):
        self._temperature_floor = temperature_floor
        self._temperature_ceiling = temperature_ceiling

    @property
    def temperature_floor(self):
        return self._temperature_floor

    @property
    def temperature_ceiling(self):
        return self._temperature_ceiling
