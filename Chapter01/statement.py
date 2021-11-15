import math


def statement(invoice: dict, plays: dict):
    total_amount = 0
    volume_credits = 0
    result = f'Invoice (Customer: {invoice["customer"]})\n'
    dollar_format = "${:,.2f}".format

    for perf in invoice["performances"]:
        play = plays[perf["playID"]]
        this_amount = 0

        if play["type"] == "tragedy":
            this_amount = 40000
            if perf["audience"] > 30:
                this_amount += 1000 * (perf["audience"] - 30)
        elif play["type"] == "comedy":
            this_amount = 30000
            if perf["audience"] > 20:
                this_amount += 10000 + 500 * (perf["audience"] - 20)
            this_amount += 300 * perf["audience"]
        else:
            raise ValueError(f'Unknown genre: {play["type"]}')

        volume_credits += max(perf["audience"] - 30, 0)
        if play["type"] == "comedy":
            volume_credits += math.floor(perf["audience"] / 5)

        result += f'\t{play["name"]}: {dollar_format(this_amount / 100)} ({perf["audience"]} Seats)\n'
        total_amount += this_amount

    result += f"Total Amount: {dollar_format(total_amount / 100)}\n"
    result += f"Volume Credits: {volume_credits}\n"
    return result
