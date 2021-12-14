def rating(driver):
    return 2 if more_than_five_late_deliveries(driver) else 1


def more_than_five_late_deliveries(dvr):
    return dvr.number_of_late_deliveries > 5
