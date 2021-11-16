import math


def statement(invoice: dict, plays: dict) -> str:
    total_amount = 0
    volume_credits = 0
    result = f'Invoice (Customer: {invoice["customer"]})\n'
    dollar_format = "${:,.2f}".format

    for perf in invoice["performances"]:
        volume_credits += get_volume_credits_for(perf, plays)
        result += (
            f'\t{get_play_for(perf, plays)["name"]}: '
            f"{dollar_format(get_amount_for(perf, plays) / 100)} "
            f'({perf["audience"]} Seats)\n'
        )
        total_amount += get_amount_for(perf, plays)

    result += f"Total Amount: {dollar_format(total_amount / 100)}\n"
    result += f"Volume Credits: {volume_credits}\n"
    return result


def get_volume_credits_for(perf, plays):
    volume_credits = max(perf["audience"] - 30, 0)
    if get_play_for(perf, plays)["type"] == "comedy":
        volume_credits += math.floor(perf["audience"] / 5)

    return volume_credits


def get_amount_for(performance: dict, plays: dict) -> int:
    result = 0

    if get_play_for(performance, plays)["type"] == "tragedy":
        result = 40000
        if performance["audience"] > 30:
            result += 1000 * (performance["audience"] - 30)
    elif get_play_for(performance, plays)["type"] == "comedy":
        result = 30000
        if performance["audience"] > 20:
            result += 10000 + 500 * (performance["audience"] - 20)
        result += 300 * performance["audience"]
    else:
        raise ValueError(
            f'Unknown genre: {get_play_for(performance, plays)["type"]}'
        )

    return result


def get_play_for(performance: dict, plays: dict) -> dict:
    return plays[performance["playID"]]
