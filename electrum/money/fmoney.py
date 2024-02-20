"""
Electrum FMoney (F for Finance) Module for Precise Monetary Operations
"""

# Built-in Module
from decimal import Decimal
from typing import Self

# Local Modules
from electrum.money.money import Money
from electrum.currency.currency import Currency
from electrum.currency.currency_formatter import CurrencyFormatter

# Utilities
from electrum.utils import round_up, round_down
from electrum.utils import parse_numeric_value
from electrum.utils import convert_decimal
from electrum.utils import valid_numeric

# Custom Exceptions
from electrum.exceptions import InvalidAmountError
from electrum.exceptions import InvalidOperandError
from electrum.exceptions import CurrencyMismatchError


class FMoney:

    rounding: str | None = None
    precision: int = 6
    direction: str = "ltr"

    def __init__(
        self,
        amount: int | float | str | Decimal,
        currency: str | int | Currency
    ) -> None:
        self.currency = currency
        self.amount = amount

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

    def __hash__(self) -> int:
        return hash((self.amount, self.currency.alphabetic_code))

    def __repr__(self) -> str:
        return (
            f'{self.__class__.__name__}'
            f'({self.amount}, "{self.currency.alphabetic_code}")'
        )

    def __str__(self) -> str:
        return CurrencyFormatter(self.amount, self.currency).code_format(self.direction)

    def __add__(self, other: Self) -> Self:
        self.assert_instance_match(other)
        self.assert_currency_match(other)
        result = self.mround(self._amount + other._amount)
        return self.construct(result, self.currency)

    def __radd__(self, other: Self) -> Self:
        return self.__add__(other)

    def __sub__(self, other: Self) -> Self:
        self.assert_instance_match(other)
        self.assert_currency_match(other)
        result = self.mround(self._amount - other._amount)
        return self.construct(result, self.currency)

    def __rsub__(self, other: Self) -> Self:
        return self.__sub__(other)

    def __mul__(self, multiplier: int | float | str | Decimal) -> Self:
        if not valid_numeric(multiplier):
            raise InvalidOperandError
        multiplier = parse_numeric_value(multiplier)
        result = self.mround(self._amount * Decimal(str(multiplier)))
        return self.construct(result, self.currency)

    def __rmul__(self, multiplier: int | float | str | Decimal) -> Self:
        return self.__mul__(multiplier)

    def __truediv__(self, other: int | float | str | Decimal | Self) -> Self | float | int:
        if self.valid_instance(other):
            self.assert_currency_match(other)
            self.assert_division(other.amount)
            return convert_decimal(self._amount / other._amount)
        if not valid_numeric(other):
            raise InvalidOperandError
        other = parse_numeric_value(other)
        result = self.mround(self._amount / Decimal(str(other)))
        return self.construct(result, self.currency)

    def __floordiv__(self, other: int | float | str | Decimal | Self) -> Self | int:
        if self.valid_instance(other):
            self.assert_currency_match(other)
            self.assert_division(other.amount)
            return convert_decimal(self._amount // other._amount)
        if not valid_numeric(other):
            raise InvalidOperandError
        other = parse_numeric_value(other)
        result = self.mround(self._amount // Decimal(str(other)))
        return self.construct(result, self.currency)

    def __mod__(self, other: int | float | str | Decimal | Self) -> Self | float | int:
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
        return FMoney(+self.amount, self.currency.alphabetic_code)

    def __neg__(self) -> Self:
        return FMoney(-self.amount, self.currency.alphabetic_code)

    def __abs__(self) -> Self:
        return FMoney(abs(self.amount), self.currency.alphabetic_code)

    def __eq__(self, other: Self) -> bool:
        self.assert_instance_match(other)
        self.assert_currency_match(other)
        return self.amount == other.amount

    def __ne__(self, other: Self) -> bool:
        return not self == other

    def __lt__(self, other: Self) -> bool:
        self.assert_instance_match(other)
        self.assert_currency_match(other)
        return self.amount < other.amount

    def __le__(self, other: Self) -> bool:
        self.assert_instance_match(other)
        self.assert_currency_match(other)
        return self.amount <= other.amount

    def __gt__(self, other: Self) -> bool:
        self.assert_instance_match(other)
        self.assert_currency_match(other)
        return self.amount > other.amount

    def __ge__(self, other: Self) -> bool:
        self.assert_instance_match(other)
        self.assert_currency_match(other)
        return self.amount >= other.amount

    def valid_instance(self, other: Self) -> bool:
        return isinstance(other, FMoney)

    def assert_instance_match(self, other: Self) -> None:
        if not self.valid_instance(other):
            raise InvalidOperandError

    def assert_currency_match(self, other: Self) -> None:
        if self.currency != other.currency:
            raise CurrencyMismatchError(
                expected = self.currency.alphabetic_code,
                received = other.currency.alphabetic_code
            )

    def assert_division(self, divisor: int | float) -> None:
        if divisor == 0:
            raise ZeroDivisionError

    def mround(self, amount: Decimal) -> Decimal:
        if self.rounding == "down":
            return round_down(amount, self.precision)
        if self.rounding == "up":
            return round_up(amount, self.precision)
        return round(amount, self.precision)

    @classmethod
    def construct(
        cls,
        amount: int | float | str | Decimal,
        currency: str | int | Currency
    ) -> Self:
        return FMoney(amount, currency)

    def to_money(
        self,
        rounding: str | None = None
    ) -> Money:
        if rounding is not None:
            self.rounding = rounding
        self.precision = self.currency.precision
        return Money(self.mround(self._amount), self.currency)
