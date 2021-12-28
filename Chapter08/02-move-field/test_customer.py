from customer import Customer


def test_become_preferred():
    _customer = Customer("Minwoo Jeong", 0.03)
    _customer.become_preferred()
    assert _customer.discount_rate == 0.06


def test_apply_discount():
    assert Customer("Minwoo Jeong", 0.03).apply_discount(100) == 97
    assert Customer("Minwoo Jeong", 0.21).apply_discount(100) == 79
