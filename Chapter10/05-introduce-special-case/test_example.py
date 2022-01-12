import pytest

from customer import BillingPlan, Customer, PaymentHistory
from example import (
    get_billing_plan,
    get_customer_name,
    get_weeks_delinquent_in_last_year,
    reset_billing_plan,
)
from my_site import Site


@pytest.fixture
def customer():
    return Customer("Minwoo Jeong", BillingPlan("Test"), PaymentHistory(24))


@pytest.fixture
def unknown_customer():
    return "Unknown Customer"


def test_get_customer_name(customer, unknown_customer):
    assert get_customer_name(Site(customer)) == "Minwoo Jeong"
    assert get_customer_name(Site(unknown_customer)) == "Resident"


def test_get_billing_plan(customer, unknown_customer):
    assert get_billing_plan(customer).name == "Test"
    assert get_billing_plan(unknown_customer).name == "Basic"


def test_reset_billing_plan(customer, unknown_customer):
    reset_billing_plan(customer)
    assert customer.billing_plan.name == "New"
    reset_billing_plan(unknown_customer)
    assert True


def test_get_weeks_delinquent_in_last_year(customer, unknown_customer):
    assert get_weeks_delinquent_in_last_year(customer) == 24
    assert get_weeks_delinquent_in_last_year(unknown_customer) == 0
