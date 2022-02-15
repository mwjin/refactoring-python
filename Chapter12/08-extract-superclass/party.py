class Party:
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def annual_cost(self):
        return self.monthly_cost * 12
