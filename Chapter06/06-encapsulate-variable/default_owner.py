_default_owner = {"first name": "Minwoo", "last name": "Jeong"}


def default_owner():
    return dict(_default_owner)


def set_default_owner(owner):
    global _default_owner
    _default_owner = owner
