def report_lines(customer):
    lines = []
    lines.append(["name", customer.name])
    gather_customer_data(lines, customer)
    return lines


def gather_customer_data(out, customer):
    out.append(["location", customer.location])
