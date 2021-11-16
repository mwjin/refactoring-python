from copy import copy
from functools import reduce

from performance_calculator import create_performance_calculator


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


def get_play_for(performance: dict, plays: dict) -> dict:
    return plays[performance["playID"]]


def get_total_amount(data: dict) -> int:
    return reduce(lambda total, p: total + p["amount"], data["performances"], 0)


def get_total_volume_credits(data: dict) -> int:
    return reduce(
        lambda total, p: total + p["volume_credits"], data["performances"], 0
    )
