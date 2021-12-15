from dummy import tax_threshold
from reading import acquire_reading, enrich_reading

raw_reading = acquire_reading()
reading = enrich_reading(raw_reading)
taxable_charge = reading["taxable charge"]
