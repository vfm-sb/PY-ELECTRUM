"""
Tests for FMoney Additions
"""

# Third-Party Modules
import pytest

# Local Modules
from electrum import FMoney, Currency


@pytest.fixture(autouse=True)
def reset_fmoney_settings():
    original_rounding = FMoney.rounding
    original_precision = FMoney.precision
    yield
    FMoney.rounding = original_rounding
    FMoney.precision = original_precision


class TestFMoneyAddition:

    def test_addition_default(self):
        fmoney = FMoney(2, "EUR") + FMoney(2, "EUR")
        assert fmoney.amount == 4.0
        assert fmoney.currency == Currency("EUR")

    def test_addition_with_precision_3(self):
        fmoney = FMoney(123.456, "GBP") + FMoney(789.012, "GBP")
        assert fmoney.amount == 912.468

    def test_addition_with_precision_4(self):
        fmoney = FMoney(1.2345, "JPY") + FMoney(9.8765, "JPY")
        assert fmoney.amount == 11.111

    def test_addition_with_precision_5(self):
        fmoney = FMoney(98.76543, "CAD") + FMoney(12.34567, "CAD")
        assert fmoney.amount == 111.1111

    def test_addition_with_precision_6(self):
        fmoney = FMoney(123.456789, "USD") + FMoney(987.654321, "USD")
        assert fmoney.amount == 1111.11111

    def test_additions_with_default_settings(self):
        fmoney = FMoney(26.991, "EUR") + FMoney(2.999, "EUR")
        assert fmoney.amount == 29.99
        fmoney = FMoney(17.98, "BGN") + FMoney(3.596, "BGN")
        assert fmoney.amount == 21.576
        FMoney.precision = 2
        fmoney = FMoney(17.98, "BGN") + FMoney(3.596, "BGN")
        assert fmoney.amount == 21.58

    def test_addition_with_rounding_down_settings(self):
        FMoney.rounding = "down"
        FMoney.precision = 6
        fmoney = FMoney(17.98, "BGN") + FMoney(3.596, "BGN")
        assert fmoney.amount == 21.576
        FMoney.precision = 2
        fmoney = FMoney(17.98, "BGN") + FMoney(3.596, "BGN")
        assert fmoney.amount == 21.57

    def test_addition_with_rounding_up_settings(self):
        FMoney.rounding = "up"
        FMoney.precision = 6
        fmoney = FMoney(17.98, "BGN") + FMoney(3.596, "BGN")
        assert fmoney.amount == 21.576
        FMoney.precision = 2
        fmoney = FMoney(17.98, "BGN") + FMoney(3.596, "BGN")
        assert fmoney.amount == 21.58
