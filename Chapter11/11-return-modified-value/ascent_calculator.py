class AscentCalculator:
    def __init__(self, points) -> None:
        self._points = points
        self._total_ascent = 0

    @property
    def total_ascent(self):
        self._total_ascent = self.calculate_ascent()
        return self._total_ascent

    def calculate_ascent(self):
        result = 0
        for i in range(1, len(self._points)):
            vertical_change = (
                self._points[i].elevation - self._points[i - 1].elevation
            )
            result += vertical_change if vertical_change > 0 else 0
        return result
