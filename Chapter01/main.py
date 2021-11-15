import json

from statement import statement


def main():
    invoice_doc = ""

    with open("plays.json") as play_f, open("invoices.json") as invoice_f:
        plays = json.load(play_f)
        invoices = json.load(invoice_f)

    for invoice in invoices:
        invoice_doc += statement(invoice, plays)

    print(invoice_doc, end="")


if __name__ == "__main__":
    main()
