import pytest

from province import Province, sample_province_data


@pytest.fixture(scope="function")
def asia():
    return Province(sample_province_data())


@pytest.fixture(scope="function")
def province_no_producer():
    data = {
        "name": "No producers",
        "producers": [],
        "demand": 30,
        "price": 20,
    }
    return Province(data)


def test_province_short_fall(asia):
    assert asia.shortfall == 5


def test_province_profit(asia):
    assert asia.profit == 230


def test_set_production_to_producer(asia):
    asia.producers[0].production = 20
    assert asia.shortfall == -6
    assert asia.profit == 292


def test_province_no_producer_short_fall(province_no_producer):
    assert province_no_producer.shortfall == 30


def test_province_no_producer_profit(province_no_producer):
    assert province_no_producer.profit == 0


def test_province_zero_demand(asia):
    asia.demand = 0
    assert asia.shortfall == -25
    assert asia.profit == 0


def test_province_negative_demand(asia):
    asia.demand = -1
    assert asia.shortfall == -26
    assert asia.profit == -10


def test_province_empty_string_demand(asia):
    with pytest.raises(ValueError):
        asia.demand = ""


def test_string_for_producers():
    data = {
        "name": "String producers",
        "producers": "",
        "demand": 30,
        "price": 20,
    }
    province = Province(data)
    assert province.shortfall == 0
