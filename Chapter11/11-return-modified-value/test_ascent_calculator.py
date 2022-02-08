from ascent_calculator import AscentCalculator
from point import Point


def points(nums):
    return [Point(n) for n in nums]


def test_total_ascent():
    assert AscentCalculator(points([1, 2, 3, 4, 5])).total_ascent == 4
    assert AscentCalculator(points([1, 2, 1, 7, 2])).total_ascent == 7
    assert AscentCalculator(points([3, 2, 7, 5, 11])).total_ascent == 11
