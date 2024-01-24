# Built-in Modules
from decimal import Decimal

# Custom Utilities
from .converter_utils import convert_numeric_string
from .converter_utils import convert_decimal


def parse_numeric_value(value: int | float | str | Decimal) -> int | float:
    if isinstance(value, str):
        return convert_numeric_string(value=value)
    if isinstance(value, Decimal):
        return convert_decimal(value)
    if not isinstance(value, (int, float)):
        raise ValueError(f"Invalid Numeric Value >> {value}")
    return value
