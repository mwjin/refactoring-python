def check_room_temperature(plan, room):
    low = room.days_temp_range.low
    high = room.days_temp_range.high
    if not plan.within_range(low, high):
        return "The room temperature is out of the range."
    return "The room temperature is in appropriate range."
