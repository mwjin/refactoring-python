from datetime import date, timedelta

from catalog_item import CatalogItem
from scroll import Scroll


def test_days_since_last_cleaning():
    expect = 600
    target_date = date.today()
    last_cleaned_date = target_date - timedelta(days=expect)
    catalog = {1: CatalogItem(1, "Catalog1", [])}
    assert (
        Scroll(
            0, "Scroll1", [], last_cleaned_date, 1, catalog
        ).days_since_last_cleaning(target_date)
        == expect
    )


def test_needs_cleaning():
    target_date = date.today()
    catalog = {1: CatalogItem(1, "Catalog1", [])}
    assert not Scroll(
        1, "Scroll1", [], target_date - timedelta(days=1500), 1, catalog
    ).needs_cleaning(target_date)
    assert Scroll(
        2, "Scroll2", [], target_date - timedelta(days=1501), 1, catalog
    ).needs_cleaning(target_date)


def test_needs_cleaning_with_revered_tag():
    target_date = date.today()
    catalog = {1: CatalogItem(1, "Catalog1", ["revered"])}
    assert not Scroll(
        1, "Scroll1", ["revered"], target_date - timedelta(days=700), 1, catalog
    ).needs_cleaning(target_date)
    assert Scroll(
        2, "Scroll2", ["revered"], target_date - timedelta(days=701), 1, catalog
    ).needs_cleaning(target_date)
