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
            return self.financial_ltr()
        if self.currency.default_format == "symbol":
            return self.symbol_format()
        if self.currency.default_format == "abbr":
            return self.abbr_format()
        return self.name_format()

    def financial_ltr(self) -> str:
        code_repr = f"{self.currency.alphabetic_code} {self.amount}"
        if "-" in code_repr:
            code_repr = "-" + code_repr.replace("-", "")
        return code_repr

    def financial_rtl(self) -> str:
        return f"{self.amount} {self.currency.alphabetic_code}"

    def name_format(self) -> str:
        if abs(self.amount) >= 1:
            return self.unit_name_format()
        return self.subunit_name_format()

    def unit_name_format(self) -> str:
        if abs(self.amount) > 1 and self.currency.unit_plural:
            return f"{self.amount} {self.currency.unit_plural.capitalize()}"
        return f"{self.amount} {self.currency.unit_name.capitalize()}"

    def subunit_name_format(self) -> str:
        base_amount = int(self.amount * self.currency.denominator)
        if abs(self.amount) > self.currency.base and self.currency.subunit_plural:
            return f"{base_amount} {self.currency.subunit_plural.capitalize()}"
        if self.currency.subunit_name:
            return f"{base_amount} {self.currency.subunit_name.capitalize()}"
        return self.unit_name_format()

    def symbol_format(self) -> str:
        if self.currency.unit_symbol and abs(self.amount) >= 1:
            return self.unit_symbol_format()
        if self.currency.subunit_symbol and abs(self.amount) < 1:
            return self.subunit_symbol_format()
        if self.currency.unit_abbr or self.currency.subunit_abbr:
            return self.abbr_format()
        return self.name_format()

    def unit_symbol_format(self) -> str:
        unit_repr = f'{self.currency.unit_symbol_format.replace("value", str(self.amount))}'
        if "-" in unit_repr:
            unit_repr = "-" + unit_repr.replace("-", "")
        return unit_repr

    def subunit_symbol_format(self) -> str:
        if self.currency.subunit_symbol:
            subunit_repr = f'{self.currency.subunit_symbol_format.replace("value", str(self.base_amount))}'
            if "-" in subunit_repr:
                subunit_repr = "-" + subunit_repr.replace("-", "")
            return subunit_repr
        return self.unit_symbol_format()

    def abbr_format(self) -> str:
        if self.currency.unit_abbr and abs(self.amount) >= 1:
            return self.unit_abbr_format()
        if self.currency.subunit_abbr and abs(self.amount) < 1:
            return self.subunit_abbr_format()
        return self.symbol_format()

    def unit_abbr_format(self) -> str:
        return f'{self.currency.unit_abbr_format.replace("value", str(self.amount))}'

    def subunit_abbr_format(self) -> str:
        if self.currency.subunit_abbr:
            return f'{self.currency.subunit_abbr_format.replace("value", str(self.base_amount))}'
        return self.unit_abbr_format()
