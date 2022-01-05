class Customer:
    repository = {}

    def __init__(self, id):
        self._id = id
        self._name = ""

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, arg):
        self._name = arg

    @staticmethod
    def register_customer(id):
        if id not in Customer.repository:
            Customer.repository[id] = Customer(id)
        return Customer.repository.get(id)
