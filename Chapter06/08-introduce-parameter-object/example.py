def readings_outside_range(station, range):
    return [
        reading
        for reading in station["readings"]
        if not range.contains(reading["temp"])
    ]
