class Customer:
    def __init__(self, discount_rate) -> None:
        self._discount_rate = discount_rate

    @property
    def discount_rate(self):
        return self._discount_rate

    def apply_discount(self, number):
        if self.discount_rate:
            assert self.discount_rate >= 0
            return number - (self.discount_rate * number)
        else:
            return number
