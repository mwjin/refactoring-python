class Book:
    def __init__(self):
        self._reservations = []

    def add_reservation(self, customer):
        self._reservations.append(customer)

    @property
    def reservations(self):
        return list(self._reservations)
