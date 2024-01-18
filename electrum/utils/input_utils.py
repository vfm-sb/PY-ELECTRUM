# Exceptions
from electrum.exceptions import InvalidNumericInputError


def get_numeric_value(input_string: str) -> int | float:
    try:
        return int(input_string)
    except ValueError:
        try:
            return float(input_string)
        except ValueError as exc:
            raise InvalidNumericInputError(input_string) from exc


def get_integer_value(input_string: str) -> int:
    try:
        return int(input_string)
    except ValueError as exc:
        raise InvalidNumericInputError("Invalid Integer Value", input_string) from exc


def split_by_comma(input_string: str) -> list:
    return [part.strip() for part in input_string.split(",")]
