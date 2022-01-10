class Employee:
    def __init__(self, seniority, months_disabled, is_part_time) -> None:
        self._seniority = seniority
        self._months_disabled = months_disabled
        self._is_part_time = is_part_time

    @property
    def seniority(self):
        return self._seniority

    @property
    def months_disabled(self):
        return self._months_disabled

    @property
    def is_part_time(self):
        return self._is_part_time
