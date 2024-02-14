"""
Tests for FMoney Operations
"""

# Third-Party Modules
import pytest

# Local Modules
from electrum import FMoney


@pytest.fixture(autouse=True)
def reset_fmoney_settings():
    original_rounding = FMoney.rounding
    original_precision = FMoney.precision
    yield
    FMoney.rounding = original_rounding
    FMoney.precision = original_precision


class TestFMoneyOperations:

    def test_raw_discount_model(self):
        product_price = FMoney(29.99, "eur")
        discount_rate = 0.1
        discount_amount = product_price * discount_rate
        assert discount_amount.amount == 2.999
        discounted_price = product_price - discount_amount
        assert discounted_price.amount == 26.991

    def test_customer_friendly_discount_model(self):
        product_price = FMoney(29.99, "eur")
        discount_rate = 0.1
        discount_amount = product_price * discount_rate
        assert discount_amount.amount == 2.999
        discounted_price = product_price - discount_amount
        assert discounted_price.amount == 26.991
        true_discounted_price = discounted_price.to_money(rounding="down")
        assert true_discounted_price.amount == 26.99

    def test_store_friendly_discount_model(self):
        product_price = FMoney(29.99, "eur")
        discount_rate = 0.1
        discount_amount = product_price * discount_rate
        assert discount_amount.amount == 2.999
        discounted_price = product_price - discount_amount
        assert discounted_price.amount == 26.991
        true_discounted_price = discounted_price.to_money(rounding="up")
        assert true_discounted_price.amount == 27
