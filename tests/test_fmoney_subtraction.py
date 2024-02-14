"""
Tests for FMoney Subtractions
"""

# Third-Party Modules
import pytest

# Local Modules
from electrum import FMoney, Currency


@pytest.fixture(autouse=True)
def reset_fmoney_settings():
    # Save the original values of rounding and precision
    original_rounding = FMoney.rounding
    original_precision = FMoney.precision
    # Yield control to the test
    yield
    # Reset the values after the test
    FMoney.rounding = original_rounding
    FMoney.precision = original_precision


class TestFMoneySubtraction:

    def test_subtraction_default(self):
        fmoney = FMoney(4, "EUR") - FMoney(2, "EUR")
        assert fmoney.amount == 2.0
        assert fmoney.currency == Currency("EUR")
        fmoney = FMoney(2, "EUR") - FMoney(4, "EUR")
        assert fmoney.amount == -2.0

    def test_subtraction_with_precision_3(self):
        print(FMoney.rounding)
        print(FMoney.precision)
        fmoney = FMoney(789.012, "GBP") - FMoney(123.456, "GBP")
        assert fmoney.amount == 665.556

    def test_subtraction_with_precision_4(self):
        fmoney = FMoney(9.8765, "JPY") - FMoney(1.2345, "JPY")
        assert fmoney.amount == 8.642

    def test_subtraction_with_precision_5(self):
        fmoney = FMoney(12.34567, "CAD") - FMoney(98.76543, "CAD")
        assert fmoney.amount == -86.41976

    def test_subtraction_with_precision_6(self):
        fmoney = FMoney(987.654321, "USD") - FMoney(123.456789, "USD")
        assert fmoney.amount == 864.197532

    def test_subtraction_with_default_settings(self):
        fmoney = FMoney(26.991, "EUR") - FMoney(2.999, "EUR")
        assert fmoney.amount == 23.992
        fmoney = FMoney(17.98, "BGN") - FMoney(3.596, "BGN")
        assert fmoney.amount == 14.384
        FMoney.precision = 2
        fmoney = FMoney(17.98, "BGN") - FMoney(3.596, "BGN")
        assert fmoney.amount == 14.38

    def test_subtraction_with_rounding_down_settings(self):
        FMoney.rounding = "down"
        FMoney.precision = 6
        fmoney = FMoney(17.98, "BGN") - FMoney(3.596, "BGN")
        assert fmoney.amount == 14.384
        FMoney.precision = 2
        fmoney = FMoney(17.98, "BGN") - FMoney(3.596, "BGN")
        assert fmoney.amount == 14.38

    def test_subtraction_with_rounding_up_settings(self):
        FMoney.rounding = "up"
        FMoney.precision = 6
        fmoney = FMoney(17.98, "BGN") - FMoney(3.596, "BGN")
        assert fmoney.amount == 14.384
        FMoney.precision = 2
        fmoney = FMoney(17.98, "BGN") - FMoney(3.596, "BGN")
        assert fmoney.amount == 14.39