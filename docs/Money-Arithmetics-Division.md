# Money Arithmetics: Division

| Object 1 | Operator | Object 2 | Result | Validity |
| :--: | :--: | :--: | :--: | :--: |
| Money | / | Money | Int or Float | Valid |
| Money | / | Int or Float | Money | Valid |
| Int or Float | / | Money | NotImplementedError | Invalid |
| Money | / | Numeric String | Money | Valid |
| Numeric String  | / | Money | NotImplementedError | Invalid |
| Money | / | Decimal | Money | Valid |
| Decimal  | / | Money | NotImplementedError | Invalid |
| Money(XYZ) | / | Money(XYZ) | Int or Float | Valid |
| Money(XYZ) | / | Int or Float | Money(XYZ) | Valid |
| Int or Float  | / | Money(XYZ) | NotImplementedError | Invalid |
| Money(XYZ) | / | Numeric String | Money(XYZ) | Valid |
| Numeric String  | / | Money(XYZ) | NotImplementedError | Invalid |
| Money(XYZ) | / | Decimal | Money(XYZ) | Valid |
| Decimal  | / | Money(XYZ) | NotImplementedError | Invalid |
| Money(XYZ) | / | Money(ABC) | CurrencyMismatchError | Invalid |
| Money(ABC) | / | Money(XYZ) | CurrencyMismatchError | Invalid |
| Money(XYZ) | / | Money | CurrencyMismatchError | Invalid |
| Money | / | Money(XYZ) | CurrencyMismatchError | Invalid |
| Money(XYZ) | / | Other Object | InvalidOperandError | Invalid |
| Other Object | / | Money(XYZ) | NotImplementedError | Invalid |


## `Money(value=x) / Money(value=y)`

A `Money` object without a `currency` argument can be divided by another `Money` object without a `currency` argument.

> A `Money` object can also be divided by an **Integer**, **Float**, valid **Numeric String** or valid **Decimal** value.

When the divisor is another `Money` object without a `Currency` value like the dividend, a Valid Division Operation will return either an Integer or a Float value.

**Note**: Money object's `amount` argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object **cannot** perform division with any value other than an object of *Money Type* or a *Numeric Type*.

### Valid Examples

```python
>>> Money(value=2) / Money(value=2)
>>> 1.0
```

```python
>>> Money(2) / Money(2)
>>> 1.0
```

```python
>>> Money("2") / Money(2)
>>> 1.0
```

```python
>>> Money(2) / Money("2")
>>> 1.0
```

```python
>>> Money("2") / Money("2")
>>> 1.0
```

### Invalid Examples

```python
>>> 2 / Money(2)
>>> NotImplementedError
```

```python
>>> 2.2 / Money(2)
>>> NotImplementedError
```

```python
>>> "4" / Money(2)
>>> NotImplementedError
```

```python
>>> Money(2) / Other("2")
>>> InvalidOperandError
```

```python
>>> Other("2") / Money(2)
>>> NotImplementedError
```


## `Money(value=x, currency="XYZ) / Money(value=y, currency="XYZ)`

A `Money` object with a `currency` argument can be divided by another `Money` object with the same `Currency`.

> A `Money` object can also be divided by an **Integer**, **Float**, valid **Numeric String** or valid **Decimal** value.

When the divisor is another `Money` object with the same `Currency`, a Valid Division Operation will return an Integer or Float value.

**Note**: Money object's `amount` argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object **cannot** perform division with any value other than an object of *Money Type* or a *Numeric Type*.

**Note**: Money object's `currency` argument must be a valid value! (See VALID CURRENCY VALUES) & (See VALID CURRENCIES)

### Valid Examples

```python
>>> Money(value=2, "EUR") / Money(value=2, "EUR")
>>> 1.0
```

```python
>>> Money(2, "EUR") / Money(2, "EUR")
>>> 1.0
```

```python
>>> Money("2", "EUR") / Money(2, "EUR")
>>> 1.0
```

```python
>>> Money(2, "EUR") / Money("2", "EUR")
>>> 1.0
```

```python
>>> Money("2", "EUR") / Money("2", "EUR")
>>> 1.0
```

### Invalid Examples

```python
>>> Money(2, "EUR") / Money(2, "BGN")
>>> CurrencyMismatchError
```

```python
>>> Money(2, "BGN") / Money(2, "EUR")
>>> CurrencyMismatchError
```

```python
>>> Money(2, "EUR") / Money(2)
>>> CurrencyMismatchError
```

```python
>>> Money(2) / Money(2, "EUR")
>>> CurrencyMismatchError
```

```python
>>> 2 / Money(2, "EUR")
>>> NotImplementedError
```

```python
>>> 2.2 / Money(2, "EUR")
>>> NotImplementedError
```

```python
>>> "4" / Money(2, "EUR")
>>> NotImplementedError
```

```python
>>> Money(2, "EUR") / Other("2")
>>> InvalidOperandError
```

```python
>>> Other("2") / Money(2, "EUR")
>>> NotImplementedError
```


## `Money(value=x) / value`

A `Money` object can be divided by an **Integer**, **Float**, valid **Numeric String** or valid **Decimal** value.

> A `Money` object without a `Currency` value can also be divided by another `Money` object without a `Currency` value.

When the divisor is a Numeric Value, a Valid Division Operation will return a Money object without a `Currency` value like the dividend.

**Note**: Money object's `amount` argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object **cannot** perform division with any value other than an object of *Money Type* or a *Numeric Type*.

### Valid Examples

```python
>>> Money(value=2) / 2
>>> Money(1.0)
```

```python
>>> Money(2) / 2
>>> Money(1.0)
```

```python
>>> Money(2) / "2"
>>> Money(1.0)
```

```python
>>> Money("2") / 2
>>> Money(1.0)
```

```python
>>> Money("2") / "2"
>>> Money(1.0)
```

### Invalid Examples

```python
>>> 2 / Money(2)
>>> NotImplementedError
```

```python
>>> 2.2 / Money(2)
>>> NotImplementedError
```

```python
>>> "4" / Money(2)
>>> NotImplementedError
```

```python
>>> Money(2) / Other("2")
>>> InvalidOperandError
```

```python
>>> Other("2") / Money(2)
>>> NotImplementedError
```


## `Money(value=x, currency="XYZ) / value`

A `Money` object with a `Currency` value can be divided by an **Integer**, **Float**, valid **Numeric String** or valid **Decimal** value.

> A `Money` object with a `Currency` value can also be divided by another `Money` object with the same `Currency` value.

When the divisor is a Numeric Value, a Valid Division Operation will return a Money object with the same `Currency` value as the dividend.

**Note**: Money object's `amount` argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object **cannot** perform division with any value other than an object of *Money Type* or a *Numeric Type*.

**Note**: Money object's `currency` argument must be a valid value! (See VALID CURRENCY VALUES) & (See VALID CURRENCIES)

### Valid Examples

```python
>>> Money(value=2, "EUR") / 2
>>> Money(1.0, "EUR")
```

```python
>>> Money(2, "EUR") / 2
>>> Money(1.0, "EUR")
```

```python
>>> Money(2, "EUR") / "2"
>>> Money(1.0, "EUR")
```

```python
>>> Money("2", "EUR") / 2
>>> Money(1.0, "EUR")
```

```python
>>> Money("2", "EUR") / "2"
>>> Money(1.0, "EUR")
```

### Invalid Examples

```python
>>> Money(2, "EUR") / Money(2, "BGN")
>>> CurrencyMismatchError
```

```python
>>> Money(2, "BGN") / Money(2, "EUR")
>>> CurrencyMismatchError
```

```python
>>> Money(2, "EUR") / Money(2)
>>> CurrencyMismatchError
```

```python
>>> Money(2) / Money(2, "EUR")
>>> CurrencyMismatchError
```

```python
>>> 2 / Money(2, "EUR")
>>> NotImplementedError
```

```python
>>> 2.2 / Money(2, "EUR")
>>> NotImplementedError
```

```python
>>> "4" / Money(2, "EUR")
>>> NotImplementedError
```

```python
>>> Money(2, "EUR") / Other("2")
>>> InvalidOperandError
```

```python
>>> Other("2") / Money(2, "EUR")
>>> NotImplementedError
```

