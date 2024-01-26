"""
Tests for Money Subtractions
"""
# pylint: disable=expression-not-assigned

# Built-in Modules
from decimal import Decimal

# Third-Party Modules
import pytest

# Local Modules
from electrum import Money, Currency

# Custom Exceptions
from electrum.exceptions import InvalidOperandError, CurrencyMismatchError


class TestMoneySubtraction:

    def test_subtraction_default(self):
        money = Money(4, "EUR") - Money(2, "EUR")
        assert money.amount == 2.0
        assert money.currency == Currency("EUR")

    def test_subtraction_negative_default(self):
        money = Money(2, "EUR") - Money(4, "EUR")
        assert money.amount == -2.0
        assert money.currency == Currency("EUR")

    def test_subtraction_with_int_and_float(self):
        money = Money(4, "EUR") - Money(2.2, "EUR")
        assert money.amount == 1.8

    def test_subtraction_with_two_floats(self):
        money = Money(4.4, "EUR") - Money(2.2, "EUR")
        assert money.amount == 2.2

    def test_subtraction_with_int_and_integer_string(self):
        money = Money(4, "EUR") - Money("2", "EUR")
        assert money.amount == 2.0

    def test_subtraction_with_int_and_float_string(self):
        money = Money(4, "EUR") - Money("2.2", "EUR")
        assert money.amount == 1.8

    def test_subtraction_with_float_and_float_string(self):
        money = Money(4.4, "EUR") - Money("2.2", "EUR")
        assert money.amount == 2.2

    def test_subtraction_with_two_integer_strings(self):
        money = Money("4", "EUR") - Money("2", "EUR")
        assert money.amount == 2.0

    def test_subtraction_with_integer_string_and_float_string(self):
        money = Money("4", "EUR") - Money("2.2", "EUR")
        assert money.amount == 1.8

    def test_subtraction_with_two_float_strings(self):
        money = Money("4.4", "EUR") - Money("2.2", "EUR")
        assert money.amount == 2.2

    def test_subtraction_with_int_and_decimal_integer(self):
        money = Money(4, "EUR") - Money(Decimal("2"), "EUR")
        assert money.amount == 2

    def test_subtraction_with_int_and_decimal_float(self):
        money = Money(4, "EUR") - Money(Decimal("2.2"), "EUR")
        assert money.amount == 1.8

    def test_subtraction_with_float_and_decimal_float(self):
        money = Money(4.4, "EUR") - Money(Decimal("2.2"), "EUR")
        assert money.amount == 2.2

    def test_subtraction_with_two_decimal_values(self):
        money = Money(Decimal("6.6"), "EUR") - Money(Decimal("3.3"), "EUR")
        assert money.amount == 3.3

    def test_subtraction_with_three_instances(self):
        money = Money(4.4, "EUR") - Money(2.2, "EUR") - Money(1.1, "EUR")
        assert money.amount == 1.1

    def test_working_subtractions(self):
        money = Money(1.01, "BGN") - Money(0.01, "BGN")
        assert money.amount == 1.0
        money = Money(5.5, "BGN") - Money(2.2, "BGN")
        assert money.amount == 3.3
        money = Money(17.98, "BGN") - Money(9.99, "BGN")
        assert money.amount == 7.99
        money = Money(50, "EUR") - Money(24.99, "EUR")
        assert money.amount == 25.01
        money = Money(225.50, "GBP") - Money(163.33, "GBP")
        assert money.amount == 62.17
        money = Money(2024.01, "TRY") - Money(1923.10, "TRY")
        assert money.amount == 100.91
        money = Money(16015, "JPY") - Money(13320, "JPY")
        assert money.amount == 2695
        money = Money(144_000, "USD") - Money(40_265, "USD")
        assert money.amount == 103_735

    def test_subtractions_with_invalid_operand(self):
        with pytest.raises(InvalidOperandError):
            Money(4, "EUR") - 2
        with pytest.raises(InvalidOperandError):
            4 - Money(2, "EUR")
        with pytest.raises(InvalidOperandError):
            Money(4, "EUR") - "2"
        with pytest.raises(InvalidOperandError):
            "4" - Money(2, "EUR")
        with pytest.raises(InvalidOperandError):
            Money(4, "EUR") - Decimal("2")
        with pytest.raises(InvalidOperandError):
            Decimal("4") - Money(2, "EUR")
        with pytest.raises(InvalidOperandError):
            Money(4, "EUR") - Currency("EUR")
        with pytest.raises(InvalidOperandError):
            Currency("EUR") - Money(2, "EUR")

    def test_subtractions_with_currency_mismatch(self):
        with pytest.raises(CurrencyMismatchError):
            Money(4, "EUR") - Money(2, "BGN")
        with pytest.raises(CurrencyMismatchError):
            Money(4, "BGN") - Money(2, "EUR")
