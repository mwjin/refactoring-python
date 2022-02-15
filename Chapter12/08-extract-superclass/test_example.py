import pytest

from department import Department
from employee import Employee


def test_employee_annual_cost():
    assert Employee(1, "Minwoo Jeong", 500).annual_cost == 6000


@pytest.fixture
def staff():
    return [
        Employee(1, "A", 100),
        Employee(2, "B", 200),
        Employee(3, "C", 300),
        Employee(4, "D", 400),
        Employee(5, "E", 500),
    ]


def test_department_total_monthly_cost(staff):
    assert Department("Dept", staff).total_monthly_cost == 1500


def test_department_total_annual_cost(staff):
    assert Department("Dept", staff).total_annual_cost == 18000
