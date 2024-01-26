"""
Tests for Money Multiplications
"""
# pylint: disable=expression-not-assigned

# Built-in Modules
from decimal import Decimal

# Third-Party Modules
import pytest

# Local Modules
from electrum import Money, Currency

# Custom Exceptions
from electrum.exceptions import InvalidOperandError


class TestMoneyMultiplication:

    def test_multiplication_default(self):
        money = Money(2, "EUR") * 2
        assert money.amount == 4.0
        assert money.currency == Currency("EUR")

    def test_multiplication_default_in_reverse(self):
        money = 2 * Money(2, "EUR")
        assert money.amount == 4.0

    def test_multiplying_int_money_by_float_value(self):
        money = Money(2, "EUR") * 2.2
        assert money.amount == 4.4

    def test_multiplying_float_value_by_int_money(self):
        money = 2.2 * Money(2, "EUR")
        assert money.amount == 4.4

    def test_multiplying_float_money_by_float_value(self):
        money = Money(2.2, "EUR") * 2.2
        assert money.amount == 4.84

    def test_multiplying_float_value_by_float_money(self):
        money = 2.2 * Money(2.2, "EUR")
        assert money.amount == 4.84

    def test_multiplying_int_money_by_str_value(self):
        money = Money(2, "EUR") * "2"
        assert money.amount == 4.0

    def test_multiplying_int_value_by_str_money(self):
        money = 2 * Money("2", "EUR")
        assert money.amount == 4.0

    def test_multiplying_str_money_by_str_value(self):
        money = Money("2", "EUR") * "2"
        assert money.amount == 4.0

    def test_multiplying_str_value_by_str_money(self):
        money = "2" * Money("2", "EUR")
        assert money.amount == 4.0

    def test_multiplying_money_by_decimal_value(self):
        money = Money(2, "EUR") * Decimal("2")
        assert money.amount == 4.0

    def test_multiplying_decimal_value_by_money(self):
        money = Decimal("2") * Money(2, "EUR")
        assert money.amount == 4.0

    def test_working_multiplications(self):
        money = Money(2.49, "BGN") * 4
        assert money.amount == 9.96
        money = Money(5.30, "EUR") * 5
        assert money.amount == 26.5
        money = Money(221.83, "GBP") * 12
        assert money.amount == 2661.96
        money = Money(1329.00, "TRY") * 1.20
        assert money.amount == 1594.8
        money = Money(1775, "JPY") * 4
        assert money.amount == 7100
        money = Money(305_955.02, "USD") * 0.08
        assert money.amount == 24_476.40

    def test_multiplications_with_invalid_operand(self):
        with pytest.raises(InvalidOperandError):
            Money(2, "EUR") * Money(2, "EUR")
        with pytest.raises(InvalidOperandError):
            Money(2, "EUR") * Money(2, "USD")
