def price(order):
    # price = base price - quantity discount + shipping
    base_price = order.quantity * order.item_price
    return (
        base_price
        - max(0, order.quantity - 500) * order.item_price * 0.05
        + min(base_price * 0.1, 100)
    )

