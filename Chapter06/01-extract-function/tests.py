from datetime import date, timedelta

from example import print_owing


def test_print_owing(capsys, invoice):
    due_date = date.today() + timedelta(days=30)
    print_owing(invoice)
    expected = (
        "**** Customer Outstanding Debt ****\n",
        f"Customer: {invoice.customer}\n",
        "Outstanding Debt: 150\n",
        f"Due Date: {due_date.strftime('%d/%m/%y')}\n",
    )
    captured = capsys.readouterr()
    assert captured.out == expected
