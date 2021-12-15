from dummy import base_rate, tax_threshold
from reading import acquire_reading, Reading

reading_data = acquire_reading()
reading = Reading(reading_data)
taxable_charge = reading.taxable_charge
