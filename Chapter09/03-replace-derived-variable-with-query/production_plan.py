from functools import reduce


class ProductionPlan:
    def __init__(self):
        self._production = 0
        self._adjustments = []

    @property
    def production(self):
        return reduce(lambda sum, a: sum + a.amount, self._adjustments, 0)

    def apply_adjustment(self, adjustment):
        self._adjustments.append(adjustment)
        self._production += adjustment.amount
