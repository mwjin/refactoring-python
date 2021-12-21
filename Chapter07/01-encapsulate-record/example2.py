from customer_data import customer_data


def compare_usage(customer_id, later_year, month):
    global customer_data
    earlier_year = str(int(later_year) - 1)
    later = customer_data[customer_id]["usages"][later_year][month]
    earlier = customer_data[customer_id]["usages"][earlier_year][month]
    return {"laterAmount": later, "change": later - earlier}


def set_amount(customer_id, year, month, amount):
    global customer_data
    customer_data[customer_id]["usages"][year][month] = amount
