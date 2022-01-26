import thermostat


def get_temp_instruction(plan):
    if (
        plan.target_temperature(thermostat.selected_temperature)
        > thermostat.current_temperature
    ):
        return "Set to heat"
    elif (
        plan.target_temperature(thermostat.selected_temperature)
        < thermostat.current_temperature
    ):
        return "Set to cool"
    else:
        return "Set off"
