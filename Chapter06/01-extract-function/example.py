from datetime import date, timedelta


def print_owing(invoice):
    print_banner()

    # Calculate the outstanding debt
    outstanding = 0
    for order in invoice.orders:
        outstanding += order.amount

    record_due_date(invoice)
    print_details(invoice, outstanding)


def print_banner():
    print("**** Customer Outstanding Debt ****")


def calculate_outstanding(invoice):
    outstanding = 0
    for order in invoice.orders:
        outstanding += order.amount
    return outstanding


def record_due_date(invoice):
    today = date.today()
    invoice.due_date = today + timedelta(days=30)


def print_details(invoice, outstanding):
    print(f"Customer: {invoice.customer}")
    print(f"Outstanding Debt: {outstanding}")
    print(f"Due Date: {invoice.due_date.strftime('%d/%m/%y')}")
