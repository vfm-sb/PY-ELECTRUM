# Local Modules
from electrum.currency.currency_helper import CurrencyHelper


class CurrencyLoader(CurrencyHelper):

    def __init__(self, code: str | int) -> None:
        super().__init__()
        self.assert_currency(code)
        self.currency_data = self.retrieve_currency_data(code)

    @classmethod
    def load(cls, code: str | int) -> dict:
        currency = cls(code)
        return currency.currency_data
