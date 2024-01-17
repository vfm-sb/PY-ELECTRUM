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

    def save_currencies(self) -> None:
        self.currencies = dict(sorted(self.currencies.items()))
        save_json_file(filename=AVAILABLE_CURRENCIES, path=PATH, data=self.currencies)

    def retrieve_currency_data(self, code: str | int) -> dict:
        currency_id = self.get_currency_id(code)
        filename = currency_id + ".json"
        return get_json_file(filename, path=PATH)

    def load_currency_data(self, currency_id: str) -> dict:
        if not self.currency_exists(currency_id):
            return CurrencyHelper.empty_dataset()
        return self.retrieve_currency_data(currency_id)

    def save_currency_data(self, currency_id: str, currency_data: dict) -> None:
        filename = currency_id + ".json"
        save_json_file(filename, PATH, data=currency_data)

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

    @staticmethod
    def empty_dataset() -> dict:
        return {
            "iso-alphabetic": None,
            "iso-numeric": None,
            "name": None,
            "base": None,
            "denominator": None,
            "precision": None,
            "unit-name": None,
            "unit-plural": None,
            "unit-symbol": None,
            "unit-symbol-format": None,
            "unit-abbreviation": None,
            "unit-abbreviation-format": None,
            "subunit-name": None,
            "subunit-plural": None,
            "subunit-symbol": None,
            "subunit-symbol-format": None,
            "subunit-abbreviation": None,
            "subunit-abbreviation-format": None,
            "banknotes": None,
            "coins": None,
            "users": None,
        }


# Testing
if __name__ == "__main__":
    pass
