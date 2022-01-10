def disability_amount(employee):
    if (
        employee.seniority < 2
        or employee.months_disabled > 12
        or employee.is_part_time
    ):
        return 0
    return 1
