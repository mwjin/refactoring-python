from customer import Customer


def test_apply_discount():
    assert Customer(0.2).apply_discount(100) == 80
    assert Customer(0.32).apply_discount(100) == 68
