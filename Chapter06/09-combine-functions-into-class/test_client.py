from client1 import base_charge
from client2 import taxable_charge
from client3 import basic_charge_amount


def test_base_charge():
    global base_charge
    assert base_charge == 10000


def test_taxable_charge():
    global taxable_charge
    assert taxable_charge == 5000


def test_basic_charge_amount():
    global basic_charge_amount
    assert basic_charge_amount == 10000
