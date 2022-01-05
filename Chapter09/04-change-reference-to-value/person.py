from telephone_number import TelephoneNumber


class Person:
    def __init__(self):
        self._telephone_number = TelephoneNumber(82, 123456789)

    @property
    def office_area_code(self):
        return self._telephone_number.area_code

    @office_area_code.setter
    def office_area_code(self, arg):
        self._telephone_number = TelephoneNumber(arg, self.office_number)

    @property
    def office_number(self):
        return self._telephone_number.number

    @office_number.setter
    def office_number(self, arg):
        self._telephone_number = TelephoneNumber(self.office_area_code, arg)
