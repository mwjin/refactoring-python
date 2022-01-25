from datetime import timedelta


def delivery_date(order, is_rush):
    if order.delivery_state == "MA" or order.delivery_state == "CT":
        delivery_time = 1 if is_rush else 2
    elif order.delivery_state == "NY" or order.delivery_state == "NH":
        delivery_time = 2
        if order.delivery_state == "NH" and not is_rush:
            delivery_time = 3
    elif is_rush:
        delivery_time = 3
    elif order.delivery_state == "ME":
        delivery_time = 3
    else:
        delivery_time = 4
    result = order.add_days_to_placed_on(2 + delivery_time)
    if is_rush:
        result -= timedelta(days=1)
    return result
