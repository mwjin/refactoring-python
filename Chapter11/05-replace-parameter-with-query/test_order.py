from order import Order


def test_final_price():
    assert Order(150, 1000).final_price == 135000
    assert Order(70, 120).final_price == 7980
