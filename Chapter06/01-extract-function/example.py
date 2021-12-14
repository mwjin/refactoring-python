from datetime import date, timedelta


def print_owing(invoice):
    outstanding = 0

    print("**** Customer Outstanding Debt ****")

    # Calculate the outstanding debt
    for order in invoice.orders:
        outstanding += order.amount

    # Record the due date
    today = date.today()
    invoice.due_date = today + timedelta(days=30)

    # Print the details
    print(f"Customer: {invoice.customer}")
    print(f"Outstanding Debt: {outstanding}")
    print(f"Due Date: {invoice.due_date.strftime('%d/%m/%y')}")
