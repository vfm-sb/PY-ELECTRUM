"""
Tests for Coin, Note/Banknote, Cash Classes
"""
# pylint: disable=expression-not-assigned

# Built-in Modules
from decimal import Decimal

# Third-Party Modules
import pytest

# Local Modules
from electrum import (
    Money,
    Coin, Note, Banknote, Cash,
    Currency
)
from electrum.exceptions import (
    CurrencyNotFoundError,
    CurrencyMismatchError,
    InvalidOperandError,
)
from electrum.exceptions import (
    InvalidAmountError,
    InvalidCoinValueError,
    InvalidBanknoteValueError,
    InvalidCashValueError
)


class TestCoinNoteCashInit:

    def test_coin_init_default(self):
        coin = Coin(0.01, "EUR")
        assert coin.amount == 0.01
        assert coin.currency == Currency("EUR")
        coin = Coin(0.1, "BGN")
        assert coin.amount == 0.1
        assert coin.currency == Currency("BGN")
        coin = Coin(0.25, "TRY")
        assert coin.amount == 0.25
        assert coin.currency == Currency("TRY")

    def test_note_init_default(self):
        note = Note(5, "EUR")
        assert note.amount == 5.0
        assert note.currency == Currency("EUR")
        banknote = Banknote(10, "BGN")
        assert banknote.amount == 10.0
        assert banknote.currency == Currency("BGN")
        note = Note(20, "TRY")
        assert note.amount == 20.0
        assert note.currency == Currency("TRY")
        banknote = Banknote(50, "GBP")
        assert banknote.amount == 50.0
        assert banknote.currency == Currency("GBP")
        note = Note(100, "USD")
        assert note.amount == 100.0
        assert note.currency == Currency("USD")

    def test_cash_init_default(self):
        cash = Cash(0.01, "EUR")
        assert cash.amount == 0.01
        assert cash.currency == Currency("EUR")
        cash = Cash(0.5, "EUR")
        assert cash.amount == 0.5
        assert cash.currency == Currency("EUR")
        cash = Cash(1, "EUR")
        assert cash.amount == 1.0
        assert cash.currency == Currency("EUR")
        cash = Cash(5, "EUR")
        assert cash.amount == 5.0
        assert cash.currency == Currency("EUR")
        cash = Cash(50, "EUR")
        assert cash.amount == 50.0
        assert cash.currency == Currency("EUR")
        cash = Cash(100, "EUR")
        assert cash.amount == 100.0
        assert cash.currency == Currency("EUR")

    def test_coin_init_with_currency_instance(self):
        coin = Coin(1, Currency("EUR"))
        assert coin.currency.alphabetic_code == "EUR"
        assert coin.currency.numeric_code == "978"

    def test_cash_init_with_currency_instance(self):
        coin = Cash(5, Currency("BGN"))
        assert coin.currency.alphabetic_code == "BGN"
        assert coin.currency.numeric_code == "975"

    def test_note_init_with_currency_instance(self):
        note = Note(20, Currency("TRY"))
        assert note.currency.alphabetic_code == "TRY"
        assert note.currency.numeric_code == "949"

    def test_coin_note_cash_with_numeric_string_amount(self):
        coin = Coin("0.01", "EUR")
        assert coin.amount == 0.01
        note = Note("5", "EUR")
        assert note.amount == 5.0
        cash = Cash("0.01", "EUR")
        assert cash.amount == 0.01
        cash = Cash("20", "EUR")

    def test_coin_note_cash_with_decimal_amount(self):
        coin = Coin(Decimal("0.01"), "EUR")
        assert coin.amount == 0.01
        note = Note(Decimal("5"), "EUR")
        assert note.amount == 5.0
        cash = Cash(Decimal("0.01"), "EUR")
        assert cash.amount == 0.01
        cash = Cash(Decimal("20"), "EUR")

    def test_coin_note_cash_init_with_currency_not_found(self):
        with pytest.raises(CurrencyNotFoundError):
            Coin(0.5, "DEM")
        with pytest.raises(CurrencyNotFoundError):
            Note(1000, "BGL")
        with pytest.raises(CurrencyNotFoundError):
            Cash(1_000_000, "TRL")

    def test_coin_note_cash_init_with_invalid_amount(self):
        with pytest.raises(InvalidAmountError):
            Coin("x", "EUR")
        with pytest.raises(InvalidAmountError):
            Note("53K", "BGN")
        with pytest.raises(InvalidAmountError):
            Cash("100B", "TRY")

    def test_coin_init_with_invalid_amount(self):
        with pytest.raises(InvalidCoinValueError):
            Coin(0.25, "EUR")
        with pytest.raises(InvalidCoinValueError):
            Coin(0.99, "BGN")
        with pytest.raises(InvalidCoinValueError):
            Coin(1.01, "TRY")
        with pytest.raises(InvalidCoinValueError):
            Coin(2.5, "GBP")

    def test_note_init_with_invalid_amount(self):
        with pytest.raises(InvalidBanknoteValueError):
            Note(1, "EUR")
        with pytest.raises(InvalidBanknoteValueError):
            Note(2, "BGN")
        with pytest.raises(InvalidBanknoteValueError):
            Banknote(99, "TRY")
        with pytest.raises(InvalidBanknoteValueError):
            Banknote(100, "GBP")

    def test_cash_init_with_invalid_amount(self):
        with pytest.raises(InvalidCashValueError):
            Cash(0.25, "EUR")
        with pytest.raises(InvalidCashValueError):
            Cash(2.5, "BGN")
        with pytest.raises(InvalidCashValueError):
            Cash(25, "TRY")
        with pytest.raises(InvalidCashValueError):
            Cash(100, "GBP")


class TestCoinNoteCashAddition:

    def test_coin_addition_default(self):
        money = Coin(0.01, "EUR") + Coin(0.1, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 0.11
        assert money.currency == Currency("EUR")

    def test_note_addition_default(self):
        money = Note(10, "EUR") + Note(10, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 20.0
        assert money.currency == Currency("EUR")

    def test_cash_addition_default(self):
        money = Cash(0.5, "EUR") + Cash(50, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 50.5
        assert money.currency == Currency("EUR")

    def test_coin_note_cash_addition_default(self):
        money = Coin(0.2, "EUR") + Note(20, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 20.2
        assert money.currency == Currency("EUR")
        money = Coin(0.05, "EUR") + Cash(0.5, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 0.55
        money = Note(20, "EUR") + Cash(50, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 70.0
        money = Coin(1, "EUR") + Note(10, "EUR") + Cash(100, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 111.0

    def test_coin_note_cash_addition_with_money(self):
        money = Coin(0.01, "EUR") + Money(0.99, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 1.0
        assert money.currency == Currency("EUR")
        money = Note(10, "EUR") + Money(1.11, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 11.11
        assert money.currency == Currency("EUR")
        money = Cash(0.05, "EUR") + Money(19.95, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 20.0
        assert money.currency == Currency("EUR")

    def test_coin_note_cash_addition_with_invalid_operand(self):
        with pytest.raises(InvalidOperandError):
            Coin(1, "EUR") + 1
        with pytest.raises(InvalidOperandError):
            1 + Coin(1, "EUR")
        with pytest.raises(InvalidOperandError):
            Note(5, "EUR") + 5
        with pytest.raises(InvalidOperandError):
            5 + Note(5, "EUR")
        with pytest.raises(InvalidOperandError):
            Cash(1, "EUR") + 1
            Cash(5, "EUR") + 5
        with pytest.raises(InvalidOperandError):
            1 + Cash(1, "EUR")
            5 + Cash(5, "EUR")

    def test_coin_note_cash_addition_with_currency_mismatch(self):
        with pytest.raises(CurrencyMismatchError):
            Coin(2, "EUR") + Coin(2, "BGN")
        with pytest.raises(CurrencyMismatchError):
            Note(5, "EUR") + Note(5, "BGN")
        with pytest.raises(CurrencyMismatchError):
            Cash(2, "EUR") + Cash(2, "BGN")
        with pytest.raises(CurrencyMismatchError):
            Cash(5, "BGN") + Cash(5, "EUR")


class TestCoinNoteCashSubtraction:

    def test_coin_subtraction_default(self):
        money = Coin(0.2, "EUR") - Coin(0.1, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 0.1
        assert money.currency == Currency("EUR")

    def test_note_subtraction_default(self):
        money = Note(20, "EUR") - Note(10, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 10.0
        assert money.currency == Currency("EUR")

    def test_cash_subtraction_default(self):
        money = Cash(50, "EUR") - Cash(1, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 49.0
        assert money.currency == Currency("EUR")

    def test_coin_note_cash_subtraction_default(self):
        money = Note(20, "EUR") - Coin(0.02, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 19.98
        assert money.currency == Currency("EUR")
        money = Cash(0.5, "EUR") - Coin(0.01, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 0.49
        money = Note(50, "EUR") - Cash(20, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 30.0
        money = Note(100, "EUR") - Cash(50, "EUR") - Coin(1, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 49.0

    def test_coin_note_cash_subtraction_with_money(self):
        money = Money(0.99, "EUR") - Coin(0.01, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 0.98
        assert money.currency == Currency("EUR")
        money = Note(10, "EUR") - Money(3.99, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 6.01
        assert money.currency == Currency("EUR")
        money = Cash(20, "EUR") - Money(19.95, "EUR")
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 0.05
        assert money.currency == Currency("EUR")

    def test_coin_note_cash_subtraction_with_invalid_operand(self):
        with pytest.raises(InvalidOperandError):
            Coin(1, "EUR") - 1
        with pytest.raises(InvalidOperandError):
            1 - Coin(1, "EUR")
        with pytest.raises(InvalidOperandError):
            Note(5, "EUR") - 5
        with pytest.raises(InvalidOperandError):
            5 - Note(5, "EUR")
        with pytest.raises(InvalidOperandError):
            Cash(1, "EUR") - 1
            Cash(5, "EUR") - 5
        with pytest.raises(InvalidOperandError):
            1 - Cash(1, "EUR")
            5 - Cash(5, "EUR")

    def test_coin_note_cash_subtraction_with_currency_mismatch(self):
        with pytest.raises(CurrencyMismatchError):
            Coin(2, "EUR") - Coin(2, "BGN")
        with pytest.raises(CurrencyMismatchError):
            Coin(2, "BGN") - Coin(2, "EUR")
        with pytest.raises(CurrencyMismatchError):
            Note(5, "EUR") - Note(5, "BGN")
        with pytest.raises(CurrencyMismatchError):
            Note(5, "BGN") - Note(5, "EUR")
        with pytest.raises(CurrencyMismatchError):
            Cash(2, "EUR") - Cash(2, "BGN")
            Cash(5, "EUR") - Cash(5, "BGN")
        with pytest.raises(CurrencyMismatchError):
            Cash(2, "BGN") - Cash(2, "EUR")
            Cash(5, "BGN") - Cash(5, "EUR")


class TestCoinNoteCashMultiplication:

    def test_coin_multiplication_default(self):
        money = Coin(0.01, "EUR") * 5
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 0.05
        assert money.currency == Currency("EUR")

    def test_note_multiplication_default(self):
        money = Note(10, "EUR") * 10
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 100.0
        assert money.currency == Currency("EUR")

    def test_cash_multiplication_default(self):
        money = Cash(50, "EUR") * 20
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 1000.0
        assert money.currency == Currency("EUR")

    def test_coin_note_cash_multiplication_with_invalid_operand(self):
        with pytest.raises(InvalidOperandError):
            Coin(1, "EUR") * Coin(1, "EUR")
        with pytest.raises(InvalidOperandError):
            Note(5, "EUR") * Note(5, "EUR")
        with pytest.raises(InvalidOperandError):
            Cash(1, "EUR") * Cash(1, "EUR")
            Cash(5, "EUR") * Cash(5, "EUR")


class TestCoinNoteCashDivision:

    def test_dividing_coin_by_coin_default(self):
        result = Coin(2, "EUR") / Coin(1, "EUR")
        assert result == 2.0

    def test_dividing_coin_by_numeric_default(self):
        money = Coin(2, "EUR") / 1
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 2.0
        assert money.currency == Currency("EUR")

    def test_dividing_banknote_by_banknote_default(self):
        result = Note(20, "EUR") / Note(10, "EUR")
        assert result == 2.0

    def test_dividing_banknote_by_numeric_default(self):
        money = Note(20, "EUR") / 10
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 2.0
        assert money.currency == Currency("EUR")

    def test_dividing_cash_by_cash_default(self):
        result = Cash(2, "EUR") / Cash(1, "EUR")
        assert result == 2.0
        result = Cash(20, "EUR") / Cash(10, "EUR")
        assert result == 2.0

    def test_dividing_cash_by_numeric_default(self):
        money = Cash(2, "EUR") / 1
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 2.0
        assert money.currency == Currency("EUR")
        money = Cash(20, "EUR") / 10
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 2.0
        assert money.currency == Currency("EUR")

    def test_dividing_coin_note_cash_by_money_default(self):
        result = Coin(1, "EUR") / Money(0.25, "EUR")
        assert result == 4.0
        result = Note(10, "EUR") / Money(2.5, "EUR")
        assert result == 4.0
        result = Cash(1, "EUR") / Money(0.25, "EUR")
        assert result == 4.0
        result = Cash(10, "EUR") / Money(2.5, "EUR")
        assert result == 4.0


class TestCoinNoteCashFloorDivision:

    def test_coin_by_coin_floor_division_default(self):
        result = Coin(2, "EUR") // Coin(1, "EUR")
        assert result == 2.0

    def test_coin_by_numeric_floor_division_default(self):
        money = Coin(2, "EUR") // 1
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 2.0
        assert money.currency == Currency("EUR")

    def test_banknote_by_banknote_floor_division_default(self):
        result = Note(20, "EUR") // Note(10, "EUR")
        assert result == 2.0

    def test_banknote_by_numeric_floor_division_default(self):
        money = Note(20, "EUR") // 10
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 2.0
        assert money.currency == Currency("EUR")

    def test_cash_by_cash_floor_division_default(self):
        result = Cash(2, "EUR") // Cash(1, "EUR")
        assert result == 2.0
        result = Cash(20, "EUR") // Cash(10, "EUR")
        assert result == 2.0

    def test_cash_by_numeric_floor_division_default(self):
        money = Cash(2, "EUR") // 1
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 2.0
        assert money.currency == Currency("EUR")
        money = Cash(20, "EUR") // 10
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 2.0
        assert money.currency == Currency("EUR")

    def test_coin_note_cash_by_money_floor_division_default(self):
        result = Coin(1, "EUR") // Money(0.25, "EUR")
        assert result == 4.0
        result = Note(10, "EUR") // Money(2.5, "EUR")
        assert result == 4.0
        result = Cash(1, "EUR") // Money(0.25, "EUR")
        assert result == 4.0
        result = Cash(10, "EUR") // Money(2.5, "EUR")
        assert result == 4.0


class TestCoinNoteCashModuloDivision:

    def test_coin_by_coin_default(self):
        result = Coin(2, "EUR") % Coin(1, "EUR")
        assert result == 0

    def test_coin_by_numeric_default(self):
        money = Coin(2, "EUR") % 1
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 0
        assert money.currency == Currency("EUR")

    def test_banknote_by_banknote_default(self):
        result = Note(20, "EUR") % Note(10, "EUR")
        assert result == 0

    def test_banknote_by_numeric_default(self):
        money = Note(20, "EUR") % 10
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 0
        assert money.currency == Currency("EUR")

    def test_cash_by_cash_default(self):
        result = Cash(2, "EUR") % Cash(1, "EUR")
        assert result == 0
        result = Cash(20, "EUR") % Cash(10, "EUR")
        assert result == 0

    def test_cash_by_numeric_default(self):
        money = Cash(2, "EUR") % 1
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 0
        assert money.currency == Currency("EUR")
        money = Cash(20, "EUR") % 10
        assert money.__class__.__name__ == 'Money'
        assert money.amount == 0
        assert money.currency == Currency("EUR")

    def test_coin_note_cash_by_money_default(self):
        result = Coin(1, "EUR") % Money(0.3, "EUR")
        assert result == 0.1
        result = Note(10, "EUR") % Money(3, "EUR")
        assert result == 1.0
        result = Cash(1, "EUR") % Money(0.3, "EUR")
        assert result == 0.1
        result = Cash(10, "EUR") % Money(3, "EUR")
        assert result == 1.0
