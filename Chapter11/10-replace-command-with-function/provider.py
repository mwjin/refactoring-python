class Provider:
    def __init__(self, connection_charge) -> None:
        self._connection_charge = connection_charge

    @property
    def connection_charge(self):
        return self._connection_charge
