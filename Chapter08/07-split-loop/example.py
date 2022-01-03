def get_youngest_and_total_salary(people):
    youngest = people[0].age
    total_salary = 0

    for person in people:
        if person.age < youngest:
            youngest = person.age
        total_salary += person.salary

    for person in people:
        if person.age < youngest:
            youngest = person.age
        total_salary += person.salary

    return f"Youngest: {youngest}, Total Salary: {total_salary}"

