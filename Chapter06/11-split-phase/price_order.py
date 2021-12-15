from price_data import PriceData


def price_order(product, quantity, shipping_method):
    price_data = calculate_price_data(product, quantity)
    return apply_shipping(price_data, shipping_method)


def calculate_price_data(product, quantity):
    _price_data = PriceData(product, quantity)
    price_data = {
        "base price": _price_data.base_price,
        "quantity": quantity,
        "discount": _price_data.discount,
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
