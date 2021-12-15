from reading import acquire_reading, enrich_reading


raw_reading = acquire_reading()
reading = enrich_reading(raw_reading)
basic_charge_amount = reading["base charge"]
