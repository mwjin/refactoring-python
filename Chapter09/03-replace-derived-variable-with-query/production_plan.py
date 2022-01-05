class ProductionPlan:
    def __init__(self):
        self._production = 0
        self._adjustments = []

    @property
    def production(self):
        return self._production

    def apply_adjustment(self, adjustment):
        self._adjustments.append(adjustment)
        self._production += adjustment.amount
