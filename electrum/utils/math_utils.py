"""
Custom Math Utilities
"""

import decimal


def round_down(value: int | float, decimals: int):
    with decimal.localcontext() as ctx:
        decimal_value = decimal.Decimal(value)
        ctx.rounding = decimal.ROUND_DOWN
        return round(decimal_value, decimals)


def round_up(value: int | float, decimals: int):
    with decimal.localcontext() as ctx:
        decimal_value = decimal.Decimal(value)
        ctx.rounding = decimal.ROUND_UP
        return round(decimal_value, decimals)
