from department import Department
from person import Person


def test_get_manager():
    person = Person("Minwoo Jeong", Department("A", "B"))
    assert person.department.manager == "B"
