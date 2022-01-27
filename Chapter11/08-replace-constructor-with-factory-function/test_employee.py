from employee import create_employee


def test_employee_type():
    assert create_employee("Minwoo Jeong", "E").type == "Engineer"
    assert create_employee("Minwoo Jeong", "M").type == "Manager"
    assert create_employee("Minwoo Jeong", "S").type == "Salesperson"
