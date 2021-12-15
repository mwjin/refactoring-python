def readings_outside_range(station, range):
    return [
        reading
        for reading in station["readings"]
        if reading["temp"] < range.min or reading["temp"] > range.max
    ]
