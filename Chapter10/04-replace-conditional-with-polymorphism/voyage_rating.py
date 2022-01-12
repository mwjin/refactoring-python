class Rating:
    def __init__(self, voyage, history) -> None:
        self.voyage = voyage
        self.history = history

    @property
    def value(self):
        vpf = self.voyage_profit_factor
        vr = self.voyage_risk
        chr = self.captain_history_risk
        return "A" if vpf * 3 > (vr + chr * 2) else "B"

    @property
    def voyage_risk(self):
        result = 1
        if self.voyage.length > 4:
            result += 2
        if self.voyage.length > 8:
            result += self.voyage.length - 8
        if self.voyage.zone in ["China", "East India"]:
            result += 4
        return max(result, 0)

    @property
    def captain_history_risk(self):
        result = 1
        if len(self.history) < 5:
            result += 4
        result += len(list(filter(lambda v: v.profit < 0, self.history)))
        return max(result, 0)

    @property
    def voyage_profit_factor(self):
        result = 2
        if self.voyage.zone == "China":
            result += 1
        if self.voyage.zone == "East India":
            result += 1
        result += self.history_length_factor
        result += self.voyage_and_history_length_factor
        return result

    @property
    def voyage_and_history_length_factor(self):
        result = 0
        if self.voyage.length > 14:
            result -= 1
        return result

    @property
    def history_length_factor(self):
        return 1 if len(self.history) > 8 else 0

    def has_china_history(self):
        return any(filter(lambda v: v.zone == "China", self.history))


class ExperiencedChinaRating(Rating):
    @property
    def captain_history_risk(self):
        return max(super().captain_history_risk - 2, 0)

    @property
    def voyage_and_history_length_factor(self):
        result = 3
        if self.voyage.length > 12:
            result += 1
        if self.voyage.length > 18:
            result += 1
        return result

    @property
    def history_length_factor(self):
        return 1 if len(self.history) > 10 else 0


class VoyageObject:
    def __init__(self, zone, length) -> None:
        self.zone = zone
        self.length = length


class HistoryObject:
    def __init__(self, zone, profit) -> None:
        self.zone = zone
        self.profit = profit


def rating(voyage, history):
    return create_rating(voyage, history).value


def create_rating(voyage, history):
    if voyage.zone == "China" and any(
        filter(lambda v: v.zone == "China", history)
    ):
        return ExperiencedChinaRating(voyage, history)
    else:
        return Rating(voyage, history)
