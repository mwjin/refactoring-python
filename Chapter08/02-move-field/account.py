class Account:
    def __init__(self, number, type, interest_rate) -> None:
        self._number = number
        self._type = type
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self._interest_rate


class AccountType:
    def __init__(self, name, interest_rate) -> None:
        self._name = name
        self._interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self._interest_rate
