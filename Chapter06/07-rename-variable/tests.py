import title


def test_read_title():
    result = title.tphd
    assert result == "Untitled"


def test_set_title():
    title.tphd = "Hello"
    assert title.tphd == "Hello"
