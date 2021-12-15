import pytest
from example import readings_outside_range

from operating_plan import OperatingPlan
from number_range import NumberRange


@pytest.fixture
def station():
    return {
        "name": "ZB1",
        "readings": [
            {"temp": 47, "time": "2016-11-10 09:10"},
            {"temp": 53, "time": "2016-11-10 09:20"},
            {"temp": 58, "time": "2016-11-10 09:30"},
            {"temp": 53, "time": "2016-11-10 09:40"},
            {"temp": 51, "time": "2016-11-10 09:50"},
        ],
    }


@pytest.fixture
def operating_plan():
    return OperatingPlan(50, 55)


def test_readings_outside_range(station, operating_plan):
    range = NumberRange(
        operating_plan.temperature_floor, operating_plan.temperature_ceiling
    )
    readings = readings_outside_range(station, range)
    temperatures = {reading["temp"] for reading in readings}
    assert len(temperatures) == 2
    assert 47 in temperatures
    assert 58 in temperatures
