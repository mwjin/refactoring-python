import math

from circum import circumference


def test_circumference():
    assert circumference(3) == 2 * math.pi * 3
