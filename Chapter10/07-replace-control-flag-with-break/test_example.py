from example import check_for_miscreants


def test_check_for_miscreants():
    people = ["Minwoo Jeong", "Joker", "Saruman"]
    assert check_for_miscreants(people)
    people.remove("Saruman")
    assert check_for_miscreants(people)
    people.remove("Joker")
    assert not check_for_miscreants(people)
