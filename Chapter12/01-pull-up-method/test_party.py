from department import Department
from employee import Employee


def test_department_annual_cost():
    assert Department().annual_cost == 12000


def test_employee_annual_cost():
    assert Employee().annual_cost == 1200
