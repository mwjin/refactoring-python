from customer import UnknownCustomer


class Site:
    def __init__(self, customer):
        self._customer = customer

    @property
    def customer(self):
        return (
            UnknownCustomer()
            if self._customer == "Unknown Customer"
            else self._customer
        )
