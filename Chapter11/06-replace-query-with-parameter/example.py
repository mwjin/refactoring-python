import thermostat


def get_temp_instruction(plan):
    if (
        plan.new_target_temperature(thermostat.selected_temperature)
        > thermostat.current_temperature
    ):
        return "Set to heat"
    elif (
        plan.new_target_temperature(thermostat.selected_temperature)
        < thermostat.current_temperature
    ):
        return "Set to cool"
    else:
        return "Set off"
