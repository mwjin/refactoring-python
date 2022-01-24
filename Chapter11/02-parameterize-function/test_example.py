from example import base_charge


def test_base_charge():
    assert base_charge(50) == "$1.50"
    assert base_charge(120) == "$4.00"
    assert base_charge(240) == "$10.80"
    assert base_charge(500) == "$29.00"
