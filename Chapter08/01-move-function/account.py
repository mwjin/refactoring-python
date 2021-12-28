class Account:
    def __init__(self, days_overdrawn, type) -> None:
        self._days_overdrawn = days_overdrawn
        self._type = type

    @property
    def days_overdrawn(self):
        return self._days_overdrawn

    @property
    def type(self):
        return self._type

    @property
    def bank_charge(self):
        result = 4.5
        if self._days_overdrawn > 0:
            result += self.type.over_draft_charge(self.days_overdrawn)
        return result


class AccountType:
    def __init__(self, is_premium):
        self._is_premium = is_premium

    @property
    def is_premium(self):
        return self._is_premium

    def over_draft_charge(self, days_overdrawn):
        if self.is_premium:
            base_charge = 10
            if days_overdrawn <= 7:
                return base_charge
            else:
                return base_charge + (days_overdrawn - 7) * 0.05
        else:
            return days_overdrawn * 1.75
