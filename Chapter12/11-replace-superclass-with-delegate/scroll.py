from catalog_item import CatalogItem


class Scroll:
    def __init__(
        self, id, title, tags, date_last_cleaned, catalog_id, catalog
    ) -> None:
        self._id = id
        self._catalog_item = CatalogItem(None, title, tags)
        self._last_cleaned = date_last_cleaned

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._catalog_item.title

    def has_tag(self, tag):
        return self._catalog_item.has_tag(tag)

    def needs_cleaning(self, target_date):
        threshold = 700 if self.has_tag("revered") else 1500
        return self.days_since_last_cleaning(target_date) > threshold

    def days_since_last_cleaning(self, target_date):
        return (target_date - self._last_cleaned).days
