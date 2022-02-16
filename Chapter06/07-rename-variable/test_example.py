import company_name
import title


def test_read_title():
    result = title.title()
    assert result == "Untitled"


def test_set_title():
    title.set_title("Hello")
    assert title.title() == "Hello"


def test_company_name():
    assert company_name.company_name() == "Samsung"


def test_print_company_name(capsys):
    company_name.print_company_name()
    captured = capsys.readouterr()
    assert captured.out == "Samsung"
