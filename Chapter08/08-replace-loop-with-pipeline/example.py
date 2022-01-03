def acquire_data(input):
    lines = input.split("\n")
    result = []
    loop_items = lines[1:]
    for line in loop_items:
        if line.strip() == "":
            continue
        record = line.split(",")
        if record[1].strip() == "India":
            result.append(
                {"city": record[0].strip(), "phone": record[2].strip()}
            )

    return result
