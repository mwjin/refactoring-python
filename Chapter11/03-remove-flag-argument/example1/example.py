def delivery_date(order, is_rush):
    if is_rush:
        return rush_delivery_date(order)
    else:
        return regular_delivery_date(order)


def rush_delivery_date(order):
    if order.delivery_state in ["MA", "CT"]:
        delivery_time = 1
    elif order.delivery_state in ["NY", "NH"]:
        delivery_time = 2
    else:
        delivery_time = 3
    return order.add_days_to_placed_on(1 + delivery_time)


def regular_delivery_date(order):
    if order.delivery_state in ["MA", "CT", "NY"]:
        delivery_time = 2
    elif order.delivery_state in ["ME", "NH"]:
        delivery_time = 3
    else:
        delivery_time = 4
    return order.add_days_to_placed_on(2 + delivery_time)
