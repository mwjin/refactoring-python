def pay_amount(employee):
    if employee.is_separated:
        return {"amount": 0, "reasonCode": "SEP"}
    if employee.is_retired:
        return {"amount": 0, "reasonCode": "RET"}
    # Something to calculate pay
    return {"amount": 10000, "reasonCode": "None"}
