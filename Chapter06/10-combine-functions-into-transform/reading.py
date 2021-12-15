from copy import deepcopy

from dummy import base_rate

_reading = {"customer": "Minwoo", "quantity": 10, "month": 5, "year": 2017}


def acquire_reading():
    return dict(_reading)


def enrich_reading(original):
    result = deepcopy(original)
    result["base charge"] = calculate_base_charge(result)
    return result


def calculate_base_charge(reading):
    return base_rate(reading["month"], reading["year"]) * reading["quantity"]
