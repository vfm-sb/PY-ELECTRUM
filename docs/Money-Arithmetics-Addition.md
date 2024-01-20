# Money Arithmetics: Addition

| Object 1 | Operator | Object 2 | Result | Validity |
| :--: | :--: | :--: | :--: | :--: |
| Money | + | Money | Money | Valid |
| Money(XYZ) | + | Money(XYZ) | Money(XYZ) | Valid |
| Money(XYZ) | + | Money(ABC) | CurrencyMismatchError | Invalid |
| Money(ABC) | + | Money(XYZ) | CurrencyMismatchError | Invalid |
| Money(XYZ) | + | Money | CurrencyMismatchError | Invalid |
| Money | + | Money(XYZ) | CurrencyMismatchError | Invalid |
| Money(XYZ) | + | Int or Float | InvalidOperandError | Invalid |
| Int or Float  | + | Money(XYZ) | InvalidOperandError | Invalid |
| Money(XYZ) | + | Numeric String | InvalidOperandError | Invalid |
| Numeric String  | + | Money(XYZ) | InvalidOperandError | Invalid |
| Money(XYZ) | + | Decimal | InvalidOperandError | Invalid |
| Decimal  | + | Money(XYZ) | InvalidOperandError | Invalid |
| Money(XYZ) | + | Other Object | InvalidOperandError | Invalid |
| Other Object | + | Money(XYZ) | InvalidOperandError | Invalid |


## `Money(value=x) + Money(value=y)`

Two or More `Money` objects without any `currency` arguments can be added together.

The result of a Valid Addition Operation will be a `Money` instance without `Currency`.

**Note**: Money object's `amount`argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object cannot perform addition with a *Non-Money Type* object.

### Valid Examples

```python
>>> Money(value=2) + Money(value=2)
>>> Money(4.0)
```

```python
>>> Money(2) + Money(2)
>>> Money(4.0)
```

```python
>>> Money(2) + Money(2.2)
>>> Money(4.2)
```

```python
>>> Money(2.2) + Money(2.2)
>>> Money(4.4)
```

```python
>>> Money(2) + Money("2")
>>> Money(4.0)
```

```python
>>> Money("2") + Money(2)
>>> Money(4.0)
```

```python
>>> Money("2") + Money("2")
>>> Money(4.0)
```

```python
>>> Money(1.1) + Money(2.2) + Money(4.4)
>>> Money(7.7)
```

### Invalid Examples

```python
>>> Money(2) + 2
>>> InvalidOperandError
```

```python
>>> 2 + Money(2)
>>> InvalidOperandError
```

```python
>>> Money(2) + 2.2
>>> InvalidOperandError
```

```python
>>> 2.2 + Money(2)
>>> InvalidOperandError
```

```python
>>> Money(2.2) + 2.2
>>> InvalidOperandError
```

```python
>>> 2.2 + Money(2.2)
>>> InvalidOperandError
```

```python
>>> Money(2) + "2"
>>> InvalidOperandError
```

```python
>>> "2" + Money(2)
>>> InvalidOperandError
```

```python
>>> Money("2") + "2"
>>> InvalidOperandError
```

```python
>>> "2" + Money("2")
>>> InvalidOperandError
```

```python
>>> Money(2) + Decimal("2")
>>> InvalidOperandError
```

```python
>>> Decimal("2") + Money(2)
>>> InvalidOperandError
```

```python
>>> Money(2) + Other("2")
>>> InvalidOperandError
```

```python
>>> Other("2") + Money(2)
>>> InvalidOperandError
```


## `Money(value=x, currency="XYZ") + Money(value=y, currency="XYZ")`

Two or more `Money` objects of same `Currency` can be added together.

The result of a Valid Addition Operation will be a `Money` instance with the same `Currency` as the operands.

**Note**: Currencies of Money objects must match!

**Note**: Money object's `amount`argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object cannot perform addition with a *Non-Money Type* object.

**Note**: Money object's `currency` argument must be a valid value! (See VALID CURRENCY VALUES) & (See VALID CURRENCIES)

### Valid Examples

```python
>>> Money(value=2, currency="EUR") + Money(value=2, currency="EUR")
>>> Money(4.0, "EUR")
```

```python
>>> Money(2, "EUR") + Money(2, "EUR")
>>> Money(4.0, "EUR")
```

```python
>>> Money(2, "EUR") + Money(2.2, "EUR")
>>> Money(4.2, "EUR")
```

```python
>>> Money(2.2, "EUR") + Money(2.2, "EUR")
>>> Money(4.4, "EUR")
```

```python
>>> Money(2, "EUR") + Money("2", "EUR")
>>> Money(4.0, "EUR")
```

```python
>>> Money("2", "EUR") + Money(2, "EUR")
>>> Money(4.0, "EUR")
```

```python
>>> Money("2", "EUR") + Money("2", "EUR")
>>> Money(4.0, "EUR")
```

```python
>>> Money(1.1, "EUR") + Money(2.2, "EUR") + Money(4.4, "EUR")
>>> Money(7.7, "EUR")
```

```python
>>> Money(2000, "JPY") + Money(2000, "JPY")
>>> Money(4000, "JPY")
```

### Invalid Examples

```python
>>> Money(2, "EUR") + Money(2, "BGN")
>>> CurrencyMismatchError
```

```python
>>> Money(2, "BGN") + Money(2, "EUR")
>>> CurrencyMismatchError
```

```python
>>> Money(2, "EUR") + Money(2)
>>> CurrencyMismatchError
```

```python
>>> Money(2) + Money(2, "EUR")
>>> CurrencyMismatchError
```

```python
>>> Money(2, "EUR") + 2
>>> InvalidOperandError
```

```python
>>> 2 + Money(2, "EUR")
>>> InvalidOperandError
```

```python
>>> Money(2, "EUR") + 2.2
>>> InvalidOperandError
```

```python
>>> 2.2 + Money(2, "EUR")
>>> InvalidOperandError
```

```python
>>> Money(2.2, "EUR") + 2.2
>>> InvalidOperandError
```

```python
>>> 2.2 + Money(2.2, "EUR")
>>> InvalidOperandError
```

```python
>>> Money(2, "EUR") + "2"
>>> InvalidOperandError
```

```python
>>> "2" + Money(2, "EUR")
>>> InvalidOperandError
```

```python
>>> Money("2", "EUR") + "2"
>>> InvalidOperandError
```

```python
>>> "2" + Money("2", "EUR")
>>> InvalidOperandError
```

```python
>>> Money(2, "EUR") + Decimal("2")
>>> InvalidOperandError
```

```python
>>> Decimal("2") + Money(2, "EUR")
>>> InvalidOperandError
```

```python
>>> Money(2, "EUR") + Other("2")
>>> InvalidOperandError
```

```python
>>> Other("2") + Money(2, "EUR")
>>> InvalidOperandError
```
