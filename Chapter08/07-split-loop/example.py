def get_youngest_and_total_salary(people):
    return (
        f"Youngest: {get_youngest_age(people)}, "
        f"Total Salary: {get_total_salary(people)}"
    )


def get_youngest_age(people):
    return min(map(lambda p: p.age, people))


def get_total_salary(people):
    total_salary = 0
    for person in people:
        total_salary += person.salary
    return total_salary
