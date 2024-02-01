# Built-in Module
from decimal import Decimal

# Local Modules
from electrum.money.money import Money
from electrum.currency.currency import Currency

# Custom Exceptions
from electrum.exceptions import InvalidCashValueError


class Cash(Money):

    def __init__(self, amount: int | float | str | Decimal, currency: str | int | Currency) -> None:
        super().__init__(amount, currency)
        valid_cash_values = self.currency.coins + self.currency.banknotes
        if self.amount not in valid_cash_values:
            raise InvalidCashValueError(value=amount)
