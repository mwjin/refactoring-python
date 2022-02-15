class Person:
    def __init__(self, name, gender_code) -> None:
        self._name = name
        self._gender_code = gender_code

    @property
    def name(self):
        return self._name

    @property
    def gender_code(self):
        return self._gender_code

    @property
    def is_male(self):
        return self._gender_code == "M"


def create_person(record):
    if record["gender"] == "M":
        return Person(record["name"], "M")
    if record["gender"] == "F":
        return Person(record["name"], "F")
    return Person(record["name"], "X")
