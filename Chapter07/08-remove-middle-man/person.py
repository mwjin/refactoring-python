class Person:
    def __init__(self, name, department):
        self._name = name
        self._department = department

    @property
    def department(self):
        return self._department

    @property
    def name(self):
        return self._name

    @property
    def manager(self):
        return self._department.manager
