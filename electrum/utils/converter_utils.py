"""
Converter Utils
"""
# Built-in Modules
from decimal import Decimal


def convert_decimal(value: Decimal) -> int | float:
    if value % 1 == 0:
        return int(value)
    return float(value)


def convert_numeric_string(value: str) -> int | float:
    try:
        return int(value)
    except ValueError:
        return float(value)
