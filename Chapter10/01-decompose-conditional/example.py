def get_charge(quantity, date, plan):
    charge = (
        get_summer_charge(quantity, plan)
        if is_summer(date, plan)
        else get_regular_charge(quantity, plan)
    )
    return charge


def is_summer(date, plan):
    return not date < plan.summer_start and not date > plan.summer_end


def get_summer_charge(quantity, plan):
    return quantity * plan.summer_rate


def get_regular_charge(quantity, plan):
    return quantity * plan.regular_rate + plan.regular_service_charge
