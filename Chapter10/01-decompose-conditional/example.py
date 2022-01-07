def get_charge(quantity, date, plan):
    if is_summer(date, plan):
        charge = quantity * plan.summer_rate
    else:
        charge = quantity * plan.regular_rate + plan.regular_service_charge
    return charge


def is_summer(date, plan):
    return not date < plan.summer_start and not date > plan.summer_end
