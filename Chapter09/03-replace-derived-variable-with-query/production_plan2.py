from functools import reduce


class ProductionPlan:
    def __init__(self, production):
        self._initial_production = production
        self._production_accumulator = 0
        self._adjustments = []

    @property
    def production(self):
        return self._initial_production + self._production_accumulator

    def apply_adjustment(self, adjustment):
        self._adjustments.append(adjustment)
        self._production_accumulator += adjustment.amount
