from point import Point
from track_summary import track_summary


def test_track_summary():
    points = [
        Point(51.5007, 0.1246),
        Point(40.6892, 70.1245),
    ]
    assert track_summary(points) == {
        "distance": 4410.694,
        "pace": 3.779,
        "time": 1000000,
    }
