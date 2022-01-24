def base_charge(usage):
    if usage < 0:
        return usd(0)
    amount = (
        within_band(usage, 0, 100) * 0.03
        + within_band(usage, 100, 200) * 0.05
        + top_band(usage) * 0.07
    )
    return usd(amount)


def usd(amount):
    return f"${amount:,.2f}"


def within_band(usage, bottom, top):
    return min(usage, top) - bottom if usage > bottom else 0


def top_band(usage):
    return usage - 200 if usage > 200 else 0
