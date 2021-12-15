def price_order(product, quantity, shipping_method):
    price_data = calculate_price_data(product, quantity)
    price = apply_shipping(price_data, shipping_method)
    return price


def calculate_price_data(product, quantity):
    base_price = product.base_price * quantity
    discount = (
        max(quantity - product.discount_threshold, 0)
        * product.base_price
        * product.discount_rate
    )
    price_data = {
        "base price": base_price,
        "quantity": quantity,
        "discount": discount,
    }

    return price_data


def apply_shipping(price_data, shipping_method):
    shipping_per_case = (
        shipping_method.discounted_fee
        if price_data["base price"] > shipping_method.discount_threshold
        else shipping_method.fee_per_case
    )
    shipping_cost = price_data["quantity"] * shipping_per_case
    price = price_data["base price"] - price_data["discount"] + shipping_cost
    return price
