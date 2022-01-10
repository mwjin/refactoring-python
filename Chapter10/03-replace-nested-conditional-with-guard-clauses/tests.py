from employee import Employee
from example import pay_amount


def test_pay_amount():
    assert pay_amount(Employee(True, True)) == {
        "amount": 0,
        "reasonCode": "SEP",
    }
    assert pay_amount(Employee(True, False)) == {
        "amount": 0,
        "reasonCode": "SEP",
    }
    assert pay_amount(Employee(False, True)) == {
        "amount": 0,
        "reasonCode": "RET",
    }
    assert pay_amount(Employee(False, False)) == {
        "amount": 10000,
        "reasonCode": "None",
    }

