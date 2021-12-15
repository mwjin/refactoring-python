def in_new_england(customer):
    state_code = customer.address.state
    return state_code in ["MA", "CI", "ME", "VT", "NH", "RI"]
