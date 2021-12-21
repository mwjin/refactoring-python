from organization import get_organization


def get_org_name_as_header():
    return f"<h1>{get_organization().name}</h1>"


def set_org_name(new_name):
    get_organization().name = new_name
