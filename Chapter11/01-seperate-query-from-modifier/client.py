from example import find_miscreant, set_off_alarms


def client():
    found = find_miscreant(["Minwoo Jeong", "Joker"])
    set_off_alarms()
    print(f"The miscreant's name is {found}")
