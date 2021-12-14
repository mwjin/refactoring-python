from datetime import date, timedelta


def print_owing(invoice):
    print_banner()
    outstanding = calculate_outstanding(invoice)
    record_due_date(invoice)
    print_details(invoice, outstanding)


def print_banner():
    print("**** Customer Outstanding Debt ****")


def calculate_outstanding(invoice):
    result = 0
    for order in invoice.orders:
        result += order.amount
    return result


def record_due_date(invoice):
    today = date.today()
    invoice.due_date = today + timedelta(days=30)


def print_details(invoice, outstanding):
    print(f"Customer: {invoice.customer}")
    print(f"Outstanding Debt: {outstanding}")
    print(f"Due Date: {invoice.due_date.strftime('%d/%m/%y')}")
