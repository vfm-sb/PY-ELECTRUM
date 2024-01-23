"""Custom Money Exceptions"""

# Built-in Modules
from typing import Any


class InvalidAmountError(ValueError):
    def __init__(self, message: str = "Invalid Amount", value: Any | None = None) -> None:
        self.message = message
        if value:
            self.message += f" >> {value}"
        super().__init__(self.message)


class ExcessAmountError(ValueError):
    def __init__(
        self,
        message: str = "Excess Amount",
        value: float | None = None,
        limit: int | None = None
    ) -> None:
        self.message = message
        if value:
            self.message += f" >> {value % 1}"
        if limit:
            self.message += f" Value Cannot Exceed {limit - 1}"
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
