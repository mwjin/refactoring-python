def get_high_priority_count(orders):
    return len(
        [
            order
            for order in orders
            if order.priority_string == "high"
            or order.priority_string == "rush"
        ]
    )

