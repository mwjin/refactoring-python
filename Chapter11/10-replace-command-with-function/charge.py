class ChargeCalculator:
    def __init__(self, customer, usage, provider):
        self._customer = customer
        self._usage = usage
        self._provider = provider

    @property
    def base_charge(self):
        return self._customer.base_rate * self._usage

    @property
    def charge(self):
        return self.base_charge + self._provider.connection_charge


def get_month_charge(customer, usage, provider):
    month_charge = ChargeCalculator(customer, usage, provider).charge
    return month_charge
