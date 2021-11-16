from statement import statement, html_statement
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


def test_html_statement():
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
        "<h1>Invoice (Customer: BigCo)</h1>\n"
        "<table>\n"
        "<tr><th>Play</th><th>Seats</th><th>Price</th></tr>\n"
        "\t<tr><td>Hamlet</td><td>(55 Seats)</td><td>$650.00</td></tr>\n"
        "\t<tr><td>As You Like It</td><td>(35 Seats)</td><td>$580.00</td></tr>\n"
        "\t<tr><td>Othello</td><td>(40 Seats)</td><td>$500.00</td></tr>\n"
        "</table>\n"
        "<p>Total Amount: <em>$1,730.00</em></p>\n"
        "<p>Volume Credits: <em>47</em></p>\n"
    )
    assert html_statement(invoice, plays) == expected
