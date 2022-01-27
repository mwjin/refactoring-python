from employee import create_engineer, create_manager, create_salesperson


def test_employee_type():
    assert create_engineer("Minwoo Jeong").type == "Engineer"
    assert create_manager("Minwoo Jeong").type == "Manager"
    assert create_salesperson("Minwoo Jeong").type == "Salesperson"
