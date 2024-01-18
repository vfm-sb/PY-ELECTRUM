"""Custom Money Exceptions"""

# Built-in Modules
from typing import Any


class InvalidAmountError(ValueError):
    def __init__(self, message: str = "Invalid Amount", value: Any | None = None) -> None:
        self.message = message
        if value:
            self.message += f" >> {value}"
        super().__init__(self.message)


class InvalidCoinValueError(InvalidAmountError):
    def __init__(self, message: str = "Invalid Coin Amount", value: Any | None = None) -> None:
        self.message = message
        if value:
            self.message += f" >> {value}"
        super().__init__(message, value)


class InvalidBanknoteValueError(InvalidAmountError):
    def __init__(self, message: str = "Invalid Banknote Amount", value: Any | None = None) -> None:
        self.message = message
        if value:
            self.message += f" >> {value}"
        super().__init__(message, value)


class InvalidCashValueError(InvalidAmountError):
    def __init__(self, message: str = "Invalid Cash Amount", value: Any | None = None) -> None:
        self.message = message
        if value:
            self.message += f" >> {value}"
        super().__init__(message, value)
