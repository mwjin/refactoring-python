from example import get_youngest_and_total_salary
from person import Person


def test_get_youngest_and_total_salary():
    people = [Person(17, 2400), Person(32, 3750), Person(12, 10000)]
    assert (
        get_youngest_and_total_salary(people)
        == "Youngest: 12, Total Salary: 16150"
    )
