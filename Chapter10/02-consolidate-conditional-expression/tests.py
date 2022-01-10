from employee import Employee
from example import disability_amount


def test_disability_amount():
    assert disability_amount(Employee(1, 2, False)) == 0
    assert disability_amount(Employee(2, 13, False)) == 0
    assert disability_amount(Employee(2, 2, True)) == 0
    assert disability_amount(Employee(2, 2, False)) == 1
