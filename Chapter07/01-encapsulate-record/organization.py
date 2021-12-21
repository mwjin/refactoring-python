class Organization:
    def __init__(self, data) -> None:
        self._data = data

    @property
    def name(self):
        return self._data["name"]

    @name.setter
    def name(self, new_name):
        self._data["name"] = new_name


organization = Organization({"name": "Apple", "country": "KO"})


def get_organization():
    global organization
    return organization
