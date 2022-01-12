class Bird:
    def __init__(self, bird_object) -> None:
        self._name = bird_object.name
        self._type = bird_object.type
        self._number_of_coconuts = bird_object.number_of_coconuts
        self._voltage = bird_object.voltage
        self._is_nailed = bird_object.is_nailed

    @property
    def plumage(self):
        if self._type == "European Swallow":
            return "Normal"
        elif self._type == "African Swallow":
            return "Exhausted" if self._number_of_coconuts > 2 else "Normal"
        elif self._type == "Norwegian Blue Parrot":
            return "Scorched" if self._voltage > 100 else "Pretty"
        else:
            return "Unknown"

    @property
    def air_speed_velocity(self):
        if self._type == "European Swallow":
            return 35
        elif self._type == "African Swallow":
            return 40 - 2 * self._number_of_coconuts
        elif self._type == "Norwegian Blue Parrot":
            return 0 if self._is_nailed else 10 + self._voltage / 10
        else:
            return None


class BirdObject:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_of_coconuts = 0
        self.voltage = 0
        self.is_nailed = False


def plumages(birds):
    return map(lambda b: [b.name, plumage(b)], birds)


def speeds(birds):
    return map(lambda b: [b.name, air_speed_velocity(b)], birds)


def plumage(bird):
    return Bird(bird).plumage


def air_speed_velocity(bird):
    return Bird(bird).air_speed_velocity
