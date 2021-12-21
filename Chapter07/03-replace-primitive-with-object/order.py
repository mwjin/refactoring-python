class Order:
    def __init__(self, data) -> None:
        self._priority = data["priority"]
        self._id = data["id"]

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        self._priority = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
