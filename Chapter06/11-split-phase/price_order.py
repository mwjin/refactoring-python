from price_data import PriceData


def price_order(product, quantity, shipping_method):
    _price_data = PriceData(product, quantity)
    price_data = {
        "base price": _price_data.base_price,
        "quantity": _price_data.quantity,
        "discount": _price_data.discount,
    }
    return apply_shipping(price_data, shipping_method)


def apply_shipping(price_data, shipping_method):
    shipping_per_case = (
        shipping_method.discounted_fee
        if price_data["base price"] > shipping_method.discount_threshold
        else shipping_method.fee_per_case
    )
    shipping_cost = price_data["quantity"] * shipping_per_case
    price = price_data["base price"] - price_data["discount"] + shipping_cost
    return price
