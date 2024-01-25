"""Custom Currency Exceptions"""


class InvalidCurrencyError(ValueError):
    def __init__(self, message: str = "Invalid Currency") -> None:
        self.message = message
        super().__init__(self.message)


class InvalidCurrencyCodeError(ValueError):
    def __init__(self, message: str = "Invalid Currency Code", code: str | int | None = None) -> None:
        self.message = message
        if code:
            self.message += f" >> {code}"
        super().__init__(self.message)


class CurrencyNotFoundError(FileNotFoundError):
    def __init__(self, message: str = "Currency Doesn't Exist", code: str | int | None = None) -> None:
        self.message = message
        if code:
            self.message += f" >> {code}"
        super().__init__(self.message)


class CurrencyMismatchError(ValueError):
    def __init__(
        self,
        message: str = "Currencies Must Match",
        expected: str | None = None, received: str | None = None
    ) -> None:
        self.message = message
        if expected and received:
            self.message += f" >> Expected: {expected}, Received: {received}"
        super().__init__(self.message)
