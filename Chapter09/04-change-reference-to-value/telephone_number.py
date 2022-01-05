class TelephoneNumber:
    def __init__(self, area_code, number):
        self._area_code = area_code
        self._number = number

    @property
    def area_code(self):
        return self._area_code

    @property
    def number(self):
        return self._number
