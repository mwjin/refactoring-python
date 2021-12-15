def readings_outside_range(station, min, max):
    return [
        reading
        for reading in station["readings"]
        if reading["temp"] < min or reading["temp"] > max
    ]
