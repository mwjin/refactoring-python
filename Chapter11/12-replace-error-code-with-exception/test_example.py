from example import get_order_shipping_cost, get_error_list
from order import Order


def test_get_order_shipping_cost():
    assert get_order_shipping_cost(Order("KO")) == 100
    assert get_order_shipping_cost(Order("JP")) == 100
    assert get_order_shipping_cost(Order("CN")) == 100


def test_get_order_shipping_cost_with_err():
    assert get_order_shipping_cost(Order("USA")) == -23
    error = get_error_list()[-1]
    assert error["order"] == Order("USA")
    assert error["error_code"] == -23

