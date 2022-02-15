class Person:
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def gender_code(self):
        return "X"


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
        person = Male(record["name"])
    elif record["gender"] == "F":
        person = Female(record["name"])
    else:
        person = Person(record["name"])
    return person
