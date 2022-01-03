def acquire_data(input):
    lines = input.split("\n")
    result = []
    loop_items = filter(lambda line: line.strip() != "", lines[1:])
    for line in loop_items:
        record = line.split(",")
        if record[1].strip() == "India":
            result.append(
                {"city": record[0].strip(), "phone": record[2].strip()}
            )

    return result
