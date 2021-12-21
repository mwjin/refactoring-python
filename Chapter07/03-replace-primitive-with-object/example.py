def get_high_priority_count(orders):
    return len(
        [
            order
            for order in orders
            if order.priority == "high" or order.priority == "rush"
        ]
    )

