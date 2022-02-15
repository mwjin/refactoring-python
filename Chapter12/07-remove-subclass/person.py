class Person:
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def gender_code(self):
        return "X"

    @property
    def is_male(self):
        return isinstance(self, Male)


class Male(Person):
    @property
    def gender_code(self):
        return "M"


class Female(Person):
    @property
    def gender_code(self):
        return "F"


def create_person(record):
    if record["gender"] == "M":
        return Male(record["name"])
    if record["gender"] == "F":
        return Female(record["name"])
    return Person(record["name"])
