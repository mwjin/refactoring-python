from reading import acquire_reading, enrich_reading

raw_reading = acquire_reading()
reading = enrich_reading(raw_reading)
base_charge = reading["base charge"]
