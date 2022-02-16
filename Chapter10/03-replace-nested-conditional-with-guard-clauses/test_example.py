from employee import Employee
from example import adjusted_capital, pay_amount
from instrument import Instrument


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


def test_adjusted_capital():
    instrument_data = {
        "capital": 10000,
        "interest_rate": 0.03,
        "duration": 12,
        "income": 12000,
        "adjustment_factor": 0.8,
    }
    assert adjusted_capital(Instrument(instrument_data)) == 800

    instrument_data["capital"] = 0
    assert adjusted_capital(Instrument(instrument_data)) == 0

    instrument_data["capital"] = 10000
    instrument_data["interest_rate"] = 0
    assert adjusted_capital(Instrument(instrument_data)) == 0

    instrument_data["interest_rate"] = 0.03
    instrument_data["duration"] = 0
    assert adjusted_capital(Instrument(instrument_data)) == 0
