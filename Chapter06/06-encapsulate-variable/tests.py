from default_owner import default_owner, set_default_owner


def test_get_default_owner():
    spaceship_owner = default_owner()
    assert spaceship_owner["first name"] == "Minwoo"
    assert spaceship_owner["last name"] == "Jeong"


def test_set_default_owner():
    set_default_owner({"first name": "Rebecca", "last name": "Parsons"})
    owner = default_owner()
    assert owner["first name"] == "Rebecca"
    assert owner["last name"] == "Parsons"


def test_change_field_of_default_owner():
    owner1 = default_owner()
    owner2 = default_owner()
    owner2["first name"] = "Minho"
    assert owner1["first name"] == "Minho"
