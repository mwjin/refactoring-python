from employee import Employee
from example import disability_amount, vacation_amount


def test_disability_amount():
    assert disability_amount(Employee(1, 2, False, False)) == 0
    assert disability_amount(Employee(2, 13, False, False)) == 0
    assert disability_amount(Employee(2, 2, True, False)) == 0
    assert disability_amount(Employee(2, 2, False, False)) == 1


def test_vacation_amount():
    assert vacation_amount(Employee(20, 2, False, False)) == 0.5
    assert vacation_amount(Employee(20, 2, False, True)) == 1
    assert vacation_amount(Employee(10, 2, False, False)) == 0.5
    assert vacation_amount(Employee(10, 2, False, True)) == 0.5

