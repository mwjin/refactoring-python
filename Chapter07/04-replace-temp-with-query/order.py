class Order:
    def __init__(self, quantity, item):
        self._quantity = quantity
        self._item = item

    @property
    def price(self):
        base_price = self._quantity * self._item.price
        discount_factor = 0.98

        if base_price > 1000:
            discount_factor -= 0.03

        return base_price * discount_factor


class Item:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price
