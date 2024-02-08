"""
Custom Math Utilities
"""

import decimal


def round_down(value: decimal.Decimal, decimals: int) -> decimal.Decimal:
    with decimal.localcontext() as ctx:
        ctx.rounding = decimal.ROUND_DOWN
        return round(value, decimals)


def round_up(value: decimal.Decimal, decimals: int) -> decimal.Decimal:
    with decimal.localcontext() as ctx:
        ctx.rounding = decimal.ROUND_UP
        return round(value, decimals)
