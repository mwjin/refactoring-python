from bird import BirdObject, create_bird


def get_bird(type):
    return create_bird(BirdObject("test", type))


def test_plumage():
    european = get_bird("European Swallow")
    assert european.plumage == "Normal"

    african = get_bird("African Swallow")
    assert african.plumage == "Normal"
    african.number_of_coconuts = 3
    assert african.plumage == "Exhausted"

    norwegian = get_bird("Norwegian Blue Parrot")
    assert norwegian.plumage == "Pretty"
    norwegian.voltage = 101
    assert norwegian.plumage == "Scorched"

    other = get_bird("Eagle")
    assert other.plumage == "Unknown"


def test_air_speed_velocity():
    european = get_bird("European Swallow")
    assert european.air_speed_velocity == 35

    african = get_bird("African Swallow")
    assert african.air_speed_velocity == 40
    african.number_of_coconuts = 3
    assert african.air_speed_velocity == 34

    norwegian = get_bird("Norwegian Blue Parrot")
    assert norwegian.air_speed_velocity == 10
    norwegian.voltage = 101
    assert norwegian.air_speed_velocity == 20.1
    norwegian.is_nailed = True
    assert norwegian.air_speed_velocity == 0

    other = get_bird("Eagle")
    assert other.air_speed_velocity is None
