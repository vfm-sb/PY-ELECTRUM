"""
Electrum Money Module
"""

# Built-in Module
from typing import Self
from decimal import Decimal

# Local Modules
from electrum.money._money import _Money
from electrum.currency.currency import Currency
from electrum.currency.currency_formatter import CurrencyFormatter

# Utilities
from electrum.utils import round_up, round_down

# Custom Exceptions
from electrum.exceptions import ExcessAmountError


class Money(_Money):

    rounding: str | None = None

    def __init__(
        self,
        amount: int | float | str | Decimal,
        currency: str | int | Currency
    ) -> None:
        super().__init__(amount, currency)
        self.formatter = CurrencyFormatter(self.amount, self.currency)

    @property
    def amount(self):
        return super().amount

    @amount.setter
    def amount(self, amount: int | float | str | Decimal) -> None:
        super(Money, type(self)).amount.fset(self, amount)
        self.assert_amount_precision(self._amount)

    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__}'
            f'({self.amount}, "{self.currency.alphabetic_code}")'
        )

    def __str__(self) -> str:
        return self.formatter.default_format()

    def __pos__(self) -> 'Money':
        return Money(+self.amount, self.currency.alphabetic_code)

    def __neg__(self) -> 'Money':
        return Money(-self.amount, self.currency.alphabetic_code)

    def __abs__(self) -> 'Money':
        return Money(abs(self.amount), self.currency.alphabetic_code)

    def valid_instance(self, other: Self) -> bool:
        from electrum.money.coin import Coin # pylint: disable=import-outside-toplevel
        from electrum.money.note import Note, Banknote # pylint: disable=import-outside-toplevel
        from electrum.money.cash import Cash # pylint: disable=import-outside-toplevel
        return any(isinstance(other, instance) for instance in (Money, Coin, Note, Banknote, Cash))

    def assert_amount_precision(self, value: int | float) -> None:
        if value % 1 != 0 and value.as_tuple().exponent < -self.currency.precision:
            raise ExcessAmountError(value=value, limit=self.currency.denominator)

    def mround(self, value: Decimal) -> Decimal:
        if self.rounding == "down":
            return round_down(value, self.currency.precision)
        if self.rounding == "up":
            return round_up(value, self.currency.precision)
        return round(value, self.currency.precision)

    @classmethod
    def construct(
        cls,
        amount: int | float | str | Decimal,
        currency: str | int | Currency
    ) -> 'Money':
        return Money(amount, currency)

    # Formatters
    def financialize(self, direction: str = "ltr") -> str:
        if direction == "ltr":
            return self.formatter.financial_ltr()
        if direction == "rtl":
            return self.formatter.financial_rtl()
        raise ValueError("Invalid Direction Argument")

    def name_format(self) -> str:
        return self.formatter.name_format()

    @property
    def symbolize(self) -> str:
        return self.formatter.symbol_format()

    @property
    def abbreviate(self) -> str:
        return self.formatter.abbr_format()


# Testing
if __name__ == "__main__":
    pass
