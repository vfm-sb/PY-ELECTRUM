"""
Abstact BaseMoney
"""

# Built-in Module
from abc import ABC, abstractmethod
from decimal import Decimal

# Local Modules
from electrum.currency.currency import Currency


class BaseMoney(ABC):

    @abstractmethod
    def __init__(
        self,
        amount: int | float | str | Decimal,
        currency: str | int | Currency
    ) -> None:
        ...

    @property
    @abstractmethod
    def currency(self) -> Currency:
        ...

    @currency.setter
    @abstractmethod
    def currency(self, currency: str | int | Currency) -> None:
        ...

    @property
    @abstractmethod
    def amount(self) -> int | float:
        ...

    @amount.setter
    @abstractmethod
    def amount(self, amount: int | float | str | Decimal) -> None:
        ...

    @abstractmethod
    def __hash__(self) -> int:
        ...

    @abstractmethod
    def __repr__(self) -> str:
        ...

    @abstractmethod
    def __str__(self) -> str:
        ...

    @abstractmethod
    def __add__(self, other):
        ...

    @abstractmethod
    def __radd__(self, other):
        ...

    @abstractmethod
    def __sub__(self, other):
        ...

    @abstractmethod
    def __rsub__(self, other):
        ...

    @abstractmethod
    def __mul__(self, multiplier):
        ...

    @abstractmethod
    def __rmul__(self, multiplier):
        ...

    @abstractmethod
    def __truediv__(self, other):
        ...

    @abstractmethod
    def __floordiv__(self, other):
        ...

    @abstractmethod
    def __mod__(self, other):
        ...

    @abstractmethod
    def __pos__(self):
        ...

    @abstractmethod
    def __neg__(self):
        ...

    @abstractmethod
    def __abs__(self):
        ...

    @abstractmethod
    def __eq__(self, other) -> bool:
        ...

    @abstractmethod
    def __ne__(self, other) -> bool:
        ...

    @abstractmethod
    def __lt__(self, other) -> bool:
        ...

    @abstractmethod
    def __le__(self, other) -> bool:
        ...

    @abstractmethod
    def __gt__(self, other) -> bool:
        ...

    @abstractmethod
    def __ge__(self, other) -> bool:
        ...

    @abstractmethod
    def valid_instance(self, other) -> bool:
        ...

    @abstractmethod
    def assert_instance_match(self, other) -> None:
        ...

    @abstractmethod
    def assert_currency_match(self, other) -> None:
        ...

    @abstractmethod
    def assert_division(self, divisor: int | float) -> None:
        ...

    @abstractmethod
    def mround(self, value: Decimal) -> Decimal:
        ...

    @classmethod
    @abstractmethod
    def construct(
        cls,
        amount: int | float | str | Decimal,
        currency: str | int | Currency
    ):
        ...
