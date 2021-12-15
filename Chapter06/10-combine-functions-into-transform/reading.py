from copy import deepcopy

_reading = {"customer": "Minwoo", "quantity": 10, "month": 5, "year": 2017}


def acquire_reading():
    return dict(_reading)


def enrich_reading(original):
    result = deepcopy(original)
    return result
