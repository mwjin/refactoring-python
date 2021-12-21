import json

with open("customer_data.json") as infile:
    customer_data = json.load(infile)


def get_raw_data_of_customers():
    global customer_data
    return customer_data


def set_raw_data_of_customers(new_data):
    global customer_data
    customer_data = new_data
