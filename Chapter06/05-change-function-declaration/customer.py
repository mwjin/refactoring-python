class Customer:
    def __init__(self, address):
        self._address = address

    @property
    def address(self):
        return self._address
