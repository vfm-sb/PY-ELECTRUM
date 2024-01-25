# Money Arithmetics (Full Version)

<br>
<hr>
<br>

## Addition

| Object 1 | Operator | Object 2 | Result | Validity |
| :--: | :--: | :--: | :--: | :--: |
| Money(XYZ) | + | Money(XYZ) | Money(XYZ) | Valid |
| Money(XYZ) | + | Money(ABC) | CurrencyMismatchError | Invalid |
| Money(ABC) | + | Money(XYZ) | CurrencyMismatchError | Invalid |
| Money(XYZ) | + | Int or Float | InvalidOperandError | Invalid |
| Int or Float  | + | Money(XYZ) | InvalidOperandError | Invalid |
| Money(XYZ) | + | Numeric String | InvalidOperandError | Invalid |
| Numeric String  | + | Money(XYZ) | InvalidOperandError | Invalid |
| Money(XYZ) | + | Decimal | InvalidOperandError | Invalid |
| Decimal  | + | Money(XYZ) | InvalidOperandError | Invalid |
| Money(XYZ) | + | Other Object | InvalidOperandError | Invalid |
| Other Object | + | Money(XYZ) | InvalidOperandError | Invalid |


### `Money(amount=x, currency="XYZ") + Money(amount=y, currency="XYZ")`

Two or more `Money` objects of same `Currency` can be added together.

The result of a Valid Addition Operation will be a `Money` instance with the same `Currency` as the operands.

**Note**: Currencies of Money objects must match!

**Note**: Money object's `amount`argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object cannot perform addition with a *Non-Money Type* object.

**Note**: Money object's `currency` argument must be a valid value! (See VALID CURRENCY VALUES) & (See VALID CURRENCIES)

#### Valid Examples

```python
>>> Money(amount=2, currency="EUR") + Money(amount=2, currency="EUR")
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

#### Invalid Examples

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

<br>
<hr>
<br>

## Subtraction

| Object 1 | Operator | Object 2 | Result | Validity |
| :--: | :--: | :--: | :--: | :--: |
| Money(XYZ) | - | Money(XYZ) | Money(XYZ) | Valid |
| Money(XYZ) | - | Money(ABC) | CurrencyMismatchError | Invalid |
| Money(ABC) | - | Money(XYZ) | CurrencyMismatchError | Invalid |
| Money(XYZ) | - | Int or Float | InvalidOperandError | Invalid |
| Int or Float  | - | Money(XYZ) | InvalidOperandError | Invalid |
| Money(XYZ) | - | Numeric String | InvalidOperandError | Invalid |
| Numeric String  | - | Money(XYZ) | InvalidOperandError | Invalid |
| Money(XYZ) | - | Decimal | InvalidOperandError | Invalid |
| Decimal  | - | Money(XYZ) | InvalidOperandError | Invalid |
| Money(XYZ) | - | Other Object | InvalidOperandError | Invalid |
| Other Object | - | Money(XYZ) | InvalidOperandError | Invalid |


### `Money(amount=x, currency="XYZ") - Money(amount=y, currency="XYZ")`

Two or more `Money` objects of same `Currency` can be subtracted from each others.

The result of a Valid Subtraction Operation will be a `Money` instance with the same `Currency` as the operands.

**Note**: Currencies of Money objects must match!

**Note**: Money object's `amount`argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object cannot perform subtraction with a *Non-Money Type* object.

**Note**: Money object's `currency` argument must be a valid value! (See VALID CURRENCY VALUES) & (See VALID CURRENCIES)

#### Valid Examples

```python
>>> Money(amount=4, currency="EUR") - Money(amount=2, currency="EUR")
>>> Money(2.0, "EUR")
```

```python
>>> Money(amount=2, currency="EUR") - Money(amount=4, currency="EUR")
>>> Money(-2.0, "EUR")
```

```python
>>> Money(4, "EUR") - Money(2, "EUR")
>>> Money(2.0, "EUR")
```

```python
>>> Money(2, "EUR") - Money(4, "EUR")
>>> Money(-2.0, "EUR")
```

```python
>>> Money(4, "EUR") - Money(2.2, "EUR")
>>> Money(1.8, "EUR")
```

```python
>>> Money(4.4, "EUR") - Money(2.2, "EUR")
>>> Money(2.2, "EUR")
```

```python
>>> Money(4, "EUR") - Money("2", "EUR")
>>> Money(2.0, "EUR")
```

```python
>>> Money("4", "EUR") - Money(2, "EUR")
>>> Money(2.0, "EUR")
```

```python
>>> Money("4", "EUR") - Money("2", "EUR")
>>> Money(2.0, "EUR")
```

```python
>>> Money(4000, "JPY") - Money(2000, "JPY")
>>> Money(2000, "JPY")
```

#### Invalid Examples

```python
>>> Money(2, "EUR") - Money(2, "BGN")
>>> CurrencyMismatchError
```

```python
>>> Money(2, "BGN") - Money(2, "EUR")
>>> CurrencyMismatchError
```

```python
>>> Money(2, "EUR") - Money(2)
>>> CurrencyMismatchError
```

```python
>>> Money(2) - Money(2, "EUR")
>>> CurrencyMismatchError
```

```python
>>> Money(2, "EUR") - 2
>>> InvalidOperandError
```

```python
>>> 2 - Money(2, "EUR")
>>> InvalidOperandError
```

```python
>>> Money(2, "EUR") - 2.2
>>> InvalidOperandError
```

```python
>>> 2.2 - Money(2, "EUR")
>>> InvalidOperandError
```

```python
>>> Money(2.2, "EUR") - 2.2
>>> InvalidOperandError
```

```python
>>> 2.2 - Money(2.2, "EUR")
>>> InvalidOperandError
```

```python
>>> Money(4, "EUR") - "2"
>>> InvalidOperandError
```

```python
>>> "4" - Money(2, "EUR")
>>> InvalidOperandError
```

```python
>>> Money("4", "EUR") - "2"
>>> InvalidOperandError
```

```python
>>> "4" - Money("2", "EUR")
>>> InvalidOperandError
```

```python
>>> Money(4, "EUR") - Decimal("2")
>>> InvalidOperandError
```

```python
>>> Decimal("4") - Money(2, "EUR")
>>> InvalidOperandError
```

```python
>>> Money(4, "EUR") - Other("2")
>>> InvalidOperandError
```

```python
>>> Other("4") - Money(2, "EUR")
>>> InvalidOperandError
```

<br>
<hr>
<br>

## Multiplication

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


### `Money(amount=x, currency="XYZ") * value` or `value * Money(amount=x, currency="XYZ")`

A `Money` object can only be multiplied by an **Integer**, **Float**, valid **Numeric String** or valid **Decimal** value.

The result of a Valid Multiplication Operation will be a `Money` instance with the same `Currency` as the operands.

**Note**: Currencies of Money objects must match!

**Note**: Money object's `amount`argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object **cannot** perform multiplication with a *Non-Numeric Type* object.

**Note**: Money object's `currency` argument must be a valid value! (See VALID CURRENCY VALUES) & (See VALID CURRENCIES)

#### Valid Examples

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

#### Invalid Examples

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

<br>
<hr>
<br>

## Division

| Object 1 | Operator | Object 2 | Result | Validity |
| :--: | :--: | :--: | :--: | :--: |
| Money(XYZ) | / | Money(XYZ) | Int or Float | Valid |
| Money(XYZ) | / | Int or Float | Money(XYZ) | Valid |
| Int or Float  | / | Money(XYZ) | NotImplementedError | Invalid |
| Money(XYZ) | / | Numeric String | Money(XYZ) | Valid |
| Numeric String  | / | Money(XYZ) | NotImplementedError | Invalid |
| Money(XYZ) | / | Decimal | Money(XYZ) | Valid |
| Decimal  | / | Money(XYZ) | NotImplementedError | Invalid |
| Money(XYZ) | / | Money(ABC) | CurrencyMismatchError | Invalid |
| Money(ABC) | / | Money(XYZ) | CurrencyMismatchError | Invalid |
| Money(XYZ) | / | Other Object | InvalidOperandError | Invalid |
| Other Object | / | Money(XYZ) | NotImplementedError | Invalid |


### `Money(amount=x, currency="XYZ) / Money(amount=y, currency="XYZ)`

A `Money` object with a `currency` argument can be divided by another `Money` object with the same `Currency`.

> A `Money` object can also be divided by an **Integer**, **Float**, valid **Numeric String** or valid **Decimal** value.

When the divisor is another `Money` object with the same `Currency`, a Valid Division Operation will return an Integer or Float value.

**Note**: Money object's `amount` argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object **cannot** perform division with any value other than an object of *Money Type* or a *Numeric Type*.

**Note**: Money object's `currency` argument must be a valid value! (See VALID CURRENCY VALUES) & (See VALID CURRENCIES)

#### Valid Examples

```python
>>> Money(amount=2, "EUR") / Money(amount=2, "EUR")
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

#### Invalid Examples

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


### `Money(amount=x, currency="XYZ) / value`

A `Money` object with a `Currency` value can be divided by an **Integer**, **Float**, valid **Numeric String** or valid **Decimal** value.

> A `Money` object with a `Currency` value can also be divided by another `Money` object with the same `Currency` value.

When the divisor is a Numeric Value, a Valid Division Operation will return a Money object with the same `Currency` value as the dividend.

**Note**: Money object's `amount` argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object **cannot** perform division with any value other than an object of *Money Type* or a *Numeric Type*.

**Note**: Money object's `currency` argument must be a valid value! (See VALID CURRENCY VALUES) & (See VALID CURRENCIES)

#### Valid Examples

```python
>>> Money(amount=2, "EUR") / 2
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

#### Invalid Examples

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

<br>
<hr>
<br>

## Floor Division

| Object 1 | Operator | Object 2 | Result | Validity |
| :--: | :--: | :--: | :--: | :--: |
| Money(XYZ) | // | Money(XYZ) | Int | Valid |
| Money(XYZ) | // | Int or Float | Money(XYZ) | Valid |
| Int or Float  | // | Money(XYZ) | NotImplementedError | Invalid |
| Money(XYZ) | // | Numeric String | Money(XYZ) | Valid |
| Numeric String  | // | Money(XYZ) | NotImplementedError | Invalid |
| Money(XYZ) | // | Decimal | Money(XYZ) | Valid |
| Decimal  | // | Money(XYZ) | NotImplementedError | Invalid |
| Money(XYZ) | // | Money(ABC) | CurrencyMismatchError | Invalid |
| Money(ABC) | // | Money(XYZ) | CurrencyMismatchError | Invalid |
| Money(XYZ) | // | Other Object | InvalidOperandError | Invalid |
| Other Object | // | Money(XYZ) | NotImplementedError | Invalid |


### `Money(amount=x, currency="XYZ) // Money(amount=y, currency="XYZ)`

A `Money` object with a `currency` argument can be divided by another `Money` object with the same `Currency`.

> A `Money` object can also be divided by an **Integer**, **Float**, valid **Numeric String** or valid **Decimal** value.

When the divisor is another `Money` object with the same `Currency`, a Valid Floor Division Operation will return an Integer value.

**Note**: Money object's `amount` argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object **cannot** perform floor division with any value other than an object of *Money Type* or a *Numeric Type*.

**Note**: Money object's `currency` argument must be a valid value! (See VALID CURRENCY VALUES) & (See VALID CURRENCIES)

#### Valid Examples

```python
>>> Money(amount=3, "EUR") // Money(amount=2, "EUR")
>>> 1
```

```python
>>> Money(3, "EUR") // Money(2, "EUR")
>>> 1
```

```python
>>> Money("3", "EUR") // Money(2, "EUR")
>>> 1
```

```python
>>> Money(3, "EUR") // Money("2", "EUR")
>>> 1
```

```python
>>> Money("3", "EUR") // Money("2", "EUR")
>>> 1
```

#### Invalid Examples

```python
>>> 2 // Money(2, "EUR")
>>> NotImplementedError
```

```python
>>> 2.2 // Money(2, "EUR")
>>> NotImplementedError
```

```python
>>> "4" // Money(2, "EUR")
>>> NotImplementedError
```

```python
>>> Money(2, "EUR") // Other("2")
>>> InvalidOperandError
```

```python
>>> Other("2") // Money(2, "EUR")
>>> NotImplementedError
```


### `Money(amount=x, currency="XYZ) // value`

A `Money` object with a `Currency` value can be divided by an **Integer**, **Float**, valid **Numeric String** or valid **Decimal** value.

> A `Money` object with a `Currency` value can also be divided by another `Money` object with the same `Currency` value.

When the divisor is a Numeric Value, a Valid Floor Division Operation will return a Money object with the same `Currency` value as the dividend.

**Note**: Money object's `amount` argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object **cannot** perform floor division with any value other than an object of *Money Type* or a *Numeric Type*.

**Note**: Money object's `currency` argument must be a valid value! (See VALID CURRENCY VALUES) & (See VALID CURRENCIES)

#### Valid Examples

```python
>>> Money(amount=2, "EUR") // 2
>>> Money(1.0, "EUR")
```

```python
>>> Money(2, "EUR") // 2
>>> Money(1.0, "EUR")
```

```python
>>> Money(2, "EUR") // "2"
>>> Money(1.0, "EUR")
```

```python
>>> Money("2", "EUR") // 2
>>> Money(1.0, "EUR")
```

```python
>>> Money("2", "EUR") // "2"
>>> Money(1.0, "EUR")
```

#### Invalid Examples

```python
>>> Money(2, "EUR") // Money(2, "BGN")
>>> CurrencyMismatchError
```

```python
>>> Money(2, "BGN") // Money(2, "EUR")
>>> CurrencyMismatchError
```

```python
>>> Money(2, "EUR") // Money(2)
>>> CurrencyMismatchError
```

```python
>>> Money(2) // Money(2, "EUR")
>>> CurrencyMismatchError
```

```python
>>> 2 // Money(2, "EUR")
>>> NotImplementedError
```

```python
>>> 2.2 // Money(2, "EUR")
>>> NotImplementedError
```

```python
>>> "4" // Money(2, "EUR")
>>> NotImplementedError
```

```python
>>> Money(2, "EUR") // Other("2")
>>> InvalidOperandError
```

```python
>>> Other("2") // Money(2, "EUR")
>>> NotImplementedError
```

<br>
<hr>
<br>

## Modulo Operation

| Object 1 | Operator | Object 2 | Result | Validity |
| :--: | :--: | :--: | :--: | :--: |
| Money(XYZ) | % | Money(XYZ) | Int or Float | Valid |
| Money(XYZ) | % | Int or Float | Money(XYZ) | Valid |
| Int or Float  | % | Money(XYZ) | NotImplementedError | Invalid |
| Money(XYZ) | % | Numeric String | Money(XYZ) | Valid |
| Numeric String  | % | Money(XYZ) | NotImplementedError | Invalid |
| Money(XYZ) | % | Decimal | Money(XYZ) | Valid |
| Decimal  | % | Money(XYZ) | NotImplementedError | Invalid |
| Money(XYZ) | % | Money(ABC) | CurrencyMismatchError | Invalid |
| Money(ABC) | % | Money(XYZ) | CurrencyMismatchError | Invalid |
| Money(XYZ) | % | Other Object | InvalidOperandError | Invalid |
| Other Object | % | Money(XYZ) | NotImplementedError | Invalid |


### `Money(amount=x, currency="XYZ) % Money(amount=y, currency="XYZ)`

A `Money` object with a `currency` argument can be divided by another `Money` object with the same `Currency`.

> A `Money` object can also be divided by an **Integer**, **Float**, valid **Numeric String** or valid **Decimal** value.

When the divisor is another `Money` object with the same `Currency`, a Valid Modulo Operation will return either an Integer or a Float value.

**Note**: Money object's `amount` argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object **cannot** perform modulo operation with any value other than an object of *Money Type* or a *Numeric Type*.

**Note**: Money object's `currency` argument must be a valid value! (See VALID CURRENCY VALUES) & (See VALID CURRENCIES)

#### Valid Examples

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

#### Invalid Examples

```python
>>> 2 % Money(2)
>>> NotImplementedError
```

```python
>>> 2.2 % Money(2)
>>> NotImplementedError
```

```python
>>> "4" % Money(2)
>>> NotImplementedError
```

```python
>>> Money(2) % Other("2")
>>> InvalidOperandError
```

```python
>>> Other("2") % Money(2)
>>> NotImplementedError
```


### `Money(amount=x, currency="XYZ) % value`

A `Money` object with a `Currency` value can be divided by an **Integer**, **Float**, valid **Numeric String** or valid **Decimal** value.

> A `Money` object with a `Currency` value can also be divided by another `Money` object with the same `Currency` value.

When the divisor is a Numeric Value, a Valid Floor Division Operation will return a Money object with the same `Currency` value as the dividend.

**Note**: Money object's `amount` argument must be a valid value! (See VALID AMOUNT VALUES)

A `Money` object accepts either an `int`, `float`, a valid numeric `str`, or a valid `Decimal` value as the `amount` argument.

A `Money` object **cannot** perform floor division with any value other than an object of *Money Type* or a *Numeric Type*.

**Note**: Money object's `currency` argument must be a valid value! (See VALID CURRENCY VALUES) & (See VALID CURRENCIES)

#### Valid Examples

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

#### Invalid Examples

```python
>>> Money(2, "EUR") % Money(2, "BGN")
>>> CurrencyMismatchError
```

```python
>>> Money(2, "BGN") % Money(2, "EUR")
>>> CurrencyMismatchError
```

```python
>>> Money(2, "EUR") % Money(2)
>>> CurrencyMismatchError
```

```python
>>> Money(2) % Money(2, "EUR")
>>> CurrencyMismatchError
```

```python
>>> 2 % Money(2, "EUR")
>>> NotImplementedError
```

```python
>>> 2.2 % Money(2, "EUR")
>>> NotImplementedError
```

```python
>>> "4" % Money(2, "EUR")
>>> NotImplementedError
```

```python
>>> Money(2, "EUR") % Other("2")
>>> InvalidOperandError
```

```python
>>> Other("2") % Money(2, "EUR")
>>> NotImplementedError
```

