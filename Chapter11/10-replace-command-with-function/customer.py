class Customer:
    def __init__(self, base_rate) -> None:
        self._base_rate = base_rate

    @property
    def base_rate(self):
        return self._base_rate
