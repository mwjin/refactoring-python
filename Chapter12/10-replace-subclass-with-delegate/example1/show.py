class Show:
    def __init__(self, name, price) -> None:
        self._name = name
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    def set_talkback(self):
        self.talkback = True
