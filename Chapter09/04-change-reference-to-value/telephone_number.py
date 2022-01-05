class TelephoneNumber:
    def __init__(self):
        self._area_code = 82
        self._number = 123456789

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, arg):
        self._area_code = arg

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, arg):
        self._number = arg
