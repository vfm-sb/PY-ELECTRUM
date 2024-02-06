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
