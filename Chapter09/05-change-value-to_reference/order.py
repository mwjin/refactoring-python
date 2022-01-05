from customer import Customer


class Order:
    def __init__(self, data):
        self._number = data["number"]
        self._customer = Customer.register_customer(data["customer"])

    @property
    def customer(self):
        return self._customer
