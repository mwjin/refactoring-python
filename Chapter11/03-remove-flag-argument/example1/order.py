from datetime import timedelta


class Order:
    def __init__(self, delivery_state, placed_on):
        self._delivery_state = delivery_state
        self._placed_on = placed_on

    @property
    def delivery_state(self):
        return self._delivery_state

    @property
    def placed_on(self):
        return self._placed_on

    def add_days_to_placed_on(self, days):
        return self._placed_on + timedelta(days=days)
