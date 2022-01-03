from functools import reduce


def get_youngest_and_total_salary(people):
    return (
        f"Youngest: {get_youngest_age(people)}, "
        f"Total Salary: {get_total_salary(people)}"
    )


def get_youngest_age(people):
    return min(map(lambda p: p.age, people))


def get_total_salary(people):
    return reduce(lambda total, p: total + p.salary, people, 0)
