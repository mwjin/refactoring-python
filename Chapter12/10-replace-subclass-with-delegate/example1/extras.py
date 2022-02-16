class Extras:
    def __init__(self, premium_fee) -> None:
        self._premium_fee = premium_fee

    @property
    def premium_fee(self):
        return self._premium_fee

    def set_dinner(self):
        self.dinner = True
