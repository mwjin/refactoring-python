class Order:
    def __init__(self, data) -> None:
        self._priority = Priority(data["priority"])
        self._id = data["id"]

    @property
    def priority(self):
        return self._priority

    @property
    def priority_string(self):
        return self._priority.to_string()

    @priority.setter
    def priority(self, value):
        self._priority = Priority(value)

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value


class Priority:
    def __init__(self, value) -> None:
        if isinstance(value, Priority):
            return value
        if value not in Priority.legal_values():
            raise ValueError(f"'{value}' is invalid priority.")
        self._value = value

    def to_string(self):
        return self._value

    @staticmethod
    def legal_values():
        return ["low", "normal", "high", "rush"]

    @property
    def _index(self):
        return Priority.legal_values().index(self._value)

    def __eq__(self, other):
        return self._index == other._index

    def __gt__(self, other):
        return self._index > other._index

    def __lt__(self, other):
        return self._index < other._index
