from party import Party


class Department(Party):
    def __init__(self, name, staff) -> None:
        super().__init__(name)
        self._staff = staff

    @property
    def name(self):
        return self._name

    @property
    def staff(self):
        return self._staff
