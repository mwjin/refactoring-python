from organization import get_raw_data_of_organization


def get_org_name_as_header():
    return f"<h1>{get_raw_data_of_organization()['name']}</h1>"


def set_org_name(new_name):
    get_raw_data_of_organization()["name"] = new_name
