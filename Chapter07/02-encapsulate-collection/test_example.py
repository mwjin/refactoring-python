import pytest

from course import Course
from person import Person


@pytest.fixture
def person():
    _person = Person("Minwoo Jeong")
    _person.courses = [Course("Math", False), Course("Advanced Math", True)]
    return _person


def test_add_course_directly(person):
    old_courses = list(person.courses)
    person.courses.append(Course("CS", False))
    assert person.courses == old_courses  # immutable


def test_remove_course_directly(person):
    old_courses = list(person.courses)
    person.courses.pop()
    assert person.courses == old_courses  # immutable


def test_add_course_via_method(person):
    person.add_course(Course("Machine Learning", True))
    last_course = person.courses.pop()
    assert last_course == Course("Machine Learning", True)


def test_remove_course_via_method(person):
    old_course_set = set(person.courses)
    person.remove_course(Course("Math", False))
    diff = old_course_set - set(person.courses)
    assert len(diff) == 1
    assert list(diff)[0] == Course("Math", False)


def test_remove_course_not_exists(person):
    with pytest.raises(ValueError):
        person.remove_course(Course("Science", False))
