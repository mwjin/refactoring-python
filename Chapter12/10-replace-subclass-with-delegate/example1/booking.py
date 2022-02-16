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
    def is_premium(self):
        return hasattr(self, "_premium_delegate")

    @property
    def has_talkback(self):
        if self.is_premium:
            return self._premium_delegate.has_talkback
        return hasattr(self._show, "talkback") and not self.is_peak_day

    @property
    def base_price(self):
        result = self._show.price
        if self.is_peak_day:
            result += round(result * 0.15)
        if self.is_premium:
            return self._premium_delegate.extend_base_price(result)
        return result

    def _be_premium(self, extras):
        self._premium_delegate = PremiumBookingDelegate(self, extras)


class PremiumBooking(Booking):
    def __init__(self, show, date, extras) -> None:
        super().__init__(show, date)
        self._extras = extras

    @property
    def has_dinner(self):
        return hasattr(self._extras, "dinner")


class PremiumBookingDelegate:
    def __init__(self, host_booking, extras) -> None:
        self._host = host_booking
        self._extras = extras

    @property
    def has_talkback(self):
        return hasattr(self._host._show, "talkback")

    def extend_base_price(self, base_price):
        return round(base_price + self._extras.premium_fee)


def create_booking(show, date):
    return Booking(show, date)


def create_premium_booking(show, date, extras):
    result = PremiumBooking(show, date, extras)
    result._be_premium(extras)
    return result
