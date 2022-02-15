class EmployeeType:
    def __init__(self, value) -> None:
        self._value = value

    def __str__(self) -> str:
        return self._value


class Engineer(EmployeeType):
    def __str__(self) -> str:
        return "engineer"


class Employee:
    def __init__(self, name, type) -> None:
        self._validate_type(type)
        self._name = name
        self.type = type

    def _validate_type(self, type):
        if type not in ["engineer", "manager", "salesperson"]:
            raise ValueError(f'There is no "{type}" employee type.')

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
            return Engineer(value)
        return EmployeeType(value)

    @property
    def capitalized_type(self):
        return self.type_string.capitalize()

    def __str__(self) -> str:
        return f"{self._name} ({self.capitalized_type})"
