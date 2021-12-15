class ShippingMethod:
    def __init__(
        self, discount_threshold, discounted_fee, fee_per_case
    ) -> None:
        self._discount_threshold = discount_threshold
        self._discounted_fee = discounted_fee
        self._fee_per_case = fee_per_case

    @property
    def discount_threshold(self):
        return self._discount_threshold

    @property
    def discounted_fee(self):
        return self._discounted_fee

    @property
    def fee_per_case(self):
        return self._fee_per_case
