class Person:
    def __init__(self, name) -> None:
        self._name = name
        self._courses = []

    @property
    def name(self):
        return self._name

    @property
    def courses(self):
        return self._courses

    @courses.setter
    def courses(self, new_courses):
        self._courses = new_courses
