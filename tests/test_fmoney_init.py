"""
Tests for FMoney Initializations
"""

# Third-Party Modules
import pytest

# Local Modules
from electrum import FMoney, Currency
from electrum.exceptions import CurrencyNotFoundError
from electrum.exceptions import InvalidAmountError


@pytest.fixture(autouse=True)
def reset_fmoney_settings():
    original_rounding = FMoney.rounding
    original_precision = FMoney.precision
    yield
    FMoney.rounding = original_rounding
    FMoney.precision = original_precision


class TestFMoneyInit:

    def test_init_default(self):
        fmoney = FMoney(2, "EUR")
        assert fmoney.amount == 2
        assert fmoney.currency == Currency("EUR")
        fmoney = FMoney(0.999, "USD")
        assert fmoney.amount == 0.999
        fmoney = FMoney(1.9515, "BGN")
        assert fmoney.amount == 1.9515

    def test_init_with_currency_lowercase(self):
        fmoney = FMoney(2, "eur")
        assert fmoney.currency == Currency("EUR")

    def test_init_with_currency_mixcase(self):
        fmoney = FMoney(2, "EuR")
        assert fmoney.currency == Currency("EUR")

    def test_init_with_currency_numeric_default(self):
        fmoney = FMoney(2, 978)
        assert fmoney.currency == Currency("EUR")

    def test_init_with_currency_numeric_string(self):
        fmoney = FMoney(2, "978")
        assert fmoney.currency == Currency("EUR")

    def test_init_with_currency_not_found(self):
        with pytest.raises(CurrencyNotFoundError):
            FMoney(200, "DEM")
        with pytest.raises(CurrencyNotFoundError):
            FMoney(1000, "BGL")
        with pytest.raises(CurrencyNotFoundError):
            FMoney(1_350_000, "TRL")
        with pytest.raises(CurrencyNotFoundError):
            FMoney(200, "276")
        with pytest.raises(CurrencyNotFoundError):
            FMoney(1000, "100")
        with pytest.raises(CurrencyNotFoundError):
            FMoney(1_350_000, "792")
        with pytest.raises(CurrencyNotFoundError):
            FMoney(200, Currency("DEM"))
        with pytest.raises(CurrencyNotFoundError):
            FMoney(1000, Currency("BGL"))
        with pytest.raises(CurrencyNotFoundError):
            FMoney(1_350_000, Currency("TRL"))

    def test_init_with_invalid_amount(self):
        with pytest.raises(InvalidAmountError):
            FMoney("x", "EUR")
        with pytest.raises(InvalidAmountError):
            FMoney("53K", "BGN")
        with pytest.raises(InvalidAmountError):
            FMoney("100B", "TRY")
