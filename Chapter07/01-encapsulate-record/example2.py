from customer_data import get_raw_data_of_customers


def compare_usage(customer_id, later_year, month):
    earlier_year = str(int(later_year) - 1)
    later = get_raw_data_of_customers()[customer_id]["usages"][later_year][
        month
    ]
    earlier = get_raw_data_of_customers()[customer_id]["usages"][earlier_year][
        month
    ]
    return {"laterAmount": later, "change": later - earlier}


def set_usage(customer_id, year, month, amount):
    get_raw_data_of_customers()[customer_id]["usages"][year][month] = amount
