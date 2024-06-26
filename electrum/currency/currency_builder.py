# Local Modules
import pyvutils
from ihandler import ihandler
from electrum.currency.currency_helper import CurrencyHelper


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
            "update-date": pyvutils.current_month_stamp()
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
            "default-format": self.ask_default_format,
            "banknotes": self.ask_banknotes,
            "coins": self.ask_coins,
            "users": self.ask_users,
        }

    def ask_alphabetic_code(self, current_code: str | None = None) -> str:
        print(f"{'Enter' if not current_code else 'Change'} Alphabetic Code:")
        if current_code:
            print(f'Current Alphabetic Code is "{current_code}"')
        try:
            alphabetic_code = ihandler(input_type="alphabetic-currency-code")
        except ValueError as error_message:
            print(error_message)
            print()
            return self.ask_alphabetic_code(current_code)
        return alphabetic_code

    def ask_numeric_code(self, current_code: str | None = None) -> str:
        print(f"{'Enter' if not current_code else 'Change'} Numeric Code:")
        if current_code:
            print(f'Current Numeric Code is {current_code}')
        try:
            numeric_code = ihandler(input_type="numeric-currency-code")
        except ValueError as error_message:
            print(error_message)
            print()
            return self.ask_numeric_code(current_code)
        return numeric_code

    def ask_currency_name(self, current_name: str | None = None) -> str:
        print(f"{'Enter' if not current_name else 'Change'} Currency Name:")
        if current_name:
            print(f'Current Currency Name is {current_name}')
        try:
            currency_name = ihandler(input_type="strict-lowercase")
        except ValueError as error_message:
            print(error_message)
            print()
            return self.ask_currency_name(current_name)
        return currency_name

    def ask_base_unit(self, current_base_unit: float | int | None = None) -> float | int:
        print(f"{'Enter' if not current_base_unit else 'Change'} Base Unit:")
        if current_base_unit:
            print(f'Current Currency Base Unit is {current_base_unit}')
        try:
            base_unit = ihandler(input_type="strict-numeric")
        except ValueError as error_message:
            print(error_message)
            print()
            return self.ask_base_unit(current_base_unit)
        return base_unit

    def ask_denominator(self, current_denominator: int | None = None) -> int:
        print(f"{'Enter' if not current_denominator else 'Change'} Denominator Value:")
        if current_denominator:
            print(f'Current Denominator Value is {current_denominator}')
        try:
            denominator = ihandler(input_type="strict-integer")
        except ValueError as error_message:
            print(error_message)
            print()
            return self.ask_denominator(current_denominator)
        return denominator

    def ask_precision(self, current_precision: int | None = None) -> int:
        print(f"{'Enter' if not current_precision else 'Change'} Precision Value:")
        if current_precision:
            print(f'Current Precision Value is {current_precision}')
        try:
            precision = ihandler(input_type="strict-integer")
        except ValueError as error_message:
            print(error_message)
            print()
            return self.ask_precision(current_precision)
        return precision

    def ask_unit_name(self, current_name: str | None = None) -> str:
        print(f"{'Enter' if not current_name else 'Change'} Unit Name:")
        if current_name:
            print(f'Current Unit Name is "{current_name}"')
        try:
            unit_name = ihandler(input_type="strict-lowercase")
        except ValueError as error_message:
            print(error_message)
            print()
            return self.ask_currency_name(current_name)
        return unit_name

    def ask_unit_plural(self, current_plural: str | None = None) -> str | None:
        print(f"{'Enter' if not current_plural else 'Change'} Unit Plural:")
        if current_plural:
            print(f'Current Unit Plural is "{current_plural}"')
        unit_plural = ihandler(input_type="loose-lowercase")
        if unit_plural == "":
            return None
        return unit_plural

    def ask_unit_symbol(self, current_symbol: str | None = None) -> str | None:
        print(f"{'Enter' if not current_symbol else 'Change'} Unit Symbol:")
        if current_symbol:
            print(f'Current Unit Symbol is "{current_symbol}"')
        unit_symbol = ihandler(input_type="unrestricted-string")
        if unit_symbol == "":
            return None
        return unit_symbol

    def ask_unit_symbol_format(self, current_format: str | None = None) -> str | None:
        symbol = self.currency_data["unit-symbol"]
        if symbol is None:
            print(f"Unit Symbol Format:\n> {None}")
            return None
        print("Enter Unit Symbol Format:")
        if current_format:
            print(f'Current Unit Symbol Format is "{current_format}"')
        choices = [f"{symbol}value", f"{symbol} value", f"value{symbol}", f"value {symbol}"]
        CurrencyBuilderCLI.print_format_choices(choices)
        try:
            unit_symbol_format = ihandler(input_type="alphanumeric-choice", choices=choices)
        except ValueError as error_message:
            print(error_message)
            print()
            return self.ask_unit_symbol_format(current_format)
        return unit_symbol_format

    def ask_unit_abbreviation(self, current_abbreviation: str | None = None) -> str | None:
        print(f"{'Enter' if not current_abbreviation else 'Change'} Unit Abbreviation:")
        if current_abbreviation:
            print(f'Current Unit Abbreviation is "{current_abbreviation}"')
        unit_abbreviation = ihandler(input_type="unrestricted-string")
        if unit_abbreviation == "":
            return None
        return unit_abbreviation

    def ask_unit_abbreviation_format(self, current_format: str | None = None) -> str | None:
        abbr = self.currency_data["unit-abbreviation"]
        if abbr is None:
            print(f"Unit Abbreviation Format:\n> {None}")
            return None
        print("Unit Abbreviation Format:")
        if current_format:
            print(f'Current Unit Abbreviation Format is "{current_format}"')
        choices = [f"{abbr}value", f"{abbr} value", f"value{abbr}", f"value {abbr}"]
        CurrencyBuilderCLI.print_format_choices(choices)
        try:
            unit_abbreviation_format = ihandler(input_type="alphanumeric-choice", choices=choices)
        except ValueError as error_message:
            print(error_message)
            print()
            return self.ask_unit_abbreviation_format(current_format)
        return unit_abbreviation_format

    def ask_subunit_name(self, current_name: str | None = None) -> str | None:
        print(f"{'Enter' if not current_name else 'Change'} Subunit Name:")
        if current_name:
            print(f'Current Subunit Name is "{current_name}"')
        try:
            subunit_name = ihandler(input_type="loose-lowercase")
        except ValueError as error_message:
            print(error_message)
            print()
            return self.ask_currency_name(current_name)
        if subunit_name == "":
            return None
        return subunit_name

    def ask_subunit_plural(self, current_plural: str | None = None) -> str | None:
        name = self.currency_data["subunit-name"]
        if name is None:
            print(f"Subunit Plural:\n> {None}")
            return None
        print(f"{'Enter' if not current_plural else 'Change'} Subunit Plural:")
        if current_plural:
            print(f'Current Subunit Plural is "{current_plural}"')
        subunit_plural = ihandler(input_type="loose-lowercase")
        if subunit_plural == "":
            return None
        return subunit_plural

    def ask_subunit_symbol(self, current_symbol: str | None = None) -> str | None:
        print(f"{'Enter' if not current_symbol else 'Change'} Subunit Symbol:")
        if current_symbol:
            print(f'Current Subunit Symbol is "{current_symbol}"')
        subunit_symbol = ihandler(input_type="unrestricted-string")
        if subunit_symbol == "":
            return None
        return subunit_symbol

    def ask_subunit_symbol_format(self, current_format: str | None = None) -> str | None:
        symbol = self.currency_data["subunit-symbol"]
        if symbol is None:
            print(f"Subunit Symbol Format:\n> {None}")
            return None
        print("Enter Subunit Symbol Format:")
        if current_format:
            print(f'Current Subunit Symbol Format is "{current_format}"')
        choices = [f"{symbol}value", f"{symbol} value", f"value{symbol}", f"value {symbol}"]
        CurrencyBuilderCLI.print_format_choices(choices)
        try:
            subunit_symbol_format = ihandler(input_type="alphanumeric-choice", choices=choices)
        except ValueError as error_message:
            print(error_message)
            print()
            return self.ask_unit_symbol_format(current_format)
        return subunit_symbol_format

    def ask_subunit_abbreviation(self, current_abbreviation: str | None = None) -> str | None:
        print(f"{'Enter' if not current_abbreviation else 'Change'} Subunit Abbreviation:")
        if current_abbreviation:
            print(f'Current Subunit Abbreviation is "{current_abbreviation}"')
        subunit_abbreviation = ihandler(input_type="unrestricted-string")
        if subunit_abbreviation == "":
            return None
        return subunit_abbreviation

    def ask_subunit_abbreviation_format(self, current_format: str | None = None) -> str | None:
        abbr = self.currency_data["subunit-abbreviation"]
        if abbr is None:
            print(f"Subunit Abbreviation Format:\n> {None}")
            return None
        print("Enter Subunit Abbreviation Format:")
        if current_format:
            print(f'Current Subunit Abbreviation Format is "{current_format}"')
        choices = [f"{abbr}value", f"{abbr} value", f"value{abbr}", f"value {abbr}"]
        CurrencyBuilderCLI.print_format_choices(choices)
        try:
            subunit_abbreviation_format = ihandler(input_type="alphanumeric-choice", choices=choices)
        except ValueError as error_message:
            print(error_message)
            print()
            return self.ask_subunit_abbreviation_format(current_format)
        return subunit_abbreviation_format

    def ask_default_format(self, current_default: str | None = None) -> str:
        print("Enter Default Format:")
        if current_default:
            print(f'Currency Default Format is "{current_default}"')
        choices = ["code", "name", "symbol", "abbr"]
        CurrencyBuilderCLI.print_format_choices(choices)
        try:
            default_format = ihandler(input_type="alphanumeric-choice", choices=choices)
        except ValueError as error_message:
            print(error_message)
            print()
            return self.ask_default_format(current_default)
        return default_format

    def ask_banknotes(self, current_banknotes: list | None = None) -> list:
        print(f"{'Enter' if not current_banknotes else 'Change'} Banknotes:")
        if current_banknotes:
            print(f'Current Banknotes are {", ".join([str(note) for note in current_banknotes])}')
        try:
            banknotes = ihandler(input_type="multiple-numerics", duplicates=False)
        except ValueError as error_message:
            print(error_message)
            print()
            return self.ask_banknotes(current_banknotes)
        return sorted(banknotes)

    def ask_coins(self, current_coins: list | None = None) -> list:
        print(f"{'Enter' if not current_coins else 'Change'} Coins:")
        if current_coins:
            print(f'Current Coins are {", ".join([str(coin) for coin in current_coins])}')
        try:
            coins = ihandler(input_type="multiple-numerics", duplicates=False)
        except ValueError as error_message:
            print(error_message)
            print()
            return self.ask_coins(current_coins)
        return sorted(coins)

    def ask_users(self, current_users: list | None = None) -> list:
        print(f"{'Enter' if not current_users else 'Change'} Currency Users:")
        if current_users:
            text = "Users are" if len(current_users) > 1 else "User is"
            print(f'Current Currency {text} {", ".join(current_users)}')
        try:
            users = ihandler(input_type="multiple-strings", duplicates=False)
        except ValueError as error_message:
            print(error_message)
            print()
            return self.ask_users(current_users)
        return sorted(users)

    @staticmethod
    def print_format_choices(choices: list) -> None:
        formatted_choices = []
        for index, choice in enumerate(choices):
            formatted_choice = f'({index + 1}) {choice.replace("value", "1")}'
            formatted_choices.append(formatted_choice)
        print(" | ".join(formatted_choices))


# Testing
if __name__ == "__main__":
    pass
