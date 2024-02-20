"""
Currency Formatter for Electrum
"""

# Local Modules
from electrum.currency.currency import Currency


class CurrencyFormatter:

    def __init__(self, amount: int | float, currency: Currency) -> None:
        self.currency = currency
        self.amount = amount
        self.base_amount = int(self.amount * self.currency.denominator)

    def default_format(self):
        if self.currency.default_format == "code":
            return self.code_format()
        if self.currency.default_format == "symbol":
            return self.symbol_format()
        if self.currency.default_format == "abbr":
            return self.abbr_format()
        return self.name_format()

    def code_format(self, direction: str = "ltr") -> str:
        if direction == "rtl":
            return f"{self.amount} {self.currency.alphabetic_code}"
        ltr_repr = f"{self.currency.alphabetic_code} {self.amount}"
        return self.normalize_output(ltr_repr)

    def name_format(self) -> str:
        if abs(self.amount) >= 1:
            return self._unit_name_format()
        return self._subunit_name_format()

    def _unit_name_format(self) -> str:
        if abs(self.amount) > 1 and self.currency.unit_plural:
            return f"{self.amount} {self.currency.unit_plural.capitalize()}"
        return f"{self.amount} {self.currency.unit_name.capitalize()}"

    def _subunit_name_format(self) -> str:
        base_amount = int(self.amount * self.currency.denominator)
        if abs(self.amount) > self.currency.base and self.currency.subunit_plural:
            return f"{base_amount} {self.currency.subunit_plural.capitalize()}"
        if self.currency.subunit_name:
            return f"{base_amount} {self.currency.subunit_name.capitalize()}"
        return self._unit_name_format()

    def symbol_format(self) -> str:
        if self.currency.unit_symbol and abs(self.amount) >= 1:
            return self._unit_symbol_format()
        if self.currency.subunit_symbol and abs(self.amount) < 1:
            return self._subunit_symbol_format()
        if self.currency.unit_abbr or self.currency.subunit_abbr:
            return self.abbr_format()
        return self.name_format()

    def _unit_symbol_format(self) -> str:
        unit_repr = f'{self.currency.unit_symbol_format.replace("value", str(self.amount))}'
        return self.normalize_output(unit_repr)

    def _subunit_symbol_format(self) -> str:
        if self.currency.subunit_symbol:
            subunit_repr = f'{self.currency.subunit_symbol_format.replace("value", str(self.base_amount))}'
            return self.normalize_output(subunit_repr)
        return self._unit_symbol_format()

    def abbr_format(self) -> str:
        if self.currency.unit_abbr and abs(self.amount) >= 1:
            return self._unit_abbr_format()
        if self.currency.subunit_abbr and abs(self.amount) < 1:
            return self._subunit_abbr_format()
        return self.symbol_format()

    def _unit_abbr_format(self) -> str:
        return f'{self.currency.unit_abbr_format.replace("value", str(self.amount))}'

    def _subunit_abbr_format(self) -> str:
        if self.currency.subunit_abbr:
            return f'{self.currency.subunit_abbr_format.replace("value", str(self.base_amount))}'
        return self._unit_abbr_format()

    @staticmethod
    def normalize_output(value_repr: str) -> str:
        if "-" in value_repr:
            value_repr = "-" + value_repr.replace("-", "")
        return value_repr
