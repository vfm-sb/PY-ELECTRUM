"""Custom Currency Exceptions"""


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
