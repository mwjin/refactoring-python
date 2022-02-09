from copy import deepcopy

import country_data
from error import OrderProcessingError
from shipping_rules import ShippingRules

_error_list = []


def get_order_shipping_cost(order_data):
    try:
        return calculate_shipping_costs(order_data)
    except Exception as e:
        if isinstance(e, OrderProcessingError):
            _error_list.append({"order": order_data, "error_code": e.code})
            return e.code
        else:
            raise e


def get_error_list():
    return deepcopy(_error_list)


def calculate_shipping_costs(order):
    shipping_rules = local_shipping_rules(order.country)
    return 100


def local_shipping_rules(country):
    data = country_data.shipping_rules.get(country)
    if data:
        return ShippingRules(data)
    else:
        raise OrderProcessingError(-23)
