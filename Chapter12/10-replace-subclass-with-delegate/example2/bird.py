class Bird:
    def __init__(self, data) -> None:
        self._name = data.get("name")
        self._plumage = data.get("plumage")

    @property
    def name(self):
        return self._name

    @property
    def plumage(self):
        return self._plumage if self._plumage else "Normal"

    @property
    def air_speed_velocity(self):
        return None


class EuropeanSwallow(Bird):
    @property
    def air_speed_velocity(self):
        return 35


class EuropeanSwallowDelegate:
    pass


class AfricanSwallow(Bird):
    def __init__(self, data) -> None:
        super().__init__(data)
        self._number_of_coconuts = data.get("number_of_coconuts")

    @property
    def air_speed_velocity(self):
        return 40 - 2 * self._number_of_coconuts


class NorwegianBlueParrot(Bird):
    def __init__(self, data) -> None:
        super().__init__(data)
        self._voltage = data.get("voltage")
        self._is_nailed = data.get("is_nailed")

    @property
    def plumage(self):
        if self._voltage > 100:
            return "Scorched"
        else:
            return self._plumage if self._plumage else "Beautiful"

    @property
    def air_speed_velocity(self):
        return 0 if self._is_nailed else 10 + self._voltage / 10


def create_bird(data):
    if data.get("type") == "EuropeanSwallow":
        return EuropeanSwallow(data)
    elif data.get("type") == "AfricanSwallow":
        return AfricanSwallow(data)
    elif data.get("type") == "NorwegianBlueParrot":
        return NorwegianBlueParrot(data)
    return Bird(data)
