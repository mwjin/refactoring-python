from dummy import base_rate, tax_threshold
from reading import acquire_reading, Reading


def taxable_charge_fn(reading):
    return max(0, reading.base_charge - tax_threshold(reading.year))


reading_data = acquire_reading()
reading = Reading(reading_data)
taxable_charge = taxable_charge_fn(reading)
