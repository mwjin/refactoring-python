def get_charge(quantity, date, plan):
    if is_summer(date, plan):
        charge = get_summer_charge(quantity, plan)
    else:
        charge = quantity * plan.regular_rate + plan.regular_service_charge
    return charge


def is_summer(date, plan):
    return not date < plan.summer_start and not date > plan.summer_end


def get_summer_charge(quantity, plan):
    return quantity * plan.summer_rate

