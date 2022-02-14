from department import Department
from employee import Employee


def test_get_name_department():
    assert (
        Department("Team1", Employee("Minwoo Jeong", 1, 1000)).name == "Team1"
    )


def test_get_name_employee():
    assert Employee("Minwoo Jeong", 1, 1000).name == "Minwoo Jeong"
