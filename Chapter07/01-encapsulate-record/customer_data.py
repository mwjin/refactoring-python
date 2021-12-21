import json


class CustomerData:
    def __init__(self, data) -> None:
        self._data = data

    def set_usage(self, customer_id, year, month, amount):
        self._data[customer_id]["usages"][year][month] = amount


with open("customer_data.json") as infile:
    customer_data = CustomerData(json.load(infile))


def get_customer_data():
    return customer_data


def get_raw_data_of_customers():
    return customer_data._data


def set_raw_data_of_customers(new_data):
    global customer_data
    customer_data = CustomerData(new_data)
