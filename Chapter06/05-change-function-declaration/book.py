class Book:
    def __init__(self):
        self._reservations = []

    def zz_add_reservation(self, customer, is_priority):
        self._reservations.append(customer)

    @property
    def reservations(self):
        return list(self._reservations)
