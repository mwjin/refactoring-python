from datetime import date, timedelta

from scroll import Scroll


def test_days_since_last_cleaning():
    expect = 600
    target_date = date.today()
    last_cleaned_date = target_date - timedelta(days=expect)
    assert (
        Scroll(0, "Scroll1", [], last_cleaned_date).days_since_last_cleaning(
            target_date
        )
        == expect
    )


def test_needs_cleaning():
    target_date = date.today()
    assert not Scroll(
        1, "Scroll1", [], target_date - timedelta(days=1500)
    ).needs_cleaning(target_date)
    assert Scroll(
        2, "Scroll2", [], target_date - timedelta(days=1501)
    ).needs_cleaning(target_date)


def test_needs_cleaning_with_revered_tag():
    target_date = date.today()
    assert not Scroll(
        1, "Scroll1", ["revered"], target_date - timedelta(days=700)
    ).needs_cleaning(target_date)
    assert Scroll(
        2, "Scroll2", ["revered"], target_date - timedelta(days=701)
    ).needs_cleaning(target_date)
