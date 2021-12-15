from price_order import price_order
from product import Product
from shipping_method import ShippingMethod


def test_price_order():
    assert (
        price_order(
            Product(1000, 2500, 0.05), 100, ShippingMethod(5000, 1000, 2500)
        )
        == 200000
    )
    assert (
        price_order(
            Product(1500, 4500, 0.02), 25, ShippingMethod(5500, 1200, 1500)
        )
        == 67500
    )
