# Built-in Module
from typing import Union
from decimal import Decimal

# Local Modules
from electrum.currency.currency import Currency

# Utilities
from electrum.utils.parser_utils import parse_numeric_value

# Custom Exceptions
from electrum.exceptions.currency_exceptions import InvalidCurrencyError
from electrum.exceptions.money_exceptions import InvalidAmountError


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
        else:
            raise InvalidCurrencyError

    @property
    def amount(self) -> int | float:
        return self._amount

    @amount.setter
    def amount(self, amount: Union[int, float, str, Decimal]) -> None:
        if not isinstance(amount, (int, float, str, Decimal)):
            raise InvalidAmountError(value=amount)
        self._amount = parse_numeric_value(amount)

    @property
    def base_amount(self) -> int:
        return self._base_amount

    @base_amount.setter
    def base_amount(self, base_amount: int) -> None:
        self._base_amount = base_amount

    def amount_to_base(self, amount: int | float) -> int:
        return amount * self.currency.denominator
