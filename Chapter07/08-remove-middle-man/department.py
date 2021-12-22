class Department:
    def __init__(self, charge_code, manager):
        self._charge_code = charge_code
        self._manager = manager

    @property
    def charge_code(self):
        return self._charge_code

    @charge_code.setter
    def charge_code(self, value):
        self._charge_code = value

    @property
    def manager(self):
        return self._manager

    @manager.setter
    def manager(self, value):
        self._manager = value
