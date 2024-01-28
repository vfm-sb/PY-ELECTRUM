# Modulo Division

| Object 1 | Operator | Object 2 | Result | Validity |
| :--: | :--: | :--: | :--: | :--: |
| Money(XYZ) | % | Money(XYZ) | Int or Float | Valid |
| Money(XYZ) | % | Int or Float | Money(XYZ) | Valid |
| Money(XYZ) | % | Numeric String | Money(XYZ) | Valid |
| Money(XYZ) | % | Decimal | Money(XYZ) | Valid |
| Money(XYZ) | % | Money(ABC) | CurrencyMismatchError | Invalid |
| Money(ABC) | % | Money(XYZ) | CurrencyMismatchError | Invalid |
| Money(XYZ) | % | Other Object | InvalidOperandError | Invalid |


## `Money(amount=x, currency="XYZ) % Money(amount=y, currency="XYZ)`

A `Money` object with a `currency` argument can be divided by another `Money` object with the same `Currency`.

> A `Money` object can also be divided by an **Integer**, **Float**, valid **Numeric String** or valid **Decimal** value.

When the divisor is another `Money` object with the same `Currency`, a Valid Modulo Operation will return either an Integer or a Float value.

**Note**: Money object's `amount` argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object **cannot** perform modulo operation with any value other than an object of *Money Type* or a *Numeric Type*.

**Note**: Money object's `currency` argument must be a valid value! (See VALID CURRENCY VALUES) & (See VALID CURRENCIES)

### Valid Examples

```python
>>> Money(amount=3, "EUR") % Money(amount=2, "EUR")
>>> 1
```

```python
>>> Money(3, "EUR") % Money(2, "EUR")
>>> 1
```

```python
>>> Money("3", "EUR") % Money(2, "EUR")
>>> 1
```

```python
>>> Money(3, "EUR") % Money("2", "EUR")
>>> 1
```

```python
>>> Money("3", "EUR") % Money("2", "EUR")
>>> 1
```

### Invalid Examples

```python
>>> Money(2, "EUR") % Other("2")
>>> InvalidOperandError
```


## `Money(amount=x, currency="XYZ) % value`

A `Money` object with a `Currency` value can be divided by an **Integer**, **Float**, valid **Numeric String** or valid **Decimal** value.

> A `Money` object with a `Currency` value can also be divided by another `Money` object with the same `Currency` value.

When the divisor is a Numeric Value, a Valid Floor Division Operation will return a Money object with the same `Currency` value as the dividend.

**Note**: Money object's `amount` argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object **cannot** perform floor division with any value other than an object of *Money Type* or a *Numeric Type*.

**Note**: Money object's `currency` argument must be a valid value! (See VALID CURRENCY VALUES) & (See VALID CURRENCIES)

### Valid Examples

```python
>>> Money(amount=3, "EUR") % 2
>>> Money(1.0, "EUR")
```

```python
>>> Money(3, "EUR") % 2
>>> Money(1.0, "EUR")
``%
```python
>>> Money(3, "EUR") % "2"
>>> Money(1.0, "EUR")
```

```python
>>> Money("3", "EUR") % 2
>>> Money(1.0, "EUR")
```

```python
>>> Money("3", "EUR") % "2"
>>> Money(1.0, "EUR")
```

### Invalid Examples

```python
>>> Money(2, "EUR") % Money(2, "BGN")
>>> CurrencyMismatchError
```

```python
>>> Money(2, "BGN") % Money(2, "EUR")
>>> CurrencyMismatchError
```

```python
>>> Money(2, "EUR") % Other("2")
>>> InvalidOperandError
```

