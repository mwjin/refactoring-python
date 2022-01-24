from example import find_miscreant


def test_find_miscreant():
    assert find_miscreant(["Minwoo Jeong", "Joker", "Saruman"]) == "Joker"
    assert find_miscreant(["Minwoo Jeong", "Saruman", "Joker"]) == "Saruman"
    assert find_miscreant(["Minwoo Jeong", "Batman", "Spiderman"]) == ""

