class Person:
    def __init__(self, name, office_area_code, office_number):
        self._name = name
        self._telephone_number = TelephoneNumber(
            office_area_code, office_number
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def telephone_number(self):
        return self._telephone_number.telephone_number

    @property
    def office_area_code(self):
        return self._telephone_number.office_area_code

    @office_area_code.setter
    def office_area_code(self, value):
        self._telephone_number.office_area_code = value

    @property
    def office_number(self):
        return self._telephone_number.office_number

    @office_number.setter
    def office_number(self, value):
        self._telephone_number.office_number = value


class TelephoneNumber:
    def __init__(self, area_code, number):
        self._area_code = area_code
        self._number = number

    @property
    def area_code(self):
        return self._area_code

    @area_code.setter
    def area_code(self, value):
        self._area_code = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def telephone_number(self):
        return f"({self.area_code}) {self.number}"

