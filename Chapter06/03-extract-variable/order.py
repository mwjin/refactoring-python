class Order:
    def __init__(self, quantity, item_price):
        self._quantity = quantity
        self._item_price = item_price

    @property
    def quantity(self):
        return self._quantity

    @property
    def item_price(self):
        return self._item_price

    @property
    def price(self):
        return (
            self.quantity * self.item_price
            - max(0, self.quantity - 500) * self.item_price * 0.05
            + min(self.quantity * self.item_price * 0.1, 100)
        )
