from price import price

from order import Order


def test_price():
    assert price(Order(2000, 1000)) == 1925100
    assert price(Order(600, 100)) == 59600


def test_order_price():
    assert Order(2000, 1000).price == 1925100
    assert Order(600, 100).price == 59600
