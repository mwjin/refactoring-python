from order import Order


def test_order_is_expensive():
    assert Order(1100).is_expensive()
    assert not Order(1000).is_expensive()
    assert not Order(500).is_expensive()

