class CatalogItem:
    def __init__(self, id, title, tags) -> None:
        self._id = id
        self._title = title
        self._tags = tags

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    def has_tag(self, tag):
        return tag in self._tags
