# Formatting Money Objects

Money objects can be represented in various ways:
- Default Representation >> `str(money_obj)`
- Code-Based Representation >> `money_obj.code_format()`
- Name-Based Representation >> `money_obj.name_format()`
- Symbol-Based Representation >> `money_obj.symbol_format()`
- Abbreviation-Based Representation >> `money_obj.abbr_format()`


## Default Format

Calling string representation of a Money instance will generate a formatted string based on the corresponding currency's default format.

> Each currency has its own default representation.

```python
>>> money = Money(2, "EUR")

>>> money
>>> Money(2, "EUR")

>>> str(money)
>>> €2
```


## Code Format

Calling `code_format()` method of `Money` class will produce a currency code-based string representation of the Money instance.

Placement of Currency Code can be customized using optional `direction` parameter.
    `ltr` (Default) -> Left to Right -- code on the left, value on the right.
    `rtl` -> Right to Left -- value on the left, code on the right.

```python
>>> money = Money(2, "EUR")

>>> money.code_format()
>>> EUR 2

>>> money.code_format("rtl")
>>> 2 EUR
```


## Name Format

Calling `name_format()` method of `Money` class will produce a name-based string representation of the the Money instance.

```python
>>> money = Money(1, "EUR")
>>> money.name_format()
>>> 1 Euro

>>> money = Money(2, "EUR")
>>> money.name_format()
>>> 2 Euros

>>> money = Money(0.01, "EUR")
>>> money.name_format()
>>> 1 Cent

>>> money = Money(0.02, "EUR")
>>> money.name_format()
>>> 2 Cents
```


## Symbol Format

Calling `symbol_format()` method of `Money` class will produce a symbol-based string representation of the the Money instance.

> If the currency unit or subunit symbol is not available, the corresponding output will automatically default to the abbreviation format.
> If unit and symbol abbreviations aren't available, the output will default to the name format.

```python
>>> money = Money(2, "EUR")
>>> money.symbol_format()
>>> €2

>>> money = Money(0.50, "EUR")
>>> money.symbol_format()
>>> 50c
```

```python
>>> money = Money(100, "USD")
>>> money.symbol_format()
>>> $100

>>> money = Money(0.1, "EUR")
>>> money.symbol_format()
>>> 10¢
```


## Abbreviation Format

Calling `abbr_format()` method of `Money` class will produce a abbreviation-based string representation of the the Money instance.

> If the currency unit or symbol abbreviation isn't available, the corresponding output will automatically default to the symbol format.
> If the currency unit and subunit symbols aren't also available, the output will automatically default to the name format.

```python
>>> money = Money(2, "EUR")
>>> money.abbr_format()
>>> €2

>>> money = Money(0.50, "EUR")
>>> money.abbr_format()
>>> 50c
```

```python
>>> money = Money(200, "TRY")
>>> money.abbr_format()
>>> 200 TL

>>> money = Money(0.25, "TRY")
>>> money.abbr_format()
>>> 50kr.
```

