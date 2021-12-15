def in_new_england(customer):
    return customer.address.state in ['MA', 'CI', 'ME', 'VT', 'NH', 'RI']
