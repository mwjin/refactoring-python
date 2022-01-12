class Bird:
    def __init__(self, bird_object) -> None:
        self._name = bird_object.name
        self._type = bird_object.type
        self._number_of_coconuts = bird_object.number_of_coconuts
        self._voltage = bird_object.voltage
        self._is_nailed = bird_object.is_nailed

    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type

    @property
    def number_of_coconuts(self):
        return self._number_of_coconuts

    @number_of_coconuts.setter
    def number_of_coconuts(self, arg):
        self._number_of_coconuts = arg

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, arg):
        self._voltage = arg

    @property
    def is_nailed(self):
        return self._is_nailed

    @is_nailed.setter
    def is_nailed(self, arg):
        self._is_nailed = arg

    @property
    def plumage(self):
        return "Unknown"

    @property
    def air_speed_velocity(self):
        return None


class EuropeanSwallow(Bird):
    @property
    def plumage(self):
        return "Normal"

    @property
    def air_speed_velocity(self):
        return 35


class AfricanSwallow(Bird):
    @property
    def plumage(self):
        return "Exhausted" if self._number_of_coconuts > 2 else "Normal"

    @property
    def air_speed_velocity(self):
        return 40 - 2 * self._number_of_coconuts


class NorwegianBlueParrot(Bird):
    @property
    def plumage(self):
        return "Scorched" if self._voltage > 100 else "Pretty"

    @property
    def air_speed_velocity(self):
        return 0 if self._is_nailed else 10 + self._voltage / 10


class BirdObject:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_of_coconuts = 0
        self.voltage = 0
        self.is_nailed = False


def plumages(birds):
    return map(
        lambda b: [b.name, b.plumage], map(lambda b: create_bird(b), birds)
    )


def speeds(birds):
    return map(
        lambda b: [b.name, b.air_speed_velocity],
        map(lambda b: create_bird(b), birds),
    )


def create_bird(bird):
    if bird.type == "European Swallow":
        return EuropeanSwallow(bird)
    elif bird.type == "African Swallow":
        return AfricanSwallow(bird)
    elif bird.type == "Norwegian Blue Parrot":
        return NorwegianBlueParrot(bird)
    else:
        return Bird(bird)
