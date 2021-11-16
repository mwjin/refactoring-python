import math


def statement(invoice: dict, plays: dict) -> str:
    total_amount = 0
    volume_credits = 0
    result = f'Invoice (Customer: {invoice["customer"]})\n'
    dollar_format = "${:,.2f}".format

    for perf in invoice["performances"]:
        play = get_play_for(perf, plays)
        this_amount = get_amount_for(perf, play)
        volume_credits += max(perf["audience"] - 30, 0)
        if play["type"] == "comedy":
            volume_credits += math.floor(perf["audience"] / 5)

        result += f'\t{play["name"]}: {dollar_format(this_amount / 100)} ({perf["audience"]} Seats)\n'
        total_amount += this_amount

    result += f"Total Amount: {dollar_format(total_amount / 100)}\n"
    result += f"Volume Credits: {volume_credits}\n"
    return result


def get_play_for(performance: dict, plays: dict) -> dict:
    return plays[performance["playID"]]


def get_amount_for(performance: dict, play: dict) -> int:
    result = 0

    if play["type"] == "tragedy":
        result = 40000
        if performance["audience"] > 30:
            result += 1000 * (performance["audience"] - 30)
    elif play["type"] == "comedy":
        result = 30000
        if performance["audience"] > 20:
            result += 10000 + 500 * (performance["audience"] - 20)
        result += 300 * performance["audience"]
    else:
        raise ValueError(f'Unknown genre: {play["type"]}')

    return result

