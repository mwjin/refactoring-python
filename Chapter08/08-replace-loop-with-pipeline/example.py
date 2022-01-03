def acquire_data(input):
    lines = input.split("\n")
    first_line = True
    result = []

    for line in lines:
        if first_line:
            first_line = False
            continue
        if line.strip() == "":
            continue
        record = line.split(",")
        if record[1].strip() == "India":
            result.append(
                {"city": record[0].strip(), "phone": record[2].strip()}
            )

    return result
