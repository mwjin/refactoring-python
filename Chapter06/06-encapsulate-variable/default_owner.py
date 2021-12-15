default_owner = {"first name": "Minwoo", "last name": "Jeong"}


def get_default_owner():
    return default_owner


def set_default_owner(owner):
    global default_owner
    default_owner = owner
