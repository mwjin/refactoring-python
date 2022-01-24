from example import alert_for_miscreant


def test_alert_for_miscreant():
    assert alert_for_miscreant(["Minwoo Jeong", "Joker", "Saruman"]) == "Joker"
    assert (
        alert_for_miscreant(["Minwoo Jeong", "Saruman", "Joker"]) == "Saruman"
    )
    assert alert_for_miscreant(["Minwoo Jeong", "Batman", "Spiderman"]) == ""

