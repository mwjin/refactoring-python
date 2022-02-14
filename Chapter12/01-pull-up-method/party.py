class Party:
    @property
    def monthly_cost(self):
        raise NotImplementedError(
            "A subclass of 'Party' must implement this property."
        )

    @property
    def annual_cost(self):
        return self.monthly_cost * 12
