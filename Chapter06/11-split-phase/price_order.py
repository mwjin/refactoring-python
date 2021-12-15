def price_order(product, quantity, shipping_method):
    base_price = product.base_price * quantity
    discount = (
        max(quantity - product.discount_threshold, 0)
        * product.base_price
        * product.discount_rate
    )
    price_data = {"base price": base_price, "quantity": quantity}
    price = apply_shipping(price_data, shipping_method, discount)
    return price


def apply_shipping(price_data, shipping_method, discount):
    shipping_per_case = (
        shipping_method.discounted_fee
        if price_data["base price"] > shipping_method.discount_threshold
        else shipping_method.fee_per_case
    )
    shipping_cost = price_data["quantity"] * shipping_per_case
    price = price_data["base price"] - discount + shipping_cost
    return price
