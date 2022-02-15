class Employee:
    def __init__(self, name, type) -> None:
        self._name = name

    def __str__(self) -> str:
        return f"{self._name} ({self.type})"


class Engineer(Employee):
    @property
    def type(self):
        return "engineer"


class Manager(Employee):
    @property
    def type(self):
        return "manager"


class Salesperson(Employee):
    @property
    def type(self):
        return "salesperson"


def create_employee(name, type):
    if type == "engineer":
        return Engineer(name, type)
    if type == "manager":
        return Manager(name, type)
    if type == "salesperson":
        return Salesperson(name, type)
    raise ValueError(f'There is no "{type}" employee type.')
