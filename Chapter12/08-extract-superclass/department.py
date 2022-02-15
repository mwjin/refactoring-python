from copy import copy
from functools import reduce

from party import Party


class Department(Party):
    def __init__(self, name, staff) -> None:
        super().__init__()
        self._name = name
        self._staff = staff

    @property
    def staff(self):
        return copy(self._staff)

    @property
    def name(self):
        return self._name

    @property
    def total_monthly_cost(self):
        return reduce(
            lambda sum, cost: sum + cost,
            map(lambda e: e.monthly_cost, self._staff),
            0,
        )

    @property
    def head_count(self):
        return len(self.staff)

    @property
    def total_annual_cost(self):
        return self.total_monthly_cost * 12
