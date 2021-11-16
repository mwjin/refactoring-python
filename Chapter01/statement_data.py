import math
from copy import copy
from functools import reduce


class PerformanceCalculator:
    def __init__(self, performance, play):
        self.performance = performance
        self.play = play

    def get_amount(self) -> int:
        result = 0

        if self.play["type"] == "tragedy":
            result = 40000
            if self.performance["audience"] > 30:
                result += 1000 * (self.performance["audience"] - 30)
        elif self.play["type"] == "comedy":
            result = 30000
            if self.performance["audience"] > 20:
                result += 10000 + 500 * (self.performance["audience"] - 20)
            result += 300 * self.performance["audience"]
        else:
            raise ValueError(f'Unknown genre: {self.play["type"]}')

        return result


def create_statement_data(invoice: dict, plays: dict) -> dict:
    result = {}
    result["customer"] = invoice["customer"]
    result["performances"] = [
        enrich_performance(perf, plays) for perf in invoice["performances"]
    ]
    result["total_amount"] = get_total_amount(result)
    result["total_volume_credits"] = get_total_volume_credits(result)
    return result


def enrich_performance(performance: dict, plays: dict) -> dict:
    calculator = PerformanceCalculator(
        performance, get_play_for(performance, plays)
    )
    result = copy(performance)  # Shallow copy
    result["play"] = calculator.play
    result["amount"] = get_amount_for(result)
    result["volume_credits"] = get_volume_credits_for(result)
    return result


def get_play_for(performance: dict, plays: dict) -> dict:
    return plays[performance["playID"]]


def get_amount_for(performance: dict) -> int:
    return PerformanceCalculator(performance, performance["play"]).get_amount()


def get_volume_credits_for(performance: dict) -> int:
    result = max(performance["audience"] - 30, 0)
    if performance["play"]["type"] == "comedy":
        result += math.floor(performance["audience"] / 5)

    return result


def get_total_amount(data: dict) -> int:
    return reduce(lambda total, p: total + p["amount"], data["performances"], 0)


def get_total_volume_credits(data: dict) -> int:
    return reduce(
        lambda total, p: total + p["volume_credits"], data["performances"], 0
    )
