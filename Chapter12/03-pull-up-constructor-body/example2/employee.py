class Employee:
    def __init__(self, name) -> None:
        self._name = name

    def finish_construction(self):
        if self.is_privileged:
            self.assign_car()

    @property
    def is_privileged(self):
        pass

    def assign_car(self):
        pass
