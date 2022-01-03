def acquire_data(input):
    lines = input.split("\n")
    result = list(
        map(
            lambda record: {
                "city": record[0].strip(),
                "phone": record[2].strip(),
            },
            filter(
                lambda record: record[1].strip() == "India",
                map(
                    lambda line: line.split(","),
                    filter(lambda line: line.strip() != "", lines[1:]),
                ),
            ),
        )
    )

    return result
