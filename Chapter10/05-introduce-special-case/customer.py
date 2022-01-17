class Customer:
    def __init__(self, name, billing_plan, payment_history):
        self._name = name
        self._billing_plan = billing_plan
        self._payment_history = payment_history

    @property
    def name(self):
        return self._name

    @property
    def billing_plan(self):
        return self._billing_plan

    @billing_plan.setter
    def billing_plan(self, arg):
        self._billing_plan = arg

    @property
    def payment_history(self):
        return self._payment_history

    @property
    def is_unknown(self):
        return False


class UnknownCustomer:
    @property
    def is_unknown(self):
        return True

    @property
    def name(self):
        return "Resident"


class BillingPlan:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


class PaymentHistory:
    def __init__(self, weeks_delinquent_in_last_year):
        self._weeks_delinquent_in_last_year = weeks_delinquent_in_last_year

    @property
    def weeks_delinquent_in_last_year(self):
        return self._weeks_delinquent_in_last_year
