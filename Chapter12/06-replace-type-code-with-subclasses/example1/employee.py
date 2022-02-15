class Employee:
    def __init__(self, name) -> None:
        self._name = name


class Engineer(Employee):
    def __str__(self) -> str:
        return f"{self._name} (engineer)"


class Manager(Employee):
    def __str__(self) -> str:
        return f"{self._name} (manager)"


class Salesperson(Employee):
    def __str__(self) -> str:
        return f"{self._name} (salesperson)"


def create_employee(name, type):
    if type == "engineer":
        return Engineer(name)
    if type == "manager":
        return Manager(name)
    if type == "salesperson":
        return Salesperson(name)
    raise ValueError(f'There is no "{type}" employee type.')
