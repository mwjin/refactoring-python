from copy import deepcopy

from dummy import base_rate, tax_threshold

_reading = {"customer": "Minwoo", "quantity": 10, "month": 5, "year": 2017}


def acquire_reading():
    return dict(_reading)


def enrich_reading(original):
    result = deepcopy(original)
    result["base charge"] = calculate_base_charge(result)
    result["taxable charge"] = max(
        0, result["base charge"] - tax_threshold(result["year"])
    )
    return result


def calculate_base_charge(reading):
    return base_rate(reading["month"], reading["year"]) * reading["quantity"]
