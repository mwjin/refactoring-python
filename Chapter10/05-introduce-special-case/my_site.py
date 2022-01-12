class Site:
    def __init__(self, customer):
        self._customer = customer

    @property
    def customer(self):
        return self._customer
