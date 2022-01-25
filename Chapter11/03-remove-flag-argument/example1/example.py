def delivery_date(order, is_rush):
    if is_rush:
        if order.delivery_state in ["MA", "CT"]:
            delivery_time = 1
        elif order.delivery_state in ["NY", "NH"]:
            delivery_time = 2
        else:
            delivery_time = 3
        return order.add_days_to_placed_on(1 + delivery_time)
    else:
        if order.delivery_state in ["MA", "CT", "NY"]:
            delivery_time = 2
        elif order.delivery_state in ["ME", "NH"]:
            delivery_time = 3
        else:
            delivery_time = 4
        return order.add_days_to_placed_on(2 + delivery_time)
