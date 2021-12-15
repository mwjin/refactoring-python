from dummy import base_rate, tax_threshold
from reading import acquire_reading

reading = acquire_reading()
base = base_rate(reading["month"], reading["year"]) * reading["quantity"]
taxable_charge = max(0, base - tax_threshold(reading["year"]))

