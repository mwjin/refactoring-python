from datetime import datetime


class Customer:
    def __init__(self, name, discount_rate) -> None:
        self._name = name
        self._discount_rate = discount_rate
        self._contract = CustomerContract(datetime.today())

    @property
    def discount_rate(self):
        return self._discount_rate

    def _set_discount_rate(self, discount_rate):
        self._discount_rate = discount_rate

    def become_preferred(self):
        self._set_discount_rate(self.discount_rate + 0.03)
        # Other good things...

    def apply_discount(self, amount):
        return amount - amount * self.discount_rate


class CustomerContract:
    def __init__(self, start_date) -> None:
        self._start_date = start_date
