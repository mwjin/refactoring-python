class Person:
    def __init__(self, name, office_area_code, office_number):
        self._name = name
        self._office_area_code = office_area_code
        self._office_number = office_number

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def telephone_number(self):
        return f"({self.office_area_code}) {self.office_number}"

    @property
    def office_area_code(self):
        return self._office_area_code

    @office_area_code.setter
    def office_area_code(self, value):
        self._office_area_code = value

    @property
    def office_number(self):
        return self._office_number

    @office_number.setter
    def office_number(self, value):
        self._office_number = value
