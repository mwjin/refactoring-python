from party import Party


class Employee(Party):
    @property
    def monthly_cost(self):
        return 100
