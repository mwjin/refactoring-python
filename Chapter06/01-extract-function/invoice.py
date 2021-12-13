from datetime import date


class Invoice:
    def __init__(self, customer):
        self._customer = customer
        self._orders = []
        self._due_date = date.today()

    @property
    def customer(self):
        return self._customer

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, date):
        self._due_date = date

    @property
    def orders(self):
        return self._orders

    def add_order(self, order):
        self._orders.append(order)
