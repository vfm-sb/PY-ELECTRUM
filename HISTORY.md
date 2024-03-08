# PY-ELECTRUM Development History

<br>

## 0.3.6 (2024/03/08)

- Replaced Local Utilities with `pyvutils` Equivalents
- Replaced Local Input Handlers with `ihandler` Equivalents


## 0.3.5 (2024/02/23)

- Initial Beta Checkpoint
- Re-Designed Currency Formatting for `Money`

## 0.3.1 (2024/02/16)

- Various Bugfixes and Improvements
    - Negative Value Formatting
    - Fixed Wrong Assertion Orders

## 0.3.0 (2024/02/11)

- Added `FMoney`
    - Represents Financial Money Module
    - Adjustable Rounding
    - Adjustable Precision
- Class-Based Rounding Added to `Money`

## 0.2.5 (2024/02/07)

- Added Formatted Output Support to Money Objects.
    - Default Money Representation Support
    - Code-Based Formatting: `financialize()` Method
    - Name-Based Formatting: `name_format()` Method
    - Symbol-Based Formatting: `symbolize` Property
    - Abbreviation-Based Formatting: `abbreviate` Property

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
