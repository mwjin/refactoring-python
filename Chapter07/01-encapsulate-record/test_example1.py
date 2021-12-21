import example1


def test_get_org_name_as_header():
    assert example1.get_org_name_as_header() == "<h1>Apple</h1>"


def test_set_org_name():
    example1.set_org_name("Samsung")
    assert example1.get_org_name_as_header() == "<h1>Samsung</h1>"

