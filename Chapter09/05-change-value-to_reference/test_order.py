from order import Order
from functools import reduce


def test_customer_change_name():
    order_records = [
        {"number": 1, "customer": 1},
        {"number": 2, "customer": 1},
        {"number": 3, "customer": 1},
    ]
    orders = [Order(data) for data in order_records]
    customers = [order.customer for order in orders]
    customers[0].name = "Minwoo Jeong"
    assert customers[0].name == customers[1].name == customers[2].name
