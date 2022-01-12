from customer import BillingPlan


def get_customer_name(site):
    # Client 1
    customer = site.customer

    if customer == "Unknown Customer":
        customer_name = "Resident"
    else:
        customer_name = customer.name

    return customer_name


def get_billing_plan(customer):
    # Client 2
    return (
        BillingPlan("Basic")
        if customer == "Unknown Customer"
        else customer.billing_plan
    )


def reset_billing_plan(customer):
    # Client 3
    if customer != "Unknown Customer":
        customer.billing_plan = BillingPlan("New")


def get_weeks_delinquent_in_last_year(customer):
    # Client 4
    return (
        0
        if customer == "Unknown Customer"
        else customer.payment_history.weeks_delinquent_in_last_year
    )
