from example import price

from order import Order


def test_price():
    assert price(Order(2000, 1000)) == 1925100
    assert price(Order(600, 100)) == 59600
