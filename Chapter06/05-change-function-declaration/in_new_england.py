def in_new_england(customer):
    state_code = customer.address.state
    return xx_in_new_england(state_code)


def xx_in_new_england(state_code):
    return state_code in ["MA", "CI", "ME", "VT", "NH", "RI"]
