# Local Modules
from electrum.currency.currency_loader import CurrencyLoader

# Custom Exceptions
from electrum.exceptions import ObjectMismatchError


class Currency:

    def __init__(self, code: str | int) -> None:
        currency_data = CurrencyLoader.load(code)
        self.alphabetic_code = currency_data["iso-alphabetic"]
        self.numeric_code = currency_data["iso-numeric"]
        self.name = currency_data["name"]
        self.base = currency_data["base"]
        self.denominator = currency_data["denominator"]
        self.precision = currency_data["precision"]
        self.unit_name = currency_data["unit-name"]
        self.unit_plural = currency_data["unit-plural"]
        self.unit_symbol = currency_data["unit-symbol"]
        self.unit_symbol_format = currency_data["unit-symbol-format"]
        self.unit_abbr = currency_data["unit-abbreviation"]
        self.unit_abbr_format = currency_data["unit-abbreviation-format"]
        self.subunit_name = currency_data["subunit-name"]
        self.subunit_plural = currency_data["subunit-plural"]
        self.subunit_symbol = currency_data["subunit-symbol"]
        self.subunit_symbol_format = currency_data["subunit-symbol-format"]
        self.subunit_abbr = currency_data["subunit-abbreviation"]
        self.subunit_abbr_format = currency_data["subunit-abbreviation-format"]
        self.default_format = currency_data["default-format"]
        self.banknotes = currency_data["banknotes"]
        self.coins = currency_data["coins"]
        self.users = currency_data["users"]

    def __hash__(self) -> int:
        return hash((self.alphabetic_code, self.numeric_code))

    def __eq__(self, other: 'Currency') -> bool:
        if not isinstance(other, Currency):
            raise ObjectMismatchError("Currency Object Mismatch", self, other)
        return self.alphabetic_code == other.alphabetic_code

    def __ne__(self, other: 'Currency') -> bool:
        return not self == other
