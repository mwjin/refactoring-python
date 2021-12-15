class Product:
    def __init__(self, base_price, discount_threshold, discount_rate) -> None:
        self._base_price = base_price
        self._discount_threshold = discount_threshold
        self._discount_rate = discount_rate

    @property
    def base_price(self):
        return self._base_price

    @property
    def discount_threshold(self):
        return self._discount_threshold

    @property
    def discount_rate(self):
        return self._discount_rate
