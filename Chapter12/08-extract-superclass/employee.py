from party import Party


class Employee(Party):
    def __init__(self, id, name, monthly_cost) -> None:
        super().__init__()
        self._id = id
        self._name = name
        self._monthly_cost = monthly_cost

    @property
    def monthly_cost(self):
        return self._monthly_cost

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def annual_cost(self):
        return self._monthly_cost * 12
