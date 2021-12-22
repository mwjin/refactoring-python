from person import Person


def test_telephone_number():
    assert (
        Person("Minwoo Jeong", "+82", "0123456789").telephone_number
        == "(+82) 0123456789"
    )

