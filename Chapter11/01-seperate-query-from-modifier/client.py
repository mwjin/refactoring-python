from example import alert_for_miscreant


def client():
    found = alert_for_miscreant(["Minwoo Jeong", "Joker"])
    print(f"The miscreant's name is {found}")
