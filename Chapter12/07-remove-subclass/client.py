from person import Male


def get_number_of_males(people):
    return len(list(filter(lambda p: is_male(p), people)))


def is_male(person):
    return isinstance(person, Male)
