from party import Party


class Department(Party):
    @property
    def monthly_cost(self):
        return 1000

    @property
    def total_annual_cost(self):
        return self.monthly_cost * 12
