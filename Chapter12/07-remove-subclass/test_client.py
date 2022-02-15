import pytest

from client import get_number_of_males
from person import Female, Male, Person


@pytest.fixture
def data():
    return [
        {"name": "Person1", "gender": "M"},
        {"name": "Person2", "gender": "M"},
        {"name": "Person3", "gender": "F"},
        {"name": "Person4", "gender": "F"},
        {"name": "Person5", "gender": "M"},
        {"name": "Person6", "gender": "X"},
    ]


@pytest.fixture
def people(data):
    people = []
    for record in data:
        if record["gender"] == "M":
            person = Male(record["name"])
        elif record["gender"] == "F":
            person = Female(record["name"])
        else:
            person = Person(record["name"])
        people.append(person)
    return people


def test_get_number_of_males(people):
    assert get_number_of_males(people) == 3
