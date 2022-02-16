from bird import create_bird


def test_bird():
    bird = create_bird({"type": "Other", "name": "Bird1", "plumage": "Wow"})
    assert bird.plumage == "Wow"
    assert bird.air_speed_velocity is None

    bird = create_bird({"type": "Other", "name": "Bird2"})
    assert bird.plumage == "Normal"


def test_european_swallow():
    bird = create_bird({"type": "EuropeanSwallow", "name": "Bird1"})
    assert bird.air_speed_velocity == 35


def test_african_swallow():
    bird = create_bird(
        {"type": "AfricanSwallow", "name": "Bird1", "number_of_coconuts": 2}
    )
    assert bird.air_speed_velocity == 36


def test_norwegian_blue_parrot():
    bird_data = {
        "type": "NorwegianBlueParrot",
        "name": "Bird1",
        "voltage": 150,
        "is_nailed": True,
    }
    bird = create_bird(bird_data)
    assert bird.plumage == "Scorched"
    assert bird.air_speed_velocity == 0

    bird_data["is_nailed"] = False
    bird = create_bird(bird_data)
    assert bird.air_speed_velocity == 25

    bird_data["voltage"] = 50
    bird = create_bird(bird_data)
    assert bird.plumage == "Beautiful"

    bird_data["plumage"] = "Wow"
    bird = create_bird(bird_data)
    assert bird.plumage == "Wow"
