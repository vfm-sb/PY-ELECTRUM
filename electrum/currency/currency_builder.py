# Local Modules
from electrum.currency import CurrencyHelper
# Utilities
from electrum.utils import get_timestamp


class CurrencyBuilderCLI(CurrencyHelper):

    def __init__(self, code: str | int | None = None) -> None:
        super().__init__()
        self.currency_id = self.get_currency_id(code)
        if self.currency_id is None:
            self.currency_id = self.ask_alphabetic_code()
        self.currency_data = self.load_currency_data(self.currency_id)
        if self.currency_exists(self.currency_id):
            self.modify()
        else:
            self.build()
        self.update_currencies()
        self.save_currency_data(self.currency_id, self.currency_data)

    def build(self) -> None:
        print(f"Currency ID (ISO Alphabetic Code): {self.currency_id}")
        print() # Spacer
        self.currency_data["iso-alphabetic"] = self.currency_id
        for key, method in self.input_methods().items():
            if key == "iso-alphabetic":
                continue
            self.currency_data[key] = method()
            print() # Spacer

    def modify(self) -> None:
        print(f"Currency ID (ISO Alphabetic Code): {self.currency_id}")
        print() # Spacer
        for key, method in self.input_methods().items():
            current_value = self.currency_data[key]
            self.currency_data[key] = method(current_value)
            print() # Spacer

    def update_currencies(self) -> None:
        self.currencies[self.currency_id] = {
            "iso-alphabetic": self.currency_data["iso-alphabetic"],
            "iso-numeric": self.currency_data["iso-numeric"],
            "update-date": get_timestamp()
        }
        self.save_currencies()

    def input_methods(self) -> dict:
        return {
            "iso-alphabetic": self.ask_alphabetic_code,
            "iso-numeric": self.ask_numeric_code,
            "name": self.ask_currency_name,
            "base": self.ask_base_unit,
            "denominator": self.ask_denominator,
            "precision": self.ask_precision,
            "unit-name": self.ask_unit_name,
            "unit-plural": self.ask_unit_plural,
            "unit-symbol": self.ask_unit_symbol,
            "unit-symbol-format": self.ask_unit_symbol_format,
            "unit-abbreviation": self.ask_unit_abbreviation,
            "unit-abbreviation-format": self.ask_unit_abbreviation_format,
            "subunit-name": self.ask_subunit_name,
            "subunit-plural": self.ask_subunit_plural,
            "subunit-symbol": self.ask_subunit_symbol,
            "subunit-symbol-format": self.ask_subunit_symbol_format,
            "subunit-abbreviation": self.ask_subunit_abbreviation,
            "subunit-abbreviation-format": self.ask_subunit_abbreviation_format,
            "banknotes": self.ask_banknotes,
            "coins": self.ask_coins,
            "users": self.ask_users,
        }


# Testing
if __name__ == "__main__":
    pass
