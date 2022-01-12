def check_for_miscreants(people):
    for p in people:
        if p == "Joker":
            send_alert()
            return True
        if p == "Saruman":
            send_alert()
            return True
    return False


def send_alert():
    print("There is a miscreant!")
