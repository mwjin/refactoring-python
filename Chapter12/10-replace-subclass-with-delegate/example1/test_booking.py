from datetime import datetime

import pytest

from booking import Booking, PremiumBooking
from extras import Extras
from show import Show


@pytest.fixture
def weekday():
    return datetime.strptime("16 02 2022", "%d %m %Y")


@pytest.fixture
def weekend():
    return datetime.strptime("19 02 2022", "%d %m %Y")


@pytest.fixture
def show():
    return Show("Show!", 1000)


@pytest.fixture
def extras():
    return Extras(200)


def test_booking_is_peak_day(show, weekday, weekend):
    assert not Booking(show, weekday).is_peak_day
    assert Booking(show, weekend).is_peak_day


def test_booking_has_talkback(show, weekday, weekend):
    assert not Booking(show, weekday).has_talkback
    show.set_talkback()
    assert Booking(show, weekday).has_talkback
    assert not Booking(show, weekend).has_talkback


def test_booking_base_price(show, weekday, weekend):
    assert Booking(show, weekday).base_price == 1000
    assert Booking(show, weekend).base_price == 1150


def test_premium_booking_has_talkback(show, weekday, weekend, extras):
    assert not PremiumBooking(show, weekday, extras).has_talkback
    show.set_talkback()
    assert PremiumBooking(show, weekday, extras).has_talkback
    assert PremiumBooking(show, weekend, extras).has_talkback


def test_premium_booking_base_price(show, weekday, weekend, extras):
    assert PremiumBooking(show, weekday, extras).base_price == 1200
    assert PremiumBooking(show, weekend, extras).base_price == 1350


def test_premium_booking_has_dinner(show, weekday, extras):
    assert not PremiumBooking(show, weekday, extras).has_dinner
    extras.set_dinner()
    assert PremiumBooking(show, weekday, extras).has_dinner
