# PY-ELECTRUM README

> For **Py-Electrum v0.3.x**

The **Py-Electrum** is a Monetary Operations Library for Python Users and Developers.

## About

In the **Py-Electrum**, `Money`, `Coin`, `Note`/`Banknote`, `Cash` and `Currency` are represented true to their real-world standards, accounting for both real-world limitations and limitations of the real-world.


## Getting Started

### Prerequisites

- **pip**: [How to Install pip](https://pip.pypa.io/en/stable/installation/)

### Installation

```
pip install electrum
```

## Usage

### Importing `electrum`

**`electrum` Library Hierarchy**:

```
electrum
│
├── Money
├── FMoney
│
├── Coin
├── Note
├── Banknote
├── Cash
│
├── Currency
└── CurrencyBuilderCLI
```

```python
import electrum
```

```python
from electrum import Money
```

```python
from electrum import Currency
```

```python
from electrum import Coin, Note, Banknote, Cash
```

```python
from electrum import FMoney
```


### Creating `Money` Instances

[Detailed Version Money Instance Creation](https://github.com/vfm-sb/PY-ELECTRUM/blob/main/docs/Creating-Money-Instance.md)

A `Money` instance can be created in various ways.

`Money` Class accepts two arguments; `amount` and `currency`.

The `amount` value can be either an Integer, Float, Numeric String or Decimal value. The `amount` value should also adhere to the appropriate **decimal precision** limit for the given currency.

The `currency` value can be either a valid currency identifier code or a valid `Currency` object. Currency identifier code is either an *ISO Alphabetic Code* or *ISO Numeric Code*.

**Recommended Way**:

- Use Integer or Float as the `amount` value ([See Other Valid Amount Values](https://github.com/vfm-sb/PY-ELECTRUM/blob/main/docs/Valid-Amount-Values.md))
- Use ISO Alphabetic Code (String) as the `currency` value ([See Other Valid Currency Values](https://github.com/vfm-sb/PY-ELECTRUM/blob/main/docs/Valid-Currency-Values.md))

```python
money = Money(2, "EUR")
another = Money(2.2, "EUR")
```

### Creating `FMoney` Instance

An `FMoney` instance can be created the same way as `Money` type objects. The only difference is the `amount` value doesn't adhere to the Currency-based decimal precision limit.

> The default precision limit is **6** but not enforced during instantiation.
> The default rounding model is `None`

```python
fmoney = FMoney(2.999, "USD")
another = FMoney(1.9515, "BGN")
```

### `Cash`, `Coin` and `Note`/`Banknote` Classes

In addition to `Money`, Py-Electrum also contains `Coin`, `Note`/ `Banknote` and `Cash` classes that represent real-world **Coin**, **Banknote** and **Cash** concepts.

- A `Coin` object can only be instantiated with the predefined subunits of the given currency.
- A `Note` or`Banknote` object can only be instantiated with the predefined units of the given currency.
    - The `Note` and `Banknote` classes are identical; the choice between them is a matter of user preference.
- `Cash` objects are combination of `Coin` and `Banknote` objects. They can be instantiated both with predefined unit and subunit values of the given currency.

```python
>>> Coin(0.01, "EUR")
>>> Coin(2, "EUR")

>>> Note(5, "EUR")
>>> Note(100, "EUR")
>>> Banknote(100, "USD")

>>> Cash(0.01, "EUR")
>>> Cash(100, "EUR")
```


## Documentation

### String Representation of `Money` Objects

Money objects can be represented in various ways:
- Default Representation >> `str(money_obj)`
- Code-Based Representation >> `money_obj.code_format()`
- Name-Based Representation >> `money_obj.name_format()`
- Symbol-Based Representation >> `money_obj.symbol_format()`
- Abbreviation-Based Representation >> `money_obj.abbr_format()`


## Roadmap

## Contributing

## Licence

## Contact

## Acknowledgements

