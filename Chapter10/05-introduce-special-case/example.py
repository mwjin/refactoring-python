from customer import BillingPlan


def get_customer_name(site):
    # Client 1
    return site.customer.name


def get_billing_plan(customer):
    # Client 2
    return customer.billing_plan


def reset_billing_plan(customer):
    # Client 3
    customer.billing_plan = BillingPlan("New")


def get_weeks_delinquent_in_last_year(customer):
    # Client 4
    return customer.payment_history.weeks_delinquent_in_last_year
