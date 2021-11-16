import math
from copy import copy
from functools import reduce


class PerformanceCalculator:
    def __init__(self, performance: dict, play: dict):
        self.performance = performance
        self.play = play

    def get_amount(self) -> int:
        raise Exception("Use subclass")

    def get_volume_credits(self) -> int:
        result = max(self.performance["audience"] - 30, 0)
        if self.play["type"] == "comedy":
            result += math.floor(self.performance["audience"] / 5)

        return result


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
    calculator = create_performance_calculator(
        performance, get_play_for(performance, plays)
    )
    result = copy(performance)  # Shallow copy
    result["play"] = calculator.play
    result["amount"] = calculator.get_amount()
    result["volume_credits"] = calculator.get_volume_credits()
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


def get_play_for(performance: dict, plays: dict) -> dict:
    return plays[performance["playID"]]


def get_total_amount(data: dict) -> int:
    return reduce(lambda total, p: total + p["amount"], data["performances"], 0)


def get_total_volume_credits(data: dict) -> int:
    return reduce(
        lambda total, p: total + p["volume_credits"], data["performances"], 0
    )
