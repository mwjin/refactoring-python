from customer_data import get_customer_data


def compare_usage(customer_id, later_year, month):
    earlier_year = str(int(later_year) - 1)
    later = get_customer_data().raw_data[customer_id]["usages"][later_year][
        month
    ]
    earlier = get_customer_data().raw_data[customer_id]["usages"][earlier_year][
        month
    ]
    return {"laterAmount": later, "change": later - earlier}


def set_usage(customer_id, year, month, amount):
    get_customer_data().set_usage(customer_id, year, month, amount)
