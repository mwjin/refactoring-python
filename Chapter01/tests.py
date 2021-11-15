from statement import statement
import pytest


def test_statement():
    plays = {
        "hamlet": {"name": "Hamlet", "type": "tragedy"},
        "as-like": {"name": "As You Like It", "type": "comedy"},
        "othello": {"name": "Othello", "type": "tragedy"},
    }
    invoice = {
        "customer": "BigCo",
        "performances": [
            {"playID": "hamlet", "audience": 55},
            {"playID": "as-like", "audience": 35},
            {"playID": "othello", "audience": 40},
        ],
    }
    expected = (
        "Invoice (Customer: BigCo)\n"
        "\tHamlet: $650.00 (55 Seats)\n"
        "\tAs You Like It: $580.00 (35 Seats)\n"
        "\tOthello: $500.00 (40 Seats)\n"
        "Total Amount: $1,730.00\n"
        "Volume Credits: 47\n"
    )

    assert statement(invoice, plays) == expected


def test_statement_unknown_genre():
    plays = {
        "hamlet": {"name": "Hamlet", "type": "tragedy"},
        "as-like": {"name": "As You Like It", "type": "comedy"},
        "othello": {"name": "Othello", "type": "sci-fi"},
    }
    invoice = {
        "customer": "BigCo",
        "performances": [
            {"playID": "hamlet", "audience": 55},
            {"playID": "as-like", "audience": 35},
            {"playID": "othello", "audience": 40},
        ],
    }
    with pytest.raises(ValueError):
        statement(invoice, plays)

