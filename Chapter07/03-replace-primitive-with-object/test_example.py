import pytest
from order import Order
from example import get_high_priority_count


@pytest.fixture
def orders():
    return [
        Order({"id": 1, "priority": "normal"}),
        Order({"id": 2, "priority": "normal"}),
        Order({"id": 3, "priority": "high"}),
        Order({"id": 4, "priority": "rush"}),
        Order({"id": 5, "priority": "high"}),
    ]


def test_get_high_priority_count(orders):
    assert get_high_priority_count(orders) == 3
