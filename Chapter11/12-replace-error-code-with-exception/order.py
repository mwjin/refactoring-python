class Order:
    def __init__(self, country) -> None:
        self._country = country

    @property
    def country(self):
        return self._country

    def __eq__(self, __o: object) -> bool:
        return self._country == __o._country
