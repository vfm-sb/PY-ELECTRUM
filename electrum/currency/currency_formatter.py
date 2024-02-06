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

    def financial_ltr(self) -> str:
        return f"{self.currency.alphabetic_code} {self.amount}"

    def financial_rtl(self) -> str:
        return f"{self.amount} {self.currency.alphabetic_code}"

    def name_format(self) -> str:
        if self.amount >= 1:
            return self.unit_name_format()
        return self.subunit_name_format()

    def unit_name_format(self) -> str:
        if self.amount > 1 and self.currency.unit_plural:
            return f"{self.amount} {self.currency.unit_plural.capitalize()}"
        return f"{self.amount} {self.currency.unit_name.capitalize()}"

    def subunit_name_format(self) -> str:
        base_amount = int(self.amount * self.currency.denominator)
        if self.amount > self.currency.base and self.currency.subunit_plural:
            return f"{base_amount} {self.currency.subunit_plural.capitalize()}"
        if self.currency.subunit_name:
            return f"{base_amount} {self.currency.subunit_name.capitalize()}"
        return self.unit_name_format()

