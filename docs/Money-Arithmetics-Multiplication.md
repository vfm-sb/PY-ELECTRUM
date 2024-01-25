# Multiplication

| Object 1 | Operator | Object 2 | Result | Validity |
| :--: | :--: | :--: | :--: | :--: |
| Money(XYZ) | * | Int or Float | Money(XYZ) | Valid |
| Int or Float  | * | Money(XYZ) | Money(XYZ) | Valid |
| Money(XYZ) | * | Numeric String | Money(XYZ) | Valid |
| Numeric String  | * | Money(XYZ) | Money(XYZ) | Valid |
| Money(XYZ) | * | Decimal | Money(XYZ) | Valid |
| Decimal  | * | Money(XYZ) | Money(XYZ) | Valid |
| Money(XYZ) | * | Money(XYZ) | InvalidOperandError | Invalid |
| Money(XYZ) | * | Money(ABC) | InvalidOperandError | Invalid |
| Money(ABC) | * | Money(XYZ) | InvalidOperandError | Invalid |
| Money(XYZ) | * | Other Object | InvalidOperandError | Invalid |
| Other Object | * | Money(XYZ) | InvalidOperandError | Invalid |


## `Money(amount=x, currency="XYZ") * value` or `value * Money(amount=x, currency="XYZ")`

A `Money` object can only be multiplied by an **Integer**, **Float**, valid **Numeric String** or valid **Decimal** value.

The result of a Valid Multiplication Operation will be a `Money` instance with the same `Currency` as the operands.

**Note**: Currencies of Money objects must match!

**Note**: Money object's `amount`argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object **cannot** perform multiplication with a *Non-Numeric Type* object.

**Note**: Money object's `currency` argument must be a valid value! (See VALID CURRENCY VALUES) & (See VALID CURRENCIES)

### Valid Examples

```python
>>> Money(2, "EUR") * 2
>>> Money(4.0, "EUR")
```

```python
>>> 2 * Money(2, "EUR")
>>> Money(4., "EUR")
```

```python
>>> Money(2, "EUR") * 2.2
>>> Money(4.4, "EUR")
```

```python
>>> 2.2 * Money(2, "EUR")
>>> Money(4.4, "EUR")
```

```python
>>> Money(2.2, "EUR") * 2.2
>>> Money(4.84, "EUR")
```

```python
>>> Money(2, "EUR") * "2"
>>> Money(4.0, "EUR")
```

```python
>>> "2" * Money(2, "EUR")
>>> Money(4.0, "EUR")
```

```python
>>> Money("2", "EUR") * 2
>>> Money(4.0, "EUR")
```

```python
>>> 2 * Money("2", "EUR")
>>> Money(4.0, "EUR")
```

```python
>>> Money("2", "EUR") * "2"
>>> Money(4.0, "EUR")
```

```python
>>> "2" * Money("2", "EUR")
>>> Money(4.0, "EUR")
```

```python
>>> Money(2000, "JPY") * 2
>>> Money(4000, "JPY")
```

```python
>>> 2 * Money(2000, "JPY")
>>> Money(4000, "JPY")
```

### Invalid Examples

```python
>>> Money(2, "EUR") * Money(2, "EUR")
>>> InvalidOperandError
```

```python
>>> Money(2, "EUR") * Other("2")
>>> InvalidOperandError
```

```python
>>> Other("2") * Money(2, "EUR")
>>> InvalidOperandError
```

