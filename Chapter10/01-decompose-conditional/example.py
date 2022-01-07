def get_charge(quantity, date, plan):
    if not date < plan.summer_start and not date > plan.summer_end:
        charge = quantity * plan.summer_rate
    else:
        charge = quantity * plan.regular_rate + plan.regular_service_charge
    return charge
