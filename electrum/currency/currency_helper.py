# Utilities
from electrum.utils import get_json_file, save_json_file

# Custom Exceptions
from electrum.exceptions import CurrencyNotFoundError

# Constants
from electrum.currency import PATH
from electrum.currency import AVAILABLE_CURRENCIES


class CurrencyHelper:

    def __init__(self) -> None:
        self.currencies = self.load_currencies()

    def load_currencies(self) -> dict:
        return get_json_file(filename=AVAILABLE_CURRENCIES, path=PATH)

    def retrieve_currency_data(self, code: str | int) -> dict:
        currency_id = self.get_currency_id(code)
        filename = currency_id + ".json"
        return get_json_file(filename, path=PATH)

    def get_currency_id(self, code: str | int) -> str | None:
        code = str(code).upper()
        for currency_id, data in self.currencies.items():
            iso_codes = (data["iso-alphabetic"], data["iso-numeric"])
            if code in iso_codes:
                return currency_id
        return None

    def currency_exists(self, code: str | int) -> bool:
        currency_id = self.get_currency_id(code)
        return currency_id in self.currencies

    def assert_currency(self, code: str | int) -> None:
        if not self.currency_exists(code):
            raise CurrencyNotFoundError


# Testing
if __name__ == "__main__":
    pass
