def disability_amount(employee):
    if employee.seniority < 2 or employee.months_disabled > 12:
        return 0
    if employee.is_part_time:
        return 0
    return 1
