from organization import organization


def get_org_name_as_header():
    global organization
    return f"<h1>{organization['name']}</h1>"


def set_org_name(new_name):
    global organization
    organization["name"] = new_name
