from example import get_organization_info


def test_get_organization_info():
    assert get_organization_info() == "Samsung (KO)"
