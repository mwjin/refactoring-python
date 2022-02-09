import country_data
from shipping_rules import ShippingRules
from copy import deepcopy

_error_list = []


def get_order_shipping_cost(order_data):
    status = -23
    try:
        status = calculate_shipping_costs(order_data)
    except:
        pass

    if status < 0:
        _error_list.append({"order": order_data, "error_code": status})

    return status


def get_error_list():
    return deepcopy(_error_list)


def calculate_shipping_costs(order):
    shipping_rules = local_shipping_rules(order.country)
    if isinstance(shipping_rules, int) and shipping_rules < 0:
        return shipping_rules  # Transfer the error
    return 100


def local_shipping_rules(country):
    data = country_data.shipping_rules.get(country)
    if data:
        return ShippingRules(data)
    else:
        return -23
