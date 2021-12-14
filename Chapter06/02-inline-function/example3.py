def report_lines(customer):
    lines = []
    gather_customer_data(lines, customer)
    return lines


def gather_customer_data(out, customer):
    out.append(["name", customer.name])
    out.append(["location", customer.location])
