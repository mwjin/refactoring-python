import pytest

import thermostat
from example import get_temp_instruction
from heating_plan import HeatingPlan


@pytest.fixture
def plan():
    return HeatingPlan(15, 30)


def test_get_temp_instruction(plan):
    thermostat.set_selected_temperature(25)
    thermostat.set_current_temperature(10)
    assert get_temp_instruction(plan) == "Set to heat"
    thermostat.set_current_temperature(25)
    assert get_temp_instruction(plan) == "Set off"
    thermostat.set_current_temperature(30)
    assert get_temp_instruction(plan) == "Set to cool"


def test_get_temp_instruction_low_selected_temp(plan):
    thermostat.set_selected_temperature(12)
    thermostat.set_current_temperature(10)
    assert get_temp_instruction(plan) == "Set to heat"
    thermostat.set_current_temperature(15)
    assert get_temp_instruction(plan) == "Set off"
    thermostat.set_current_temperature(25)
    assert get_temp_instruction(plan) == "Set to cool"


def test_get_temp_instruction_high_selected_temp(plan):
    thermostat.set_selected_temperature(32)
    thermostat.set_current_temperature(25)
    assert get_temp_instruction(plan) == "Set to heat"
    thermostat.set_current_temperature(30)
    assert get_temp_instruction(plan) == "Set off"
    thermostat.set_current_temperature(32)
    assert get_temp_instruction(plan) == "Set to cool"
