def get_month_charge(customer, usage, provider):
    month_charge = charge(customer, usage, provider)
    return month_charge


def charge(customer, usage, provider):
    base_charge = customer.base_rate * usage
    return base_charge + provider.connection_charge
