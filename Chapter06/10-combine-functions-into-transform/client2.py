from dummy import tax_threshold
from reading import acquire_reading, enrich_reading

raw_reading = acquire_reading()
reading = enrich_reading(raw_reading)
base = reading["base charge"]
taxable_charge = max(0, base - tax_threshold(reading["year"]))
