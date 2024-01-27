# Built-in Module
from __future__ import annotations
from typing import Union, TYPE_CHECKING
from decimal import Decimal

# Local Modules
from electrum.currency.currency import Currency

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

if TYPE_CHECKING:
    from electrum.money.coin import Coin
    from electrum.money.note import Note, Banknote
    from electrum.money.cash import Cash


class Money:

    def __init__(
        self,
        amount: Union[int, float, str, Decimal],
        currency: Union[str, int, Currency]
    ) -> None:
        self.currency = currency
        self.amount = amount
        self.base_amount = self.amount_to_base(self.amount)

    @property
    def currency(self) -> Currency:
        return self._currency

    @currency.setter
    def currency(self, currency: Union[str, int, Currency]) -> None:
        if isinstance(currency, (str, int)):
            self._currency = Currency(currency)
        elif isinstance(currency, Currency):
            self._currency = currency

    @property
    def amount(self) -> int | float:
        return self._amount

    @amount.setter
    def amount(self, amount: Union[int, float, str, Decimal]) -> None:
        try:
            amount = parse_numeric_value(amount)
        except ValueError as exception:
            raise InvalidAmountError(value=amount) from exception
        self.assert_amount_precision(amount)
        self._amount = amount

    @property
    def base_amount(self) -> int:
        return self._base_amount

    @base_amount.setter
    def base_amount(self, base_amount: int) -> None:
        self._base_amount = base_amount

    def __hash__(self) -> int:
        return hash((self.amount, self.currency.alphabetic_code))

    def __repr__(self) -> str:
        return f'Money({self.amount}, "{self.currency.alphabetic_code}")'

    def __str__(self) -> str:
        pass

    def __add__(self, other: Union[Money, Coin, Note, Banknote, Cash]) -> Money:
        self.assert_instance(other)
        self.assert_currency(other)
        base_result = self.base_amount + other.base_amount
        amount = self.base_to_amount(base_result)
        return Money(amount, self.currency.alphabetic_code)

    def __radd__(self, other: Union[Money, Coin, Note, Banknote, Cash]) -> Money:
        return self.__add__(other)

    def __sub__(self, other: Union[Money, Coin, Note, Banknote, Cash]) -> Money:
        self.assert_instance(other)
        self.assert_currency(other)
        base_result = self.base_amount - other.base_amount
        amount = self.base_to_amount(base_result)
        return Money(amount, self.currency.alphabetic_code)

    def __rsub__(self, other: Union[Money, Coin, Note, Banknote, Cash]) -> Money:
        self.__sub__(other)

    def __mul__(self, multiplier: Union[int, float, str, Decimal]) -> Money:
        if not valid_numeric(multiplier):
            raise InvalidOperandError
        multiplier = parse_numeric_value(multiplier)
        base_result = self.base_amount * multiplier
        amount = self.base_to_amount(base_result)
        return Money(amount, self.currency.alphabetic_code)

    def __rmul__(self, multiplier: Union[int, float, str, Decimal]) -> Money:
        return self.__mul__(multiplier)

    def __truediv__(
        self,
        other: Union[int, float, str, Decimal, Money, Coin, Note, Banknote, Cash]
    ) -> Union[Money, float]:
        if self.valid_instance(other):
            self.assert_currency(other)
            self.assert_division(other.amount)
            result = Decimal(str(self.amount)) / Decimal(str(other.amount))
            return convert_decimal(result)
        if not valid_numeric(other):
            raise InvalidOperandError
        other = parse_numeric_value(other)
        amount = self.mround(self.amount / other, mode="down")
        return Money(amount, self.currency.alphabetic_code)

    def __div__(
        self,
        other: Union[int, float, str, Decimal, Money, Coin, Note, Banknote, Cash]
    ) -> Union[Money, float]:
        return self.__truediv__(other)

    def __floordiv__(
        self,
        other: Union[int, float, str, Decimal, Money, Coin, Note, Banknote, Cash]
    ) -> Union[Money, float]:
        if self.valid_instance(other):
            self.assert_currency(other)
            self.assert_division(other.amount)
            return self.amount // other.amount
        if not valid_numeric(other):
            raise InvalidOperandError
        other = parse_numeric_value(other)
        amount = self.amount // other
        return Money(amount, self.currency.alphabetic_code)

    def __mod__(
        self,
        other: Union[int, float, str, Decimal, Money, Coin, Note, Banknote, Cash]
    ) -> Union[Money, float]:
        if self.valid_instance(other):
            self.assert_currency(other)
            self.assert_division(other.amount)
            return self.base_amount % other.base_amount
        if not valid_numeric(other):
            raise InvalidOperandError
        other = parse_numeric_value(other)
        amount = self.amount % other
        return Money(amount, self.currency.alphabetic_code)

    def __pos__(self) -> Money:
        return Money(+self.amount, self.currency.alphabetic_code)

    def __neg__(self) -> Money:
        return Money(-self.amount, self.currency.alphabetic_code)

    def __abs__(self) -> Money:
        return Money(abs(self.amount), self.currency.alphabetic_code)

    def __eq__(self, other: Union[Money, Coin, Note, Banknote, Cash]) -> bool:
        self.assert_currency(other)
        self.assert_instance(other)
        return self.amount == other.amount

    def __ne__(self, other: Union[Money, Coin, Note, Banknote, Cash]) -> bool:
        return not self == other

    def __lt__(self, other: Union[Money, Coin, Note, Banknote, Cash]) -> bool:
        self.assert_currency(other)
        self.assert_instance(other)
        return self.amount < other.amount

    def __le__(self, other: Union[Money, Coin, Note, Banknote, Cash]) -> bool:
        self.assert_currency(other)
        self.assert_instance(other)
        return self.amount <= other.amount

    def __gt__(self, other: Union[Money, Coin, Note, Banknote, Cash]) -> bool:
        self.assert_currency(other)
        self.assert_instance(other)
        return self.amount > other.amount

    def __ge__(self, other: Union[Money, Coin, Note, Banknote, Cash]) -> bool:
        self.assert_currency(other)
        self.assert_instance(other)
        return self.amount >= other.amount

    def amount_to_base(self, amount: int | float) -> int:
        return int(amount * self.currency.denominator)

    def base_to_amount(self, base_value: int) -> float | int:
        return self.mround(base_value * self.currency.base)

    def mround(self, value: int | float, mode: str | None = None) -> int | float:
        """
        Rounds Monetary Value to the Precision of the Currency.
        """
        if mode == "down":
            return round_down(value, self.currency.precision)
        if mode == "up":
            return round_up(value, self.currency.precision)
        return round(value, self.currency.precision)

    def assert_instance(self, other: Union[Money, Coin, Note, Banknote, Cash]) -> None:
        if not self.valid_instance(other):
            raise InvalidOperandError

    def assert_currency(self, other: Union[Money, Coin, Note, Banknote, Cash]) -> None:
        if self.currency != other.currency:
            raise CurrencyMismatchError(
                expected = self.currency.alphabetic_code,
                received = other.currency.alphabetic_code
            )

    def assert_amount_precision(self, value: int | float) -> None:
        decimal_value = Decimal(str(value))
        if decimal_value % 1 != 0 and decimal_value.as_tuple().exponent < -self.currency.precision:
            raise ExcessAmountError(value=value, limit=self.currency.denominator)

    def assert_division(self, divisor: int | float) -> None:
        if divisor == 0:
            raise ZeroDivisionError

    def valid_instance(self, other: Union[Money, Coin, Note, Banknote, Cash]) -> bool:
        from electrum.money.coin import Coin # pylint: disable=import-outside-toplevel
        from electrum.money.note import Note, Banknote # pylint: disable=import-outside-toplevel
        from electrum.money.cash import Cash # pylint: disable=import-outside-toplevel
        return any(isinstance(other, instance) for instance in (Money, Coin, Note, Banknote, Cash))


# Testing
if __name__ == "__main__":
    pass
