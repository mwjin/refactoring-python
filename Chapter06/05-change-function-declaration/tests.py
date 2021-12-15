import math

from circum import circum


def test_circum():
    assert circum(3) == 2 * math.pi * 3
