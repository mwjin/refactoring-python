from customer import BillingPlan, Customer, UnknownCustomer


def get_customer_name(site):
    # Client 1
    customer = site.customer

    if is_unknown(customer):
        customer_name = "Resident"
    else:
        customer_name = customer.name

    return customer_name


def get_billing_plan(customer):
    # Client 2
    return (
        BillingPlan("Basic") if is_unknown(customer) else customer.billing_plan
    )


def reset_billing_plan(customer):
    # Client 3
    if not is_unknown(customer):
        customer.billing_plan = BillingPlan("New")


def get_weeks_delinquent_in_last_year(customer):
    # Client 4
    return (
        0
        if is_unknown(customer)
        else customer.payment_history.weeks_delinquent_in_last_year
    )


def is_unknown(customer):
    if not (
        isinstance(customer, Customer) or isinstance(customer, UnknownCustomer)
    ):
        raise ValueError(f"'{customer}' is not an actual customer.")
    return customer.is_unknown
