from order import Order, Item


def test_order_price():
    assert Order(10, Item(1000)).price == 9500
    assert Order(7, Item(550)).price == 3657.5
    assert Order(3, Item(250)).price == 735
