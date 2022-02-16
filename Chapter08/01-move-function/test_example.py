from account import Account, AccountType
from point import Point
from track_summary import track_summary


def test_track_summary():
    points = [
        Point(51.5007, 0.1246),
        Point(40.6892, 70.1245),
    ]
    assert track_summary(points) == {
        "distance": 4410.694,
        "pace": 3.779,
        "time": 1000000,
    }


def test_account_bank_charge():
    assert Account(5, AccountType(True)).bank_charge == 14.5
    assert Account(5, AccountType(False)).bank_charge == 13.25
    assert Account(10, AccountType(True)).bank_charge == 14.65
    assert Account(10, AccountType(False)).bank_charge == 22.0
