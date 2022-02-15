def get_number_of_males(people):
    return len(list(filter(lambda p: p.is_male, people)))
