def price(order):
    # price = base price - quantity discount + shipping
    base_price = order.quantity * order.item_price
    quantity_discount = max(0, order.quantity - 500) * order.item_price * 0.05

    return base_price - quantity_discount + min(base_price * 0.1, 100)

