class VoyageObject:
    def __init__(self, zone, length) -> None:
        self.zone = zone
        self.length = length


class HistoryObject:
    def __init__(self, zone, profit) -> None:
        self.zone = zone
        self.profit = profit


def rating(voyage, history):
    vpf = voyage_profit_factor(voyage, history)
    vr = voyage_risk(voyage)
    chr = captain_history_risk(voyage, history)
    return "A" if vpf * 3 > (vr + chr * 2) else "B"


def voyage_risk(voyage):
    result = 1
    if voyage.length > 4:
        result += 2
    if voyage.length > 8:
        result += voyage.length - 8
    if voyage.zone in ["China", "East India"]:
        result += 4
    return max(result, 0)


def captain_history_risk(voyage, history):
    result = 1
    if len(history) < 5:
        result += 4
    result += len(list(filter(lambda v: v.profit < 0, history)))
    if voyage.zone == "China" and has_china(history):
        result -= 2
    return max(result, 0)


def has_china(history):
    return any(filter(lambda v: v.zone == "China", history))


def voyage_profit_factor(voyage, history):
    result = 2
    if voyage.zone == "China":
        result += 1
    if voyage.zone == "East India":
        result += 1
    if voyage.zone == "China" and has_china(history):
        result += 3
        if len(history) > 10:
            result += 1
        if voyage.length > 12:
            result += 1
        if voyage.length > 18:
            result += 1
    else:
        if len(history) > 8:
            result += 1
        if voyage.length > 14:
            result -= 1
    return result
