from dummy import base_rate
from reading import acquire_reading, enrich_reading


def calculate_base_charge(reading):
    return base_rate(reading["month"], reading["year"]) * reading["quantity"]


raw_reading = acquire_reading()
reading = enrich_reading(raw_reading)
basic_charge_amount = calculate_base_charge(reading)
