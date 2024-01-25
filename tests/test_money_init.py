"""
Tests for Money Initializations
"""

# Built-in Modules
from decimal import Decimal

# Third-Party Modules
import pytest

# Local Modules
from electrum import Money, Currency
from electrum.exceptions import CurrencyNotFoundError
from electrum.exceptions import InvalidAmountError, ExcessAmountError


class TestMoneyInit:

    def test_init_with_currency_default(self):
        money = Money(2, "EUR")
        assert money.amount == 2
        assert money.currency == Currency("EUR")

    def test_init_with_currency_instance_eur(self):
        money = Money(2, Currency("EUR"))
        assert money.currency.alphabetic_code == "EUR"
        assert money.currency.numeric_code == "978"

    def test_init_with_currency_instance_bgn(self):
        money = Money(2, Currency("BGN"))
        assert money.currency.alphabetic_code == "BGN"
        assert money.currency.numeric_code == "975"

    def test_init_with_currency_lowercase(self):
        money = Money(2, "eur")
        assert money.currency == Currency("EUR")

    def test_init_with_currency_mixcase(self):
        money = Money(2, "EuR")
        assert money.currency == Currency("EUR")

    def test_init_with_currency_numeric_default(self):
        money = Money(2, 978)
        assert money.currency == Currency("EUR")

    def test_init_with_currency_numeric_string(self):
        money = Money(2, "978")
        assert money.currency == Currency("EUR")

    def test_init_amount_with_float(self):
        money = Money(2.2, "EUR")
        assert money.amount == 2.2

    def test_init_amount_with_string(self):
        money = Money("4", "EUR")
        assert money.amount == 4

    def test_init_amount_with_decimal_numeric(self):
        money = Money(Decimal(4), "EUR")
        assert money.amount == 4

    def test_init_amount_with_decimal_string(self):
        money = Money(Decimal("4"), "EUR")
        assert money.amount == 4

    def test_init_with_currency_not_found(self):
        with pytest.raises(CurrencyNotFoundError):
            Money(200, "DEM")
        with pytest.raises(CurrencyNotFoundError):
            Money(1000, "BGL")
        with pytest.raises(CurrencyNotFoundError):
            Money(1_350_000, "TRL")
        with pytest.raises(CurrencyNotFoundError):
            Money(200, "276")
        with pytest.raises(CurrencyNotFoundError):
            Money(1000, "100")
        with pytest.raises(CurrencyNotFoundError):
            Money(1_350_000, "792")
        with pytest.raises(CurrencyNotFoundError):
            Money(200, Currency("DEM"))
        with pytest.raises(CurrencyNotFoundError):
            Money(1000, Currency("BGL"))
        with pytest.raises(CurrencyNotFoundError):
            Money(1_350_000, Currency("TRL"))

    def test_init_with_invalid_amount(self):
        with pytest.raises(InvalidAmountError):
            Money("x", "EUR")
        with pytest.raises(InvalidAmountError):
            Money("53K", "BGN")
        with pytest.raises(InvalidAmountError):
            Money("100B", "TRY")

    def test_init_with_excess_amount(self):
        with pytest.raises(ExcessAmountError):
            Money(1.992, "EUR")
        with pytest.raises(ExcessAmountError):
            Money(1.999, "BGN")
        with pytest.raises(ExcessAmountError):
            Money(2.005, "TRY")
        with pytest.raises(ExcessAmountError):
            Money(2024.1, "JPY")
