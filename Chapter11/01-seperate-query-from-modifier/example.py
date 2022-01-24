def alert_for_miscreant(people):
    for p in people:
        if p == "Joker":
            set_off_alarms()
            return
        if p == "Saruman":
            set_off_alarms()
            return
    return


def find_miscreant(people):
    for p in people:
        if p == "Joker":
            return "Joker"
        if p == "Saruman":
            return "Saruman"
    return ""


def set_off_alarms():
    print("A miscreant has been detected!")
