class Employee:
    def __init__(self, name, type_code) -> None:
        self._name = name
        self._type_code = type_code

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return Employee.legal_type_codes()[self._type_code]

    @staticmethod
    def legal_type_codes():
        return {"E": "Engineer", "M": "Manager", "S": "Salesperson"}


def create_employee(name, type_code):
    return Employee(name, type_code)


def create_engineer(name):
    return Employee(name, "E")


def create_manager(name):
    return Employee(name, "M")


def create_salesperson(name):
    return Employee(name, "S")
