from charge import get_month_charge
from customer import Customer
from provider import Provider


def test_get_month_charge():
    assert get_month_charge(Customer(0.2), 1000, Provider(1000)) == 1200
    assert get_month_charge(Customer(0.2), 1000, Provider(1500)) == 1700
    assert get_month_charge(Customer(0.3), 1000, Provider(1500)) == 1800
    assert get_month_charge(Customer(0.3), 1525, Provider(1500)) == 1957.5
