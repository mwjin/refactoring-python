def pay_amount(employee):
    if employee.is_separated:
        return {"amount": 0, "reasonCode": "SEP"}
    if employee.is_retired:
        return {"amount": 0, "reasonCode": "RET"}
    # Something to calculate pay
    return {"amount": 10000, "reasonCode": "None"}


def adjusted_capital(instrument):
    if (
        instrument.capital <= 0
        or instrument.interest_rate <= 0
        or instrument.duration <= 0
    ):
        return 0
    return (
        instrument.income / instrument.duration * instrument.adjustment_factor
    )
