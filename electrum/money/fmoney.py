"""
Electrum FMoney (F for Finance) Module for Precise Monetary Operations
"""

# Built-in Module
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
from electrum.exceptions import InvalidOperandError
from electrum.exceptions import CurrencyMismatchError


class FMoney:

    rounding: str = None
    precision: int = 6

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
        return CurrencyFormatter(self.amount, self.currency).financial_ltr()

    def __add__(self, other):
        self.assert_instance_match(other)
        self.assert_currency_match(other)
        result = self._amount + other._amount
        return self.construct(amount=result, currency=self.currency)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        self.assert_instance_match(other)
        self.assert_currency_match(other)
        result = self._amount - other._amount
        return self.construct(amount=result, currency=self.currency)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, multiplier: int | float | str | Decimal):
        if not valid_numeric(multiplier):
            raise InvalidOperandError
        multiplier = parse_numeric_value(multiplier)
        result = self.mround(self._amount * Decimal(str(multiplier)))
        return self.construct(amount=result, currency=self.currency)

    def __rmul__(self, multiplier: int | float | str | Decimal):
        return self.__mul__(multiplier)

    def __truediv__(self, other):
        if self.valid_instance(other):
            self.assert_currency_match(other)
            self.assert_division(other.amount)
            return convert_decimal(self._amount / other._amount)
        if not valid_numeric(other):
            raise InvalidOperandError
        other = parse_numeric_value(other)
        result = self.mround(self._amount / Decimal(str(other)))
        return self.construct(amount=result, currency=self.currency)

    def __div__(self, other):
        return self.__truediv__(other)

    def __floordiv__(self, other):
        if self.valid_instance(other):
            self.assert_currency_match(other)
            self.assert_division(other.amount)
            return convert_decimal(self._amount // other._amount)
        if not valid_numeric(other):
            raise InvalidOperandError
        other = parse_numeric_value(other)
        result = self.mround(self._amount // Decimal(str(other)))
        return self.construct(amount=result, currency=self.currency)

    def __mod__(self, other):
        if self.valid_instance(other):
            self.assert_currency_match(other)
            self.assert_division(other.amount)
            return convert_decimal(self._amount % other._amount)
        if not valid_numeric(other):
            raise InvalidOperandError
        other = parse_numeric_value(other)
        result = self.mround(self._amount % Decimal(str(other)))
        return self.construct(amount=result, currency=self.currency)

    def __pos__(self):
        return FMoney(+self.amount, self.currency.alphabetic_code)

    def __neg__(self):
        return FMoney(-self.amount, self.currency.alphabetic_code)

    def __abs__(self):
        return FMoney(abs(self.amount), self.currency.alphabetic_code)

    def __eq__(self, other) -> bool:
        self.assert_currency_match(other)
        self.assert_instance_match(other)
        return self.amount == other.amount

    def __ne__(self, other) -> bool:
        return not self == other

    def __lt__(self, other) -> bool:
        self.assert_currency_match(other)
        self.assert_instance_match(other)
        return self.amount < other.amount

    def __le__(self, other) -> bool:
        self.assert_currency_match(other)
        self.assert_instance_match(other)
        return self.amount <= other.amount

    def __gt__(self, other) -> bool:
        self.assert_currency_match(other)
        self.assert_instance_match(other)
        return self.amount > other.amount

    def __ge__(self, other) -> bool:
        self.assert_currency_match(other)
        self.assert_instance_match(other)
        return self.amount >= other.amount

    def mround(self, value: Decimal) -> Decimal:
        if self.rounding == "default":
            return round(value, self.precision)
        if self.rounding == "down":
            return round_down(value, self.precision)
        if self.rounding == "up":
            return round_up(value, self.precision)
        return value

    def assert_instance_match(self, other) -> None:
        if not self.valid_instance(other):
            raise InvalidOperandError

    def assert_currency_match(self, other) -> None:
        if self.currency != other.currency:
            raise CurrencyMismatchError(
                expected = self.currency.alphabetic_code,
                received = other.currency.alphabetic_code
            )

    def assert_division(self, divisor: int | float) -> None:
        if divisor == 0:
            raise ZeroDivisionError

    def valid_instance(self, other) -> bool:
        return isinstance(other, FMoney)

    @classmethod
    def construct(
        cls,
        amount: int | float | str | Decimal,
        currency: str | int | Currency
    ):
        return cls(amount, currency)
