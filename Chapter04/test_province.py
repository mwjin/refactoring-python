import pytest

from province import Province, sample_province_data


@pytest.fixture(scope="function")
def asia():
    return Province(sample_province_data())


def test_province_short_fall(asia):
    assert asia.shortfall == 5


def test_province_profit(asia):
    assert asia.profit == 230


def test_set_production_to_producer(asia):
    asia.producers[0].production = 20
    assert asia.shortfall == -6
    assert asia.profit == 292
