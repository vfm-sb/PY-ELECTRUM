"""
Tests for FMoney Helpers
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


class TestFMoneyHelpers:

    def test_fmoney_to_money_default(self):
        print("Rounding Model is", FMoney.rounding)
        print("Precision is", FMoney.precision)

        fmoney = FMoney(26.991, "EUR")
        money = fmoney.to_money()
        assert money.amount == 26.99
        assert money.currency == Currency("EUR")
        fmoney = FMoney(1.9515, "BGN")
        money = fmoney.to_money()
        assert money.amount == 1.95
        fmoney = FMoney(99.997, "USD")
        money = fmoney.to_money()
        assert money.amount == 100

    def test_fmoney_to_money_rounding_down(self):
        assert FMoney.rounding is None
        FMoney.rounding = "down"
        fmoney = FMoney(26.991, "EUR")
        money = fmoney.to_money()
        assert money.amount == 26.99
        assert money.currency == Currency("EUR")
        fmoney = FMoney(1.9515, "BGN")
        money = fmoney.to_money()
        assert money.amount == 1.95
        fmoney = FMoney(99.997, "USD")
        money = fmoney.to_money()
        assert money.amount == 99.99

    def test_fmoney_to_money_rounding_up(self):
        FMoney.rounding = "up"
        fmoney = FMoney(26.991, "EUR")
        money = fmoney.to_money()
        assert money.amount == 27
        assert money.currency == Currency("EUR")
        fmoney = FMoney(1.9515, "BGN")
        money = fmoney.to_money()
        assert money.amount == 1.96
        fmoney = FMoney(99.997, "USD")
        money = fmoney.to_money()
        assert money.amount == 100
