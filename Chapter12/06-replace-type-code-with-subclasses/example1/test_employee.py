import pytest

from employee import Employee


def test_employee_str():
    assert (
        str(Employee("Minwoo Jeong", "engineer")) == "Minwoo Jeong (engineer)"
    )
    assert str(Employee("Minwoo Jeong", "manager")) == "Minwoo Jeong (manager)"
    assert (
        str(Employee("Minwoo Jeong", "salesperson"))
        == "Minwoo Jeong (salesperson)"
    )


def test_employee_with_error():
    with pytest.raises(ValueError):
        Employee("Minwoo Jeong", "Other")
