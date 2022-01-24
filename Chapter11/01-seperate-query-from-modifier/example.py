def alert_for_miscreant(people):
    if find_miscreant(people):
        set_off_alarms()


def find_miscreant(people):
    for p in people:
        if p == "Joker":
            return "Joker"
        if p == "Saruman":
            return "Saruman"
    return ""


def set_off_alarms():
    print("A miscreant has been detected!")
