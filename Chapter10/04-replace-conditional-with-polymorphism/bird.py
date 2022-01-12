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
    if bird.type == "European Swallow":
        return "Normal"
    elif bird.type == "African Swallow":
        return "Exhausted" if bird.number_of_coconuts > 2 else "Normal"
    elif bird.type == "Norwegian Blue Parrot":
        return "Scorched" if bird.voltage > 100 else "Pretty"
    else:
        return "Unknown"


def air_speed_velocity(bird):
    if bird.type == "European Swallow":
        return 35
    elif bird.type == "African Swallow":
        return 40 - 2 * bird.number_of_coconuts
    elif bird.type == "Norwegian Blue Parrot":
        return 0 if bird.is_nailed else 10 + bird.voltage / 10
    else:
        return None
