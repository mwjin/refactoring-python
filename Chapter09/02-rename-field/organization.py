class Organization:
    def __init__(self, data):
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
    def country(self, new_country):
        self._country = new_country


organization = Organization({"name": "Samsung", "country": "KO"})
