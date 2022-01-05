class Customer:
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
