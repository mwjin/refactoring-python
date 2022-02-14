from party import Party


class Employee(Party):
    @property
    def monthly_cost(self):
        return 100

    @property
    def annual_cost(self):
        return self.monthly_cost * 12
