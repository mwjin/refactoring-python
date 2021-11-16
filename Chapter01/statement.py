import math
from copy import copy
from functools import reduce


def statement(invoice: dict, plays: dict) -> str:
    return render_plain_text(create_statement_data(invoice, plays))


def create_statement_data(invoice: dict, plays: dict) -> dict:
    statement_data = {}
    statement_data["customer"] = invoice["customer"]
    statement_data["performances"] = [
        enrich_performance(perf, plays) for perf in invoice["performances"]
    ]
    statement_data["total_amount"] = get_total_amount(statement_data)
    statement_data["total_volume_credits"] = get_total_volume_credits(
        statement_data
    )
    return statement_data


def enrich_performance(performance: dict, plays: dict) -> dict:
    result = copy(performance)  # Shallow copy
    result["play"] = get_play_for(performance, plays)
    result["amount"] = get_amount_for(result)
    result["volume_credits"] = get_volume_credits_for(result)
    return result


def get_play_for(performance: dict, plays: dict) -> dict:
    return plays[performance["playID"]]


def get_amount_for(performance: dict) -> int:
    result = 0

    if performance["play"]["type"] == "tragedy":
        result = 40000
        if performance["audience"] > 30:
            result += 1000 * (performance["audience"] - 30)
    elif performance["play"]["type"] == "comedy":
        result = 30000
        if performance["audience"] > 20:
            result += 10000 + 500 * (performance["audience"] - 20)
        result += 300 * performance["audience"]
    else:
        raise ValueError(f'Unknown genre: {performance["play"]["type"]}')

    return result


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


def render_plain_text(data: dict) -> str:
    result = f'Invoice (Customer: {data["customer"]})\n'

    for perf in data["performances"]:
        result += (
            f'\t{perf["play"]["name"]}: '
            f'{get_usd(perf["amount"])} '
            f'({perf["audience"]} Seats)\n'
        )

    result += f"Total Amount: {get_usd(data['total_amount'])}\n"
    result += f"Volume Credits: {data['total_volume_credits']}\n"
    return result


def get_usd(num: float) -> str:
    return "${:,.2f}".format(num / 100)

