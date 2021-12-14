class Driver:
    def __init__(self) -> None:
        self._number_of_late_deliveries = 0

    @property
    def number_of_late_deliveries(self):
        return self._number_of_late_deliveries

    def do_late_delivery(self):
        self._number_of_late_deliveries += 1
