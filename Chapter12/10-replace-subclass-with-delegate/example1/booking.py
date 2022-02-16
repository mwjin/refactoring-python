class Booking:
    def __init__(self, show, date) -> None:
        self._show = show
        self._date = date

    @property
    def is_peak_day(self):
        if self._date.weekday() >= 5:  # weekend
            return True
        return False

    @property
    def has_talkback(self):
        return hasattr(self._show, "talkback") and not self.is_peak_day

    @property
    def base_price(self):
        result = self._show.price
        if self.is_peak_day:
            result += round(result * 0.15)
        return result


class PremiumBooking(Booking):
    def __init__(self, show, date, extras) -> None:
        super().__init__(show, date)
        self._extras = extras

    @property
    def has_talkback(self):
        return hasattr(self._show, "talkback")

    @property
    def base_price(self):
        return round(super().base_price + self._extras.premium_fee)

    @property
    def has_dinner(self):
        return hasattr(self._extras, "dinner")
