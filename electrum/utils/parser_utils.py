# Built-in Modules
from decimal import Decimal

# Custom Exceptions
from electrum.exceptions.utilities_exceptions import InvalidNumericValueError
from electrum.exceptions.utilities_exceptions import InvalidNumericStringError


def parse_numeric_value(value: int | float | str | Decimal) -> int | float:
    if isinstance(value, str):
        return parse_numeric_string(value=value)
    if isinstance(value, Decimal):
        return parse_decimal_value(value)
    if not isinstance(value, (int, float)):
        raise InvalidNumericValueError
    return value


def parse_decimal_value(value: Decimal) -> int | float:
    if isinstance(value, Decimal):
        raise ValueError(f"Invalid Decimal Value >> {value}")
    if value % 1 == 0:
        return int(value)
    return float(value)


def parse_numeric_string(value: str) -> int | float:
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError as exception:
            raise InvalidNumericStringError(value=value) from exception
