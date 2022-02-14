from employee import Employee


class Manager(Employee):
    def __init__(self, name, grade) -> None:
        super().__init__(name)
        self._grade = grade
        self.finish_construction()

    def finish_construction(self):
        if self.is_privileged:
            self.assign_car()

    @property
    def is_privileged(self):
        return self._grade > 4
