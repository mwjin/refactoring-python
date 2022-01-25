def check_room_temperature(plan, room):
    low = room.days_temp_range.low
    high = room.days_temp_range.high
    is_within_range = plan.within_range(low, high)
    if not is_within_range:
        return "The room temperature is out of the range."
    return "The room temperature is in appropriate range."
