import math


class PerformanceCalculator:
    def __init__(self, performance: dict, play: dict):
        self.performance = performance
        self.play = play

    def get_amount(self) -> int:
        raise Exception("Use subclass")

    def get_volume_credits(self) -> int:
        return max(self.performance["audience"] - 30, 0)


class TragedyCalculator(PerformanceCalculator):
    def get_amount(self) -> int:
        result = 40000
        if self.performance["audience"] > 30:
            result += 1000 * (self.performance["audience"] - 30)
        return result


class ComedyCalculator(PerformanceCalculator):
    def get_amount(self) -> int:
        result = 30000
        if self.performance["audience"] > 20:
            result += 10000 + 500 * (self.performance["audience"] - 20)
        result += 300 * self.performance["audience"]
        return result

    def get_volume_credits(self) -> int:
        result = super().get_volume_credits()
        result += math.floor(self.performance["audience"] / 5)
        return result


def create_performance_calculator(
    performance: dict, play: dict
) -> PerformanceCalculator:
    if play["type"] == "tragedy":
        return TragedyCalculator(performance, play)
    elif play["type"] == "comedy":
        return ComedyCalculator(performance, play)
    else:
        raise ValueError(f'Unknown genre: {play["type"]}')

