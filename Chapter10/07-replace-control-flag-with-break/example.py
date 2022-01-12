def check_for_miscreants(people):
    found = False
    for p in people:
        if not found:
            if p == "Joker":
                send_alert()
                return True
            if p == "Saruman":
                send_alert()
                return True
    return found


def send_alert():
    print("There is a miscreant!")
