class Point:
    def __init__(self, elevation) -> None:
        self._elevation = elevation

    @property
    def elevation(self):
        return self._elevation
