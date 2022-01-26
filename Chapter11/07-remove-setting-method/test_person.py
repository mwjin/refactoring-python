from person import Person


def test_person_properties():
    """This test is somewhat redundant but exists for the example."""
    person = Person(1234)
    person.name = "Minwoo Jeong"

    assert person.id == 1234
    assert person.name == "Minwoo Jeong"
