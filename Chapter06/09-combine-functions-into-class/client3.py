from dummy import base_rate
from reading import Reading, acquire_reading


reading_data = acquire_reading()
reading = Reading(reading_data)
basic_charge_amount = reading.base_charge
