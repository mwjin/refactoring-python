from default_owner import default_owner, get_default_owner


def test_get_default_owner():
    spaceship_owner = get_default_owner()
    assert spaceship_owner["first name"] == "Minwoo"
    assert spaceship_owner["last name"] == "Jeong"


def test_set_default_owner():
    global default_owner
    default_owner = {"first name": "Rebecca", "last name": "Parsons"}
    assert default_owner["first name"] == "Rebecca"
    assert default_owner["last name"]
