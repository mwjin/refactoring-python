class Organization:
    def __init__(self, data) -> None:
        self._name = data["name"]
        self._country = data["country"]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country_code):
        self._country = country_code


organization = Organization({"name": "Apple", "country": "KO"})


def get_organization():
    global organization
    return organization
