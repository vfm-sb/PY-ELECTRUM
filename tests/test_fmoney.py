"""
Tests for FMoney Initializations
"""

# Local Modules
from electrum import FMoney, Currency


class TestFMoneyInit:

    def test_init_default(self):
        fmoney = FMoney(2, "EUR")
        assert fmoney.amount == 2
        assert fmoney.currency == Currency("EUR")
        fmoney = FMoney(0.999, "USD")
        assert fmoney.amount == 0.999
        fmoney = FMoney(1.9515, "BGN")
        assert fmoney.amount == 1.9515


class TestFMoneyHelpers:

    def test_fmoney_to_money_default(self):
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
        assert FMoney.rounding is None
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
