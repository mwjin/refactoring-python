from typing import Union


class Producer:
    def __init__(self, province, data):
        self._province = province
        self._cost = data["cost"]
        self._name = data["name"]
        self._production = data.get("production", 0)

    @property
    def name(self):
        return self._name

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = int(value)

    @property
    def production(self):
        return self._production

    @production.setter
    def production(self, amount: Union[str, int]):
        if type(amount) == str:
            new_production = int(amount) if amount.isdigit() else 0
        else:
            new_production = amount
        self._province.total_production += new_production - self._production
        self._production = new_production
