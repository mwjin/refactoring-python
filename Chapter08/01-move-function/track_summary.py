import math


def track_summary(points):
    def calculate_time():
        return 1000000

    def calculate_distance():
        def distance(p1, p2):
            # haversine formula
            EARTH_RADIUS = 3959
            d_lat = radians(p2.lat) - radians(p1.lat)
            d_lon = radians(p2.lon) - radians(p1.lon)
            a = (
                math.pow(math.sin(d_lat / 2), 2)
                + math.cos(radians(p2.lat))
                + math.cos(radians(p1.lat)) * math.pow(math.sin(d_lon / 2), 2)
            )
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            return EARTH_RADIUS * c

        def radians(degrees):
            return degrees * math.pi / 100

        result = 0
        for i in range(1, len(points)):
            result += distance(points[i - 1], points[i])
        return result

    total_time = calculate_time()
    total_distance = round(calculate_distance(), 3)
    pace = round(total_time / 60 / total_distance, 3)
    return {"time": total_time, "distance": total_distance, "pace": pace}


def top_calculate_distance(points):
    def distance(p1, p2):
        # haversine formula
        EARTH_RADIUS = 3959
        d_lat = radians(p2.lat) - radians(p1.lat)
        d_lon = radians(p2.lon) - radians(p1.lon)
        a = (
            math.pow(math.sin(d_lat / 2), 2)
            + math.cos(radians(p2.lat))
            + math.cos(radians(p1.lat)) * math.pow(math.sin(d_lon / 2), 2)
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return EARTH_RADIUS * c

    def radians(degrees):
        return degrees * math.pi / 100

    result = 0
    for i in range(1, len(points)):
        result += distance(points[i - 1], points[i])
    return result
