class Employee:
    def __init__(self, name) -> None:
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
        return Engineer(name)
    if type == "manager":
        return Manager(name)
    if type == "salesperson":
        return Salesperson(name)
    raise ValueError(f'There is no "{type}" employee type.')
