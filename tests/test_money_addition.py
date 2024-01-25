# Built-in Modules
from decimal import Decimal

# Third-Party Modules
import pytest

# Local Modules
from electrum import Money, Currency

# Custom Exceptions
from electrum.exceptions import InvalidOperandError, CurrencyMismatchError


class TestMoneyAddition:

    def test_addition_default(self):
        money = Money(2, "EUR") + Money(2, "EUR")
        assert money.amount == 4.0
        assert money.currency == Currency("EUR")

    def test_addition_with_int_and_float(self):
        money = Money(2, "EUR") + Money(2.2, "EUR")
        assert money.amount == 4.2

    def test_addition_with_float_and_float_basic(self):
        money = Money(2.2, "EUR") + Money(2.2, "EUR")
        assert money.amount == 4.4

    def test_addition_with_int_and_integer_string(self):
        money = Money(2, "EUR") + Money("2", "EUR")
        assert money.amount == 4.0

    def test_addition_with_int_and_float_string(self):
        money = Money(2, "EUR") + Money("2.2", "EUR")
        assert money.amount == 4.2

    def test_addition_with_float_and_float_string(self):
        money = Money(2.2, "EUR") + Money("2.2", "EUR")
        assert money.amount == 4.4

    def test_addition_with_two_integer_strings(self):
        money = Money("2", "EUR") + Money("2", "EUR")
        assert money.amount == 4.0

    def test_addition_with_integer_string_and_float_string(self):
        money = Money("2", "EUR") + Money("2.2", "EUR")
        assert money.amount == 4.2

    def test_addition_with_two_float_strings(self):
        money = Money("2.2", "EUR") + Money("2.2", "EUR")
        assert money.amount == 4.4

    def test_addition_with_int_and_decimal_integer(self):
        money = Money(2, "EUR") + Money(Decimal(2), "EUR")
        assert money.amount == 4.0

    def test_addition_with_int_and_decimal_float(self):
        money = Money(2, "EUR") + Money(Decimal("2.2"), "EUR")
        assert money.amount == 4.2

    def test_addition_with_float_and_decimal_float(self):
        money = Money(2.2, "EUR") + Money(Decimal("2.2"), "EUR")
        assert money.amount == 4.4

    def test_addition_with_two_decimal_values(self):
        money = Money(Decimal("3.3"), "EUR") + Money(Decimal("3.3"), "EUR")
        assert money.amount == 6.6

    def test_addition_with_three_instances(self):
        money = Money(1.1, "EUR") + Money(2.2, "EUR") + Money(4.4, "EUR")
        assert money.amount == 7.7

    def test_working_additions(self):
        money = Money(0.01, "BGN") + Money(0.99, "BGN")
        assert money.amount == 1.0
        money = Money(2.22, "BGN") + Money(5.55, "BGN")
        assert money.amount == 7.77
        money = Money(9.99, "BGN") + Money(10.01, "BGN")
        assert money.amount == 20.0
        money = Money(58.50, "GBP") + Money(163.33, "GBP")
        assert money.amount == 221.83
        money = Money(1923, "TRY") + Money(100, "TRY")
        assert money.amount == 2023
        money = Money(13320, "JPY") + Money(1775, "JPY")
        assert money.amount == 15095

    def test_addition_with_invalid_operand(self):
        with pytest.raises(InvalidOperandError):
            Money(2, "EUR") + 2
        with pytest.raises(InvalidOperandError):
            2 + Money(2, "EUR")
        with pytest.raises(InvalidOperandError):
            Money(2, "EUR") + "2"
        with pytest.raises(InvalidOperandError):
            "2" + Money(2, "EUR")
        with pytest.raises(InvalidOperandError):
            Money(2, "EUR") + Decimal("2")
        with pytest.raises(InvalidOperandError):
            Decimal("2") + Money(2, "EUR")
        with pytest.raises(InvalidOperandError):
            Money(2, "EUR") + Currency("EUR")
        with pytest.raises(InvalidOperandError):
            Currency("EUR") + Money(2, "EUR")

    def test_addition_with_currency_mismatch(self):
        with pytest.raises(CurrencyMismatchError):
            Money(2, "EUR") + Money(2, "BGN")
        with pytest.raises(CurrencyMismatchError):
            Money(2, "BGN") + Money(2, "EUR")
        with pytest.raises(CurrencyMismatchError):
            Money(2, "EUR") + Money(2)
        with pytest.raises(CurrencyMismatchError):
            Money(2) + Money(2, "EUR")

    def test_working_additions_without_currency_basics(self):
        money = Money(2) + Money(2)
        assert money.amount == 4
        money = Money(2) + Money(2.2)
        assert money.amount == 4.2
        money = Money(2.2) + Money(2.2)
        assert money.amount == 4.4
        money = Money(2) + Money("2")
        assert money.amount == 4
        money = Money("2") + Money("2")
        assert money.amount == 4
        money = Money(2) + Money("2.2")
        assert money.amount == 4.2
        money = Money("2") + Money("2.2")
        assert money.amount == 4.2
        money = Money(2.2) + Money("2.2")
        assert money.amount == 4.4
        money = Money("2.2") + Money("2.2")
        assert money.amount == 4.4

    def test_working_additions_without_currency_complicated(self):
        money = Money(0.01) + Money(0.99)
        assert money.amount == 1.0
        money = Money(2.22) + Money(5.55)
        assert money.amount == 7.77
        money = Money(9.99) + Money(10.01)
        assert money.amount == 20.0
        money = Money(58.50) + Money(163.33)
        assert money.amount == 221.83
        money = Money(1923) + Money(100)
        assert money.amount == 2023
        money = Money(13320) + Money(1775)
        assert money.amount == 15095
