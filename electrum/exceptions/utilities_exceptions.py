"""Custom Utilities Exceptions for Py-Electrum"""


class InvalidNumericValueError(ValueError):
    def __init__(self, message: str = "Invalid Numeric Value", value: str | None = None) -> None:
        self.message = message
        if value is not None:
            self.message += f": {value}. "
        super().__init__(self.message)


class InvalidNumericStringError(ValueError):
    def __init__(self, message: str = "Invalid Numeric String Value", value: str | None = None) -> None:
        self.message = message
        if value is not None:
            self.message += f": {value}"
        super().__init__(self.message)
