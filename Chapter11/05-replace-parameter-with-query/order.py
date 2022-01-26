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
        if self.quantity > 100:
            discount_level = 2
        else:
            discount_level = 1
        return self.discounted_price(base_price, discount_level)

    def discounted_price(self, base_price, discount_level):
        if discount_level == 1:
            return base_price * 0.95
        elif discount_level == 2:
            return base_price * 0.9
        else:
            return base_price
