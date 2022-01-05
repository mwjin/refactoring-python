from functools import reduce


class ProductionPlan:
    def __init__(self, production):
        self._production = production
        self._adjustments = []

    @property
    def production(self):
        return self._production

    def apply_adjustment(self, adjustment):
        self._adjustments.append(adjustment)
        self._production += adjustment.amount
