class Person:
    def __init__(self, age, salary) -> None:
        self._age = age
        self._salary = salary

    @property
    def age(self):
        return self._age

    @property
    def salary(self):
        return self._salary
