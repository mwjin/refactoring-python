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
    def final_price(self):
        base_price = self.quantity * self.item_price
        return self.discounted_price(base_price, self.discount_level)

    @property
    def discount_level(self):
        return 2 if self.quantity > 100 else 1

    def discounted_price(self, base_price, discount_level):
        if self.discount_level == 1:
            return base_price * 0.95
        elif self.discount_level == 2:
            return base_price * 0.9
        else:
            return base_price
