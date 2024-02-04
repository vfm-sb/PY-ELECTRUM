# PY-ELECTRUM README

> For **Py-Electrum v0.2.x**

The **Py-Electrum** is a Monetary Operations Library for Python Users and Developers.

## About

The **Py-Electrum** represents `Money`, `Coin`, `Note`/`Banknote` and `Cash` objects as they are in the real world.

## Getting Started

### Prerequisites

- **pip**
    [How to Install pip](https://pip.pypa.io/en/stable/installation/)

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
├── Currency
│
├── Coin
├── Note
├── Banknote
├── Cash
│
└── CurrencyBuilderCLI
```

```python
import electrum
```

```python
from electrum import Money
```

```python
from electrum import Money, Currency
```

```python
from electrum import Money, Coin, Note, Cash
```

### Creating `Money` Instance

[Detailed Version Money Instance Creation](https://github.com/vfm-sb/PY-ELECTRUM/blob/main/docs/Creating-Money-Instance.md)

A Money instance can be instantiated in various ways. 

`Money` Class accepts two arguments; `amount` and `currency`. 

The `amount` value can be either an Integer, Float, Numeric String or Decimal value. The `amount` value should also adhere to the appropriate **decimal precision** limit for the given currency.

The `currency` value can be either a valid currency identifier code or a valid `Currency` object. Currency identifier code is either an *ISO Alphabetic Code* or *ISO Numeric Code*.

**Recommended Way**:

```python
money = Money(2, "EUR")
```


## Roadmap

## Contributing

## Licence

## Contact

## Acknowledgements

