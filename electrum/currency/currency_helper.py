# Local Modules
import pyvutils

# Custom Exceptions
from electrum.exceptions import InvalidCurrencyCodeError
from electrum.exceptions import CurrencyNotFoundError

# Constants
PATH = "data/currencies"
AVAILABLE_CURRENCIES = "_CURRENCIES.json"


class CurrencyHelper:

    def __init__(self) -> None:
        self.currencies = self.load_currencies()

    def load_currencies(self) -> dict:
        return pyvutils.projectkit.get_json(AVAILABLE_CURRENCIES, PATH)

    def save_currencies(self) -> None:
        self.currencies = dict(sorted(self.currencies.items()))
        pyvutils.projectkit.save_json(AVAILABLE_CURRENCIES, PATH, self.currencies)

    def retrieve_currency_data(self, code: str | int) -> dict:
        currency_id = self.get_currency_id(code)
        filename = currency_id + ".json"
        return pyvutils.projectkit.get_json(filename, PATH)

    def load_currency_data(self, currency_id: str) -> dict:
        if not self.currency_exists(currency_id):
            return CurrencyHelper.empty_dataset()
        return self.retrieve_currency_data(currency_id)

    def save_currency_data(self, currency_id: str, currency_data: dict) -> None:
        filename = currency_id + ".json"
        pyvutils.projectkit.save_json(filename, PATH, currency_data)

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
    def valid_currency_code(code: str | int) -> bool:
        return CurrencyHelper.valid_alphabetic_code(code) or CurrencyHelper.valid_numeric_code(code)

    @staticmethod
    def valid_alphabetic_code(code: str) -> bool:
        return isinstance(code, str) and code.isalpha() and len(code) == 3

    @staticmethod
    def valid_numeric_code(code: int | str) -> bool:
        return str(code).isdigit() and len(str(code)) == 3

    @staticmethod
    def assert_currency_code(code: str | int) -> None:
        if not CurrencyHelper.valid_currency_code(code):
            raise InvalidCurrencyCodeError(code=code)

    @staticmethod
    def assert_alphabetic_code(code: str) -> None:
        if not CurrencyHelper.valid_alphabetic_code(code):
            raise InvalidCurrencyCodeError("Invalid Alphabetic Currency Code", code=code)

    @staticmethod
    def assert_numeric_code(code: int | str) -> None:
        if not CurrencyHelper.valid_numeric_code(code):
            raise InvalidCurrencyCodeError("Invalid Numeric Currency Code", code=code)

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
            "default-format": None,
            "banknotes": None,
            "coins": None,
            "users": None,
        }


# Testing
if __name__ == "__main__":
    pass
