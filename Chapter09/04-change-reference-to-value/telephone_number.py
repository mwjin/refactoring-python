class TelephoneNumber:
    def __init__(self, area_code, number):
        self._area_code = area_code
        self._number = number

    def __eq__(self, o):
        return (self.area_code == o.area_code) and (self.number == o.number)

    @property
    def area_code(self):
        return self._area_code

    @property
    def number(self):
        return self._number
