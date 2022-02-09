class ResourcePool:
    def __init__(self) -> None:
        self._available = []
        self._allocated = []

    def get(self):
        if not self._available:
            result = Resource()
            self._allocated.append(result)
        else:
            try:
                result = self._available.pop()
                self._allocated.append(result)
            except IndexError:
                pass

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
