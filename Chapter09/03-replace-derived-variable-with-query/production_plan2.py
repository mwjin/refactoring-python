from functools import reduce


class ProductionPlan:
    def __init__(self, production):
        self._initial_production = production
        self._production_accumulator = 0
        self._adjustments = []

    @property
    def production(self):
        assert (
            self._production_accumulator
            == self.calculated_production_accumulator
        )
        return self._initial_production + self._production_accumulator

    @property
    def calculated_production_accumulator(self):
        return reduce(lambda sum, a: sum + a.amount, self._adjustments, 0)

    def apply_adjustment(self, adjustment):
        self._adjustments.append(adjustment)
        self._production_accumulator += adjustment.amount
