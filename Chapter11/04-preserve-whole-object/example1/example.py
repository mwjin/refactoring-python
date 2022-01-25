def check_room_temperature(plan, room):
    if not plan.within_range(room.days_temp_range):
        return "The room temperature is out of the range."
    return "The room temperature is in appropriate range."
