from distutils.log import error


class OrderProcessingError(Exception):
    def __init__(self, error_code) -> None:
        super().__init__(f"Order Processing Error: {error_code}")
        self._code = error_code

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return "OrderProcessingError"
