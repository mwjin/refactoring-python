from example import distance_travelled
from scenario import Scenario


def test_distance_travelled():
    assert distance_travelled(Scenario(10, 5, 2, 10), 5) == 6.25
    assert distance_travelled(Scenario(30, 51, 26, 12), 17) == 614.125
    assert distance_travelled(Scenario(50, 121, 56, 27), 100) == 25000
