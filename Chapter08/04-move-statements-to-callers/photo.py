class Photo:
    def __init__(self, title, location, date) -> None:
        self._title = title
        self._location = location
        self._date = date

    @property
    def title(self):
        return self._title

    @property
    def location(self):
        return self._location

    @property
    def date(self):
        return self._date

