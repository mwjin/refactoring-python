from datetime import datetime

import pytest

from example import get_charge
from plan import Plan


@pytest.fixture
def plan():
    return Plan(
        {
            "summer_start": "2021-07-01",
            "summer_end": "2021-09-30",
            "summer_rate": 0.2,
            "regular_rate": 0.1,
            "regular_service_charge": 10000,
        }
    )


def test_get_charge(plan):
    summer_date = datetime(2021, 8, 15)
    assert get_charge(1000, summer_date, plan) == 200
    no_summer_date = datetime(2021, 2, 17)
    assert get_charge(1000, no_summer_date, plan) == 10100

