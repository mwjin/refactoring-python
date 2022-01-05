class Scenario:
    def __init__(self, delay, primary_force, secondary_force, mass) -> None:
        self._delay = delay
        self._primary_force = primary_force
        self._secondary_force = secondary_force
        self._mass = mass

    @property
    def delay(self):
        return self._delay

    @property
    def primary_force(self):
        return self._primary_force

    @property
    def secondary_force(self):
        return self._secondary_force

    @property
    def mass(self):
        return self._mass
