class Organization:
    def __init__(self, data):
        self._title = data["title"]
        self._country = data["country"]

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_name):
        self._title = new_name

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, new_country):
        self._country = new_country


organization = Organization({"title": "Samsung", "country": "KO"})
