"""
Tests for Money Modulo-Divisions
"""
# pylint: disable=expression-not-assigned

# Built-in Modules
from decimal import Decimal

# Third-Party Modules
import pytest

# Local Modules
from electrum import Money, Currency

# Custom Exceptions
from electrum.exceptions import CurrencyMismatchError


class TestMoneyModuloDivision:

    def test_modulo_division_of_money_by_money_default(self):
        result = Money(3, "EUR") % Money(2, "EUR")
        assert result == 1.0
        result = Money(4, "EUR") % Money(1.5, "EUR")
        assert result == 1.0
        result = Money(6.4, "EUR") % Money(2.2, "EUR")
        assert result == 2.0
        result = Money(3, "EUR") % Money("2", "EUR")
        assert result == 1.0
        result = Money("3", "EUR") % Money(2, "EUR")
        assert result == 1.0
        result = Money(4, "EUR") % Money("1.5", "EUR")
        assert result == 1.0
        result = Money("4", "EUR") % Money(1.5, "EUR")
        assert result == 1.0
        result = Money(6.4, "EUR") % Money("2.2", "EUR")
        assert result == 2.0
        result = Money("6.4", "EUR") % Money(2.2, "EUR")
        assert result == 2.0
        result = Money("3", "EUR") % Money("2", "EUR")
        assert result == 1.0
        result = Money("4", "EUR") % Money("1.5", "EUR")
        assert result == 1.0
        result = Money("6.4", "EUR") % Money("2.2", "EUR")
        assert result == 2.0
        result = Money(3, "EUR") % Money(Decimal("2"), "EUR")
        assert result == 1.0
        result = Money(Decimal("3"), "EUR") % Money(2, "EUR")
        assert result == 1.0
        result = Money(Decimal("3"), "EUR") % Money(Decimal("2"), "EUR")
        assert result == 1.0

    def test_modulo_division_of_money_by_numeric_default(self):
        money = Money(3, "EUR") % 2
        assert money.amount == 1.0
        assert money.currency == Currency("EUR")
        money = Money(4, "EUR") % 1.5
        assert money.amount == 1.0
        money = Money(6.4, "EUR") % 2.2
        assert money.amount == 2.0
        money = Money(3, "EUR") % "2"
        assert money.amount == 1.0
        money = Money("3", "EUR") % 2
        assert money.amount == 1.0
        money = Money(4, "EUR") % "1.5"
        assert money.amount == 1.0
        money = Money("4", "EUR") % 1.5
        assert money.amount == 1.0
        money = Money(6.4, "EUR") % "2.2"
        assert money.amount == 2.0
        money = Money("6.4", "EUR") % 2.2
        assert money.amount == 2.0
        money = Money("3", "EUR") % "2"
        assert money.amount == 1.0
        money = Money("4", "EUR") % "1.5"
        assert money.amount == 1.0
        money = Money("6.4", "EUR") % "2.2"
        assert money.amount == 2.0
        money = Money(3, "EUR") % Decimal("2")
        assert money.amount == 1.0
        money = Money(Decimal("3"), "EUR") % 2
        assert money.amount == 1.0
        money = Money(Decimal("3"), "EUR") % Decimal("2")
        assert money.amount == 1.0

    def test_working_modulo_divisions_money_by_money(self):
        result = Money(20, "BGN") % Money(3.12, "BGN")
        assert result == 1.28
        result = Money(50, "EUR") % Money(4.99, "EUR")
        assert result == 0.1
        result = Money(225, "GBP") % Money(11.70, "GBP")
        assert result == 2.7
        result = Money(33_200, "TRY") % Money(1329.00, "TRY")
        assert result == 1304
        result = Money(160_837, "JPY") % Money(1775, "JPY")
        assert result == 1087
        result = Money(305_955.02, "USD") % Money(2400, "USD")
        assert result == 1155.02

    def test_working_modulo_divisions_money_by_numeric(self):
        money = Money(20, "BGN") % 6
        assert money.amount == 2.0
        money = Money(50, "EUR") % 7
        assert money.amount == 1.0
        money = Money(225, "GBP") % 35
        assert money.amount == 15.0
        money = Money(30_200, "TRY") % 30
        assert money.amount == 20.0

    def test_money_by_money_modulo_divisions_with_currency_mismatch(self):
        with pytest.raises(CurrencyMismatchError):
            Money(2, "EUR") % Money(2, "BGN")
        with pytest.raises(CurrencyMismatchError):
            Money(2, "BGN") % Money(2, "EUR")
