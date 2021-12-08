from producer import Producer


class Province:
    def __init__(self, doc: dict):
        self._name = doc["name"]
        self._producers = []
        self._total_production = 0
        self._demand = doc["demand"]
        self._price = doc["price"]
        for producer_doc in doc["producers"]:
            self.add_producer(Producer(self, producer_doc))

    def add_producer(self, producer: Producer):
        self._producers.append(producer)
        self._total_production += producer.production

    @property
    def name(self):
        return self._name

    @property
    def producers(self):
        return list(self._producers)  # Shallow copy

    @property
    def total_production(self):
        return self._total_production

    @total_production.setter
    def total_production(self, value):
        self._total_production = value

    @property
    def demand(self):
        return self._demand

    @demand.setter
    def demand(self, value):
        self._demand = int(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self.price = int(value)

    @property
    def shortfall(self):
        return self._demand - self.total_production

    @property
    def profit(self):
        return self.demand_value - self.demand_cost

    @property
    def demand_value(self):
        return self.satisfied_demand * self.price

    @property
    def satisfied_demand(self):
        return min(self._demand, self.total_production)

    @property
    def demand_cost(self):
        remaining_demand = self.demand
        result = 0
        for producer in sorted(self.producers, key=lambda p: p.cost):
            contribution = min(remaining_demand, producer.production)
            remaining_demand -= contribution
            result += contribution * producer.cost
        return result


def sample_province_data() -> dict:
    return {
        "name": "Asia",
        "producers": [
            {"name": "Byzantium", "cost": 10, "production": 9},
            {"name": "Attalia", "cost": 12, "production": 10},
            {"name": "Sinope", "cost": 10, "production": 6},
        ],
        "demand": 30,
        "price": 20,
    }
