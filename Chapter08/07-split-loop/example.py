def get_youngest_and_total_salary(people):
    return (
        f"Youngest: {get_youngest_age(people)}, "
        f"Total Salary: {get_total_salary(people)}"
    )


def get_youngest_age(people):
    youngest = people[0].age
    for person in people:
        if person.age < youngest:
            youngest = person.age
    return youngest


def get_total_salary(people):
    total_salary = 0
    for person in people:
        total_salary += person.salary
    return total_salary
