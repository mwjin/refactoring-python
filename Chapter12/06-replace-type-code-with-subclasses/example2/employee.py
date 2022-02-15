class EmployeeType:
    pass


class Engineer(EmployeeType):
    def __str__(self) -> str:
        return "engineer"


class Manager(EmployeeType):
    def __str__(self) -> str:
        return "manager"


class Salesperson(EmployeeType):
    def __str__(self) -> str:
        return "salesperson"


class Employee:
    def __init__(self, name, type) -> None:
        self._name = name
        self.type = type

    @property
    def type_string(self):
        return str(self._type)

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = Employee.create_employee_type(value)

    @staticmethod
    def create_employee_type(value):
        if value == "engineer":
            return Engineer()
        if value == "manager":
            return Manager()
        if value == "salesperson":
            return Salesperson()
        raise ValueError(f'There is no "{value}" employee type.')

    @property
    def capitalized_type(self):
        return self.type_string.capitalize()

    def __str__(self) -> str:
        return f"{self._name} ({self.capitalized_type})"
