from client1 import base_charge
from client2 import taxable_charge
from client3 import basic_charge_amount
from reading import enrich_reading


def test_base_charge():
    global base_charge
    assert base_charge == 10000


def test_taxable_charge():
    global taxable_charge
    assert taxable_charge == 5000


def test_basic_charge_amount():
    global basic_charge_amount
    assert basic_charge_amount == 10000


def test_enrich_reading_returns_another():
    original = {"customer": "Minwoo", "quantity": 10, "month": 5, "year": 2017}
    result = enrich_reading(original)
    assert original != result
