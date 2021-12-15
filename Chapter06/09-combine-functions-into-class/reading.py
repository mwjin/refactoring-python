_reading = {"customer": "Minwoo", "quantity": 10, "month": 5, "year": 2017}


class Reading:
    def __init__(self, data):
        self._customer = data["customer"]
        self._quantity = data["quantity"]
        self._month = data["month"]
        self._year = data["year"]

    @property
    def customer(self):
        return self._customer

    @property
    def quantity(self):
        return self._quantity

    @property
    def month(self):
        return self._month

    @property
    def year(self):
        return self._year


def acquire_reading():
    return dict(_reading)
