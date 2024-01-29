# Built-in Module
from decimal import Decimal

# Local Modules
from electrum.money.money import Money
from electrum.currency.currency import Currency

# Custom Exceptions
from electrum.exceptions import InvalidBanknoteValueError


class Note(Money):

    def __init__(self, amount: int | float | str | Decimal, currency: str | int | Currency) -> None:
        super().__init__(amount, currency)
        if amount not in self.currency.banknotes:
            raise InvalidBanknoteValueError(value=amount)


class Banknote(Note):
    pass
