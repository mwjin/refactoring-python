def price_order(product, quantity, shipping_method):
    base_price = product.base_price * quantity
    discount = (
        max(quantity - product.discount_threshold, 0)
        * product.base_price
        * product.discount_rate
    )
    shipping_per_case = (
        shipping_method.discounted_fee
        if base_price > shipping_method.discount_threshold
        else shipping_method.fee_per_case
    )
    shipping_cost = quantity * shipping_per_case
    price = base_price - discount + shipping_cost
    return price
