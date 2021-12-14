import pytest
from example3 import report_lines

from customer import Customer
from driver import Driver
from example1 import rating as rating1
from example2 import rating as rating2


def get_driver(num_late_delivery):
    driver = Driver()
    for _ in range(num_late_delivery):
        driver.do_late_delivery()
    return driver


@pytest.fixture
def customer():
    return Customer("Minwoo Jeong", "South Korea")


def test_rating1():
    assert rating1(get_driver(10)) == 2
    assert rating1(get_driver(5)) == 1
    assert rating1(get_driver(1)) == 1


def test_rating2():
    assert rating2(get_driver(10)) == 2
    assert rating2(get_driver(5)) == 1
    assert rating2(get_driver(1)) == 1


def test_report_lines(customer):
    assert report_lines(customer) == [
        ["name", "Minwoo Jeong"],
        ["location", "South Korea"],
    ]
