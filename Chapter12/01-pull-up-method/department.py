from party import Party


class Department(Party):
    @property
    def monthly_cost(self):
        return 1000
