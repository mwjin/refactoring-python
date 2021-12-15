import title


def test_read_title():
    result = title.title()
    assert result == "Untitled"


def test_set_title():
    title.set_title("Hello")
    assert title.title() == "Hello"
