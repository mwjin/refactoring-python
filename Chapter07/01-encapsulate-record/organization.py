class Organization:
    def __init__(self, data) -> None:
        self._data = data


organization = Organization({"name": "Apple", "country": "KO"})


def get_raw_data_of_organization():
    global organization
    return organization._data


def get_organization():
    global organization
    return organization
