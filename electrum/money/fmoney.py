"""
Electrum FMoney (F for Finance) Module for Precise Monetary Operations
"""

# Built-in Module
from decimal import Decimal
from typing import Self

# Local Modules
from electrum.money._money import _Money
from electrum.money.money import Money
from electrum.currency.currency import Currency
from electrum.currency.currency_formatter import CurrencyFormatter

# Utilities
from electrum.utils import round_up, round_down


class FMoney(_Money):

    rounding: str | None = None
    precision: int = 6
    formatter: str = "financial-ltr"

    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__}'
            f'({self.amount}, "{self.currency.alphabetic_code}")'
        )

    def __str__(self) -> str:
        formatter = CurrencyFormatter(self.amount, self.currency)
        if self.formatter in ["financial-rtl", "rtl"]:
            return formatter.financial_rtl()
        return formatter.financial_ltr()

    def valid_instance(self, other: Self) -> bool:
        return isinstance(other, FMoney)

    def mround(self, value: Decimal) -> Decimal:
        if self.rounding == "down":
            return round_down(value, self.precision)
        if self.rounding == "up":
            return round_up(value, self.precision)
        return round(value, self.precision)

    @classmethod
    def construct(
        cls,
        amount: int | float | str | Decimal,
        currency: str | int | Currency
    ) -> 'FMoney':
        return FMoney(amount, currency)

    def to_money(
        self,
        rounding: str | None = None
    ) -> Money:
        if rounding is not None:
            self.rounding = rounding
        self.precision = self.currency.precision
        return Money(self.mround(self._amount), self.currency)
