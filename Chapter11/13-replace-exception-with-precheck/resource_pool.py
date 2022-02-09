class ResourcePool:
    def __init__(self) -> None:
        self._available = []
        self._allocated = []

    def get(self):
        result = self._available.pop() if self._available else Resource()
        self._allocated.append(result)
        return result

    def add(self):
        self._available.append(Resource())


class Resource:
    __id = 0

    def __init__(self) -> None:
        self._id = Resource.__id
        Resource.__id += 1

    @property
    def id(self):
        return self._id

    @staticmethod
    def reset():
        Resource.__id = 0
