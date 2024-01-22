# Built-in Modules
import string

# Local Modules
from electrum.currency.currency_helper import CurrencyHelper

# Utilities
from electrum.utils import assert_input
from electrum.utils import get_numeric_value, get_integer_value
from electrum.utils import split_by_comma

# Exceptions
from electrum.exceptions import InvalidInputTypeError


class InputHandler:

    def __init__(self, input_type: str, prompt: str = "> ", **kwargs) -> None:
        self.input_type = input_type
        self.prompt = prompt
        self.input_method = self.get_input_method()
        self._data = self.input_method(**kwargs)

    @property
    def output(self):
        return self._data

    def get_input_method(self) -> None:
        input_types = {
            "strict-string": self.strict_string,
            "loose-string": self.loose_string,
            "unrestricted-string": self.unrestricted_string,
            "lower-string": self.lower_string,
            "upper-string": self.upper_string,
            "multiple-strings": self.multiple_strings,
            "choice": self.choice,
            "numeric": self.numeric,
            "integer": self.integer,
            "loose-numeric": self.loose_numeric,
            "loose-integer": self.loose_integer,
            "multiple-numerics": self.multiple_numerics,
            "currency-code": self.currency_code,
            "iso-alphabetic": self.alphabetic_currency_code,
            "iso-numeric": self.numeric_currency_code,
        }
        if self.input_type not in input_types:
            raise InvalidInputTypeError
        return input_types[self.input_type]

    def _string_input(self, *args) -> str:
        user_input = input(self.prompt)
        if "assert" in args:
            assert_input(user_input) # MissingInputError
        if "strip" in args:
            user_input = user_input.strip()
        if "lower" in args:
            user_input = user_input.lower()
        elif "upper" in args:
            user_input = user_input.upper()
        return user_input

    def strict_string(self) -> str:
        return self._string_input("assert", "strip")

    def loose_string(self) -> str:
        return self._string_input("lower")

    def unrestricted_string(self) -> str:
        return self._string_input()

    def lower_string(self) -> str:
        return self._string_input("assert", "strip", "lower")

    def upper_string(self) -> str:
        return self._string_input("assert", "strip", "upper")

    def multiple_strings(self, exit_keywords: list | None = None, duplicates: bool = True) -> list:
        if not exit_keywords:
            exit_keywords = ["done", "exit", "eol"]
        strings = []
        while True:
            user_input = self.lower_string()
            if user_input in exit_keywords:
                break
            if "," in user_input:
                input_values = split_by_comma(user_input)
                strings.extend(input_values)
            else:
                strings.append(user_input)
        if not duplicates:
            strings = list(set(strings))
        return strings

    def choice(self, choices: list) -> str:
        user_choice = self.loose_integer()
        integer_options = list(range(1, len(choices) + 1))
        lowercase_options = list(string.ascii_lowercase[:len(choices)])
        uppercase_options = list(string.ascii_uppercase[:len(choices)])
        valid_options = [choices, integer_options, lowercase_options, uppercase_options]
        for option_group in valid_options:
            for option, choice in zip(option_group, choices):
                if user_choice == option:
                    return choice
        raise ValueError(f'Invalid Choice >> "{user_choice}"')

    def numeric(self) -> int | float:
        user_input = self._string_input("assert", "strip")
        return get_numeric_value(input_string=user_input)

    def integer(self) -> int:
        user_input = self._string_input("assert", "strip")
        return get_integer_value(user_input)

    def loose_numeric(self) -> int | float | str:
        user_input = self._string_input("assert", "strip")
        try:
            return get_numeric_value(input_string=user_input)
        except ValueError:
            return user_input

    def loose_integer(self) -> int | str:
        user_input = self._string_input("assert", "strip")
        try:
            return get_integer_value(input_string=user_input)
        except ValueError:
            return user_input

    def multiple_numerics(self, exit_keywords: list | None = None, duplicates: bool = True) -> list:
        if not exit_keywords:
            exit_keywords = ["done", "exit", "eol"]
        numeric_values = []
        while True:
            user_input = self.loose_numeric()
            if user_input in exit_keywords:
                break
            if "," in user_input:
                input_values = split_by_comma(user_input)
                numeric_values.extend(input_values)
            else:
                numeric_values.append(user_input)
        if not duplicates:
            numeric_values = list(set(numeric_values))
        return numeric_values

    def currency_code(self) -> str:
        user_input = self.upper_string()
        CurrencyHelper.assert_currency_code(user_input) # InvalidCurrencyCodeError
        return user_input

    def alphabetic_currency_code(self) -> str:
        user_input = self.upper_string()
        CurrencyHelper.assert_alphabetic_code(user_input) # InvalidCurrencyCodeError
        return user_input

    def numeric_currency_code(self) -> str:
        user_input = self.strict_string()
        CurrencyHelper.assert_numeric_code(user_input) # InvalidCurrencyCodeError
        return user_input


# Testing
if __name__ == "__main__":
    pass
