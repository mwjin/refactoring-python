def pay_amount(employee):
    if employee.is_separated:
        return {"amount": 0, "reasonCode": "SEP"}
    if employee.is_retired:
        return {"amount": 0, "reasonCode": "RET"}
    # Something to calculate pay
    return {"amount": 10000, "reasonCode": "None"}


def adjusted_capital(instrument):
    result = 0
    if instrument.capital > 0:
        if instrument.interest_rate > 0 and instrument.duration > 0:
            result = (
                instrument.income
                / instrument.duration
                * instrument.adjustment_factor
            )
    return result
