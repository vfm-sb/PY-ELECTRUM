"""
Electrum Money Module
"""

# Built-in Module
from __future__ import annotations
from typing import Self, Type, Optional
from decimal import Decimal

# Local Modules
from electrum.currency.currency import Currency
from electrum.currency.currency_formatter import CurrencyFormatter

# Utilities
from electrum.utils import round_up, round_down
from electrum.utils import parse_numeric_value
from electrum.utils import convert_decimal
from electrum.utils import valid_numeric

# Custom Exceptions
from electrum.exceptions import InvalidAmountError
from electrum.exceptions import ExcessAmountError
from electrum.exceptions import InvalidOperandError
from electrum.exceptions import CurrencyMismatchError


class Money:

    rounding: Optional[str] = None

    def __init__(
        self,
        amount: int | float | str | Decimal,
        currency: str | int | Currency
    ) -> None:
        self.currency = currency
        self.amount = amount
        self.formatter = CurrencyFormatter(self.amount, self.currency)

    @property
    def currency(self) -> Currency:
        return self._currency

    @currency.setter
    def currency(self, currency: str | int | Currency) -> None:
        if isinstance(currency, (str, int)):
            self._currency = Currency(currency)
        elif isinstance(currency, Currency):
            self._currency = currency

    @property
    def amount(self) -> int | float:
        return convert_decimal(self._amount)

    @amount.setter
    def amount(self, amount: int | float | str | Decimal) -> None:
        try:
            amount = parse_numeric_value(amount)
        except ValueError as exception:
            raise InvalidAmountError(value=amount) from exception
        self._amount = Decimal(str(amount))
        self.assert_amount_precision(self._amount)

    def __hash__(self) -> int:
        return hash((self.amount, self.currency.alphabetic_code))

    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__}'
            f'({self.amount}, "{self.currency.alphabetic_code}")'
        )

    def __str__(self) -> str:
        return self.formatter.default_format()

    def __add__(self, other: Type[Money]) -> Self:
        self.assert_instance_match(other)
        self.assert_currency_match(other)
        result = self.mround(self._amount + other._amount)
        return self.construct(result, self.currency)

    def __radd__(self, other: Type[Money]) -> Self:
        return self.__add__(other)

    def __sub__(self, other: Type[Money]) -> Self:
        self.assert_instance_match(other)
        self.assert_currency_match(other)
        result = self.mround(self._amount - other._amount)
        return self.construct(result, self.currency)

    def __rsub__(self, other: Type[Money]) -> Self:
        return self.__sub__(other)

    def __mul__(self, multiplier: int | float | str | Decimal) -> Self:
        if not valid_numeric(multiplier):
            raise InvalidOperandError
        multiplier = parse_numeric_value(multiplier)
        result = self.mround(self._amount * Decimal(str(multiplier)))
        return self.construct(result, self.currency)

    def __rmul__(self, multiplier: int | float | str | Decimal) -> Self:
        return self.__mul__(multiplier)

    def __truediv__(
        self,
        other: int | float | str | Decimal | Type[Money]
    ) -> Self | float | int:
        if self.valid_instance(other):
            self.assert_currency_match(other)
            self.assert_division(other.amount)
            return convert_decimal(self._amount / other._amount)
        if not valid_numeric(other):
            raise InvalidOperandError
        other = parse_numeric_value(other)
        result = self.mround(self._amount / Decimal(str(other)))
        return self.construct(result, self.currency)

    def __floordiv__(
        self,
        other: int | float | str | Decimal | Type[Money]
    ) -> Self | int:
        if self.valid_instance(other):
            self.assert_currency_match(other)
            self.assert_division(other.amount)
            return convert_decimal(self._amount // other._amount)
        if not valid_numeric(other):
            raise InvalidOperandError
        other = parse_numeric_value(other)
        result = self.mround(self._amount // Decimal(str(other)))
        return self.construct(result, self.currency)

    def __mod__(
        self,
        other: int | float | str | Decimal | Type[Money]
    ) -> Self | float | int:
        if self.valid_instance(other):
            self.assert_currency_match(other)
            self.assert_division(other.amount)
            return convert_decimal(self._amount % other._amount)
        if not valid_numeric(other):
            raise InvalidOperandError
        other = parse_numeric_value(other)
        result = self.mround(self._amount % Decimal(str(other)))
        return self.construct(result, self.currency)

    def __pos__(self) -> Self:
        return Money(+self.amount, self.currency.alphabetic_code)

    def __neg__(self) -> Self:
        return Money(-self.amount, self.currency.alphabetic_code)

    def __abs__(self) -> Self:
        return Money(abs(self.amount), self.currency.alphabetic_code)

    def __eq__(self, other: Type[Money]) -> bool:
        self.assert_instance_match(other)
        self.assert_currency_match(other)
        return self.amount == other.amount

    def __ne__(self, other: Type[Money]) -> bool:
        return not self == other

    def __lt__(self, other: Type[Money]) -> bool:
        self.assert_instance_match(other)
        self.assert_currency_match(other)
        return self.amount < other.amount

    def __le__(self, other: Type[Money]) -> bool:
        self.assert_instance_match(other)
        self.assert_currency_match(other)
        return self.amount <= other.amount

    def __gt__(self, other: Type[Money]) -> bool:
        self.assert_instance_match(other)
        self.assert_currency_match(other)
        return self.amount > other.amount

    def __ge__(self, other: Type[Money]) -> bool:
        self.assert_instance_match(other)
        self.assert_currency_match(other)
        return self.amount >= other.amount

    def valid_instance(self, other: Type[Money]) -> bool:
        from electrum.money.coin import Coin # pylint: disable=import-outside-toplevel
        from electrum.money.note import Note, Banknote # pylint: disable=import-outside-toplevel
        from electrum.money.cash import Cash # pylint: disable=import-outside-toplevel
        return any(isinstance(other, instance) for instance in (Money, Coin, Note, Banknote, Cash))

    def assert_instance_match(self, other: Type[Money]) -> None:
        if not self.valid_instance(other):
            raise InvalidOperandError

    def assert_currency_match(self, other: Type[Money]) -> None:
        if self.currency != other.currency:
            raise CurrencyMismatchError(
                expected = self.currency.alphabetic_code,
                received = other.currency.alphabetic_code
            )

    def assert_amount_precision(self, value: Decimal) -> None:
        if value % 1 != 0 and value.as_tuple().exponent < -self.currency.precision:
            raise ExcessAmountError(value=value, limit=self.currency.denominator)

    def assert_division(self, divisor: int | float) -> None:
        if divisor == 0:
            raise ZeroDivisionError

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
    ) -> Self:
        return Money(amount, currency)

    def code_format(self, direction: str | None = None) -> str:
        return self.formatter.code_format(direction)

    def name_format(self) -> str:
        return self.formatter.name_format()

    def symbol_format(self) -> str:
        return self.formatter.symbol_format()

    def abbr_format(self) -> str:
        return self.formatter.abbr_format()


# Testing
if __name__ == "__main__":
    pass
