from person import Male


def get_number_of_males(people):
    return len(list(filter(lambda p: isinstance(p, Male), people)))
