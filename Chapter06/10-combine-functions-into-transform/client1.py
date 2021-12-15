from reading import acquire_reading
from dummy import base_rate

reading = acquire_reading()
base_charge = base_rate(reading["month"], reading["year"]) * reading["quantity"]
