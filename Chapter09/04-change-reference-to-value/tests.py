from person import Person
from telephone_number import TelephoneNumber


def test_office_area_code():
    person = Person()
    assert person.office_area_code == 82
    person.office_area_code = 100
    assert person.office_area_code == 100


def test_office_number():
    person = Person()
    assert person.office_number == 123456789
    person.office_number = 987654321
    assert person.office_number == 987654321


def test_telephone_eq():
    assert TelephoneNumber(82, 123456789) == TelephoneNumber(82, 123456789)
