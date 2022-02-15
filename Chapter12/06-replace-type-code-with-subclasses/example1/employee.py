class Employee:
    def __init__(self, name) -> None:
        self._name = name


class Engineer(Employee):
    @property
    def type(self):
        return "engineer"

    def __str__(self) -> str:
        return f"{self._name} ({self.type})"


class Manager(Employee):
    @property
    def type(self):
        return "manager"

    def __str__(self) -> str:
        return f"{self._name} ({self.type})"


class Salesperson(Employee):
    @property
    def type(self):
        return "salesperson"

    def __str__(self) -> str:
        return f"{self._name} ({self.type})"


def create_employee(name, type):
    if type == "engineer":
        return Engineer(name)
    if type == "manager":
        return Manager(name)
    if type == "salesperson":
        return Salesperson(name)
    raise ValueError(f'There is no "{type}" employee type.')
