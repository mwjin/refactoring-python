from bird import BirdObject, plumage, air_speed_velocity


def get_bird_object(type):
    return BirdObject("test", type)


def test_plumage():
    european = get_bird_object("European Swallow")
    assert plumage(european) == "Normal"

    african = get_bird_object("African Swallow")
    assert plumage(african) == "Normal"
    african.number_of_coconuts = 3
    assert plumage(african) == "Exhausted"

    norwegian = get_bird_object("Norwegian Blue Parrot")
    assert plumage(norwegian) == "Pretty"
    norwegian.voltage = 101
    assert plumage(norwegian) == "Scorched"

    other = get_bird_object("Eagle")
    assert plumage(other) == "Unknown"


def test_air_speed_velocity():
    european = get_bird_object("European Swallow")
    assert air_speed_velocity(european) == 35

    african = get_bird_object("African Swallow")
    assert air_speed_velocity(african) == 40
    african.number_of_coconuts = 3
    assert air_speed_velocity(african) == 34

    norwegian = get_bird_object("Norwegian Blue Parrot")
    assert air_speed_velocity(norwegian) == 10
    norwegian.voltage = 101
    assert air_speed_velocity(norwegian) == 20.1
    norwegian.is_nailed = True
    assert air_speed_velocity(norwegian) == 0

    other = get_bird_object("Eagle")
    assert air_speed_velocity(other) is None
