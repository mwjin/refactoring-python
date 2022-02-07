class ChargeCalculator:
    def __init__(self, customer, usage, provider):
        pass

    def charge(self, customer, usage, provider):
        base_charge = customer.base_rate * usage
        return base_charge + provider.connection_charge


def get_month_charge(customer, usage, provider):
    month_charge = charge(customer, usage, provider)
    return month_charge


def charge(customer, usage, provider):
    return ChargeCalculator(customer, usage, provider).charge(
        customer, usage, provider
    )
