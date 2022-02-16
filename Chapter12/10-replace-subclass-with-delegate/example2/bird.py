class Bird:
    def __init__(self, data) -> None:
        self._name = data.get("name")
        self._plumage = data.get("plumage")
        self._species_delegate = self.select_species_delegate(data)

    def select_species_delegate(self, data):
        if data.get("type") == "EuropeanSwallow":
            return EuropeanSwallowDelegate()
        return None

    @property
    def has_species_delegate(self):
        return self._species_delegate is not None

    @property
    def name(self):
        return self._name

    @property
    def plumage(self):
        return self._plumage if self._plumage else "Normal"

    @property
    def air_speed_velocity(self):
        if self.has_species_delegate:
            return self._species_delegate.air_speed_velocity
        return None


class EuropeanSwallowDelegate:
    @property
    def air_speed_velocity(self):
        return 35


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
    if data.get("type") == "AfricanSwallow":
        return AfricanSwallow(data)
    elif data.get("type") == "NorwegianBlueParrot":
        return NorwegianBlueParrot(data)
    return Bird(data)
