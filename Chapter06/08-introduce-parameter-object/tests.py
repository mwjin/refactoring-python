import pytest
from example import readings_outside_range

from operating_plan import OperatingPlan


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
    readings = readings_outside_range(
        station,
        operating_plan.temperature_floor,
        operating_plan.temperature_ceiling,
    )
    temperatures = {reading["temp"] for reading in readings}
    assert len(temperatures) == 2
    assert 47 in temperatures
    assert 58 in temperatures
