def pay_amount(employee):
    if employee.is_separated:
        return {"amount": 0, "reasonCode": "SEP"}
    if employee.is_retired:
        return {"amount": 0, "reasonCode": "RET"}
    # Something to calculate pay
    result = {"amount": 10000, "reasonCode": "None"}
    return result
