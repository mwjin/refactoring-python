from reading import Reading, acquire_reading

reading_data = acquire_reading()
reading = Reading(reading_data)
base_charge = reading.base_charge
