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
            raise RuntimeError
        elif self._type == "African Swallow":
            raise RuntimeError
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


class EuropeanSwallow(Bird):
    @property
    def plumage(self):
        return "Normal"


class AfricanSwallow(Bird):
    @property
    def plumage(self):
        return "Exhausted" if self._number_of_coconuts > 2 else "Normal"


class NorwegianBlueParrot(Bird):
    pass


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
    return create_bird(bird).plumage


def air_speed_velocity(bird):
    return create_bird(bird).air_speed_velocity


def create_bird(bird):
    if bird.type == "European Swallow":
        return EuropeanSwallow(bird)
    elif bird.type == "African Swallow":
        return AfricanSwallow(bird)
    elif bird.type == "Norwegian Blue Parrot":
        return NorwegianBlueParrot(bird)
    else:
        return Bird(bird)
