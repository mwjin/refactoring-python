import pytest

from employee import Employee


def test_employee_str():
    assert (
        str(Employee("Minwoo Jeong", "engineer")) == "Minwoo Jeong (Engineer)"
    )
    assert str(Employee("Minwoo Jeong", "manager")) == "Minwoo Jeong (Manager)"
    assert (
        str(Employee("Minwoo Jeong", "salesperson"))
        == "Minwoo Jeong (Salesperson)"
    )


def test_employee_with_error():
    with pytest.raises(ValueError):
        Employee("Minwoo Jeong", "Other")
