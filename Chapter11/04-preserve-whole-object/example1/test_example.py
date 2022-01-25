from example import check_room_temperature
from heating_plan import HeatingPlan
from room import Room
from temperature_range import TemperatureRange


def test_check_room_temperature():
    plan = HeatingPlan(TemperatureRange(15, 30))
    assert (
        check_room_temperature(plan, Room(TemperatureRange(20, 25)))
        == "The room temperature is in appropriate range."
    )
    assert (
        check_room_temperature(plan, Room(TemperatureRange(10, 20)))
        == "The room temperature is out of the range."
    )
    assert (
        check_room_temperature(plan, Room(TemperatureRange(31, 40)))
        == "The room temperature is out of the range."
    )
