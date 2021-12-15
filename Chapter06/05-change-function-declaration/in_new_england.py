def in_new_england(customer):
    return xx_in_new_england(customer.address.state)


def xx_in_new_england(state_code):
    return state_code in ["MA", "CI", "ME", "VT", "NH", "RI"]
