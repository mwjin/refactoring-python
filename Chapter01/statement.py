from statement_data import create_statement_data


def statement(invoice: dict, plays: dict) -> str:
    return render_plain_text(create_statement_data(invoice, plays))


def render_plain_text(data: dict) -> str:
    result = f"Invoice (Customer: {data['customer']})\n"

    for perf in data["performances"]:
        result += (
            f"\t{perf['play']['name']}: "
            f"{get_usd(perf['amount'])} ({perf['audience']} Seats)\n"
        )

    result += f"Total Amount: {get_usd(data['total_amount'])}\n"
    result += f"Volume Credits: {data['total_volume_credits']}\n"
    return result


def get_usd(num: float) -> str:
    return "${:,.2f}".format(num / 100)

