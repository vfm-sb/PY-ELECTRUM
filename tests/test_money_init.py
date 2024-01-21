# Built-in Modules
from decimal import Decimal

# Local Modules
from electrum import Money, Currency


class TestMoneyInit:

    def test_init_with_currency_default(self):
        money = Money(2, "EUR")
        assert money.amount == 2
        assert money.currency == Currency("EUR")

    def test_init_with_currency_instance_eur(self):
        money = Money(2, Currency("EUR"))
        assert money.currency.alphabetic_code == "EUR"
        assert money.currency.numeric_code == "978"

    def test_init_with_currency_instance_bgn(self):
        money = Money(2, Currency("BGN"))
        assert money.currency.alphabetic_code == "BGN"
        assert money.currency.numeric_code == "975"

    def test_init_with_currency_lowercase(self):
        money = Money(2, "eur")
        assert money.currency == Currency("EUR")

    def test_init_with_currency_mixcase(self):
        money = Money(2, "EuR")
        assert money.currency == Currency("EUR")

    def test_init_with_currency_numeric_default(self):
        money = Money(2, 978)
        assert money.currency == Currency("EUR")

    def test_init_with_currency_numeric_string(self):
        money = Money(2, "978")
        assert money.currency == Currency("EUR")

    def test_init_amount_with_float(self):
        money = Money(2.2, "EUR")
        assert money.amount == 2.2

    def test_init_amount_with_string(self):
        money = Money("4", "EUR")
        assert money.amount == 4

    def test_init_amount_with_decimal_numeric(self):
        money = Money(Decimal(4), "EUR")
        assert money.amount == 4

    def test_init_amount_with_decimal_string(self):
        money = Money(Decimal("4"), "EUR")
        assert money.amount == 4

    def test_init_no_currency_default(self):
        money = Money(2)
        assert money.amount == 2
        assert money.currency is None

    def test_init_no_currency_with_float_amount(self):
        money = Money(2.2)
        assert money.amount == 2.2

    def test_init_no_currency_with_string_amount(self):
        money = Money("4")
        assert money.amount == 4

    def test_init_no_currency_with_decimal_numeric_amount(self):
        money = Money(Decimal(4))
        assert money.amount == 4

    def test_init_no_currency_with_decimal_string_amount(self):
        money = Money(Decimal("4"))
        assert money.amount == 4
