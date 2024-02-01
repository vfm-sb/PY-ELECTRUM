"""
Tests for Coin, Note/Banknote, Cash Classes
"""

# Local Modules
from electrum import Money, Coin, Note, Banknote, Cash, Currency


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