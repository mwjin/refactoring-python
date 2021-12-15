def readings_outside_range(station, min, range):
    return [
        reading
        for reading in station["readings"]
        if reading["temp"] < min or reading["temp"] > range.max
    ]
