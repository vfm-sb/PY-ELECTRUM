# PY-ELECTRUM Development History



## 0.2.2 (2024/01/31)

- Electrum is now using `pathlib.Path` instead of Strings.

## 0.2.1 (2024/01/29)

- Bugfix: `Coin`, `Note/Banknote`, `Cash` Objects are Now Functional.
    - A `CurrencyBuilderCLI` Bug Caused Banknote and Coin Values To Be Stored in Strings.
- `Money` Object and its Subclasses are Now Represented Correctly.

## 0.2.0 (2024/01/28)

- All Arithmetic Calculations are now Made Using `Decimal` module.

## 0.1.2 (2024/01/23)

- Bugfix: `InvalidAmountError` Not Raised.

## 0.1.1 (2024/01/22)

- Initial Running Version.
- Available for Limited Use.
- `Money` with Limited Use.
- Initial Version of `Currency` with its Helpers.
- Currently initializing a `Money` object requires `currency` argument.
- Currently only supports a limited number of currencies.
    - EUR, USD, GBP, JPY, BGN, TRY
- Support for Coin, Note/Banknote, Cash (Money-Based Classes).
- Contains a Basic Currency Builder for CLI.
