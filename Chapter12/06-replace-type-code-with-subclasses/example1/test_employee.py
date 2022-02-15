import pytest

from employee import create_employee


def test_employee_str():
    assert (
        str(create_employee("Minwoo Jeong", "engineer"))
        == "Minwoo Jeong (engineer)"
    )
    assert (
        str(create_employee("Minwoo Jeong", "manager"))
        == "Minwoo Jeong (manager)"
    )
    assert (
        str(create_employee("Minwoo Jeong", "salesperson"))
        == "Minwoo Jeong (salesperson)"
    )


def test_employee_with_error():
    with pytest.raises(ValueError):
        create_employee("Minwoo Jeong", "Other")
