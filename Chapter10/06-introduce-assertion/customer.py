class Customer:
    def __init__(self, discount_rate) -> None:
        self._discount_rate = discount_rate

    @property
    def discount_rate(self):
        return self._discount_rate

    def apply_discount(self, number):
        return (
            number - (self.discount_rate * number)
            if self.discount_rate
            else number
        )
