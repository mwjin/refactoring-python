def check_for_miscreants(people):
    return any(map(lambda p: p in ["Joker", "Saruman"], people))


def send_alert():
    print("There is a miscreant!")
