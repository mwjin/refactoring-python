from datetime import date, timedelta

import pytest
from example import print_owing

from invoice import Invoice
from order import Order


@pytest.fixture
def invoice():
    _invoice = Invoice("Minwoo Jeong")
    for amount in range(10, 60, 10):
        _invoice.add_order(Order(amount))
    due_date = date.today() + timedelta(days=30)
    _invoice.due_date = due_date

    return _invoice


def test_print_owing(capsys, invoice):
    print_owing(invoice)
    expected = (
        "**** Customer Outstanding Debt ****\n",
        f"Customer: {invoice.customer}\n",
        "Outstanding Debt: 150\n",
        f"Due Date: {invoice.due_date.strftime('%d/%m/%y')}\n",
    )
    captured = capsys.readouterr()
    assert captured.out == expected
