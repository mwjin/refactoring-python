from employee import Employee


def test_employee_type():
    assert Employee("Minwoo Jeong", "E").type == "Engineer"
    assert Employee("Minwoo Jeong", "M").type == "Manager"
    assert Employee("Minwoo Jeong", "S").type == "Salesperson"
