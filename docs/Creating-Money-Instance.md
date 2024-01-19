# Creating Money Instance

The `Money` Class can be initialised in various ways.

(In Version 1) `Money` Class accepts two arguments; `amount` and `currency`.

The `amount` represents the amount of a money instance.
- `amount` value can be an *Integer* value.
- `amount` value can be a *Float* value.
- `amount` value can be a *Numeric String* value.
- `amount` value can be a valid *Decimal* value.

The `currency` argument is **optional**.

If `currency` argument is not provided, a `Money` instance can only interact with other `Money` instances that are without the `currency` argument.

If `currency` argument is given:
- `currency` value can be a *String* value.
    - ISO Alphabetic Code
    - ISO Numeric Code
- `currency` value can be an *Integer* value.
    - ISO Numeric Code (Excepts ISO Numeric Codes Start with *0* or *00*)
- `currency` value can be a `Currency` instance.

## Money Object Varieties

### `Money(value)`

- `Money(1)`
- `Money(9.99)`
- `Money(1_000)`
- `Money("1")`
- `Money("9.99")`
- `Money("1000")`
- `Money(Decimal(1))`
- `Money(Decimal(9.99))`
- `Money(Decimal("1"))`
- `Money(Decimal("9.99"))`

### `Money(value, currency_object)`

```python
money_instance = Money(1, Currency.EUR)
```

```python
eur = Currency("EUR")
money_instance = Money(1, eur)
```

```python
eur = Currency(978)
money_instance = Money(1, eur)
```

```python
eur = Currency("978")
money_instance = Money(1, eur)
```


### `Money(value, iso_alphabetic_code)`

- `Money(1, "EUR")`
- `Money(10, "BGN")`
- `Money(100, "TRY")`
- `Money(1000, "JPY")`

### `Money(value, iso_numeric_code)`

**ISO Numeric Code** can be `int` or `str`.
> As Long as ISO Numeric Code Doesn't Start with *0* or *00*

**ISO Numeric Code (int)**
- `Money(1000, 392) # 392 is equal to "JPY"`
- `Money(100, 949) # 949 is equal to "TRY"`
- `Money(10, 975) # 975 is equal to "BGN"`
- `Money(1, 978) # 978 is equal to "EUR"`

**ISO Numeric Code (str)**
- `Money(1000, "392") # "392" is equal to "JPY"`
- `Money(100, "949") # "949" is equal to "TRY"`
- `Money(10, "975") # "975" is equal to "BGN"`
- `Money(1, "978") # "978" is equal to "EUR"`


#### str-Only Exceptions

If Currency's ISO Numeric Code Starts with *0* or *00*, The Argument Must Be `str`
> Arguments like `008`  or `032`, etc. will raise `InvalidCurrencyError`

- `Money(5000, "008") # Albanian Lek (ALL)`
- `Money(1_000_000, "032") # Argentinian Peso (ARS)`

<br>

## Money `amount` Value Varieties

### Integer

- `Money(1)`
- `Money(1, "EUR")`
- `Money(10, "BGN")`
- `Money(100, "TRY")`

### Float

- `Money(11.11)`
- `Money(19.92, "EUR")`
- `Money(20.23, "BGN")`
- `Money(88.88, "TRY")`

### String

- `Money("1")`
- `Money("1", "EUR")`
- `Money("10", "BGN")`
- `Money("100", "TRY")`
- `Money("11.11")`
- `Money("19.92", "EUR")`
- `Money("20.23", "BGN")`
- `Money("88.88", "TRY")`

### Decimal

- `Money(Decimal(1))`
- `Money(Decimal("1"))`
- `Money(Decimal(11.11))`
- `Money(Decimal("11.11"))`
- `Money(Decimal(1), "EUR")`
- `Money(Decimal("1"), "EUR")`
- `Money(Decimal(19.92), "EUR")`
- `Money(Decimal("19.92"), "EUR")`


## Money `currency` Value Varieties

### String

- `Money(1, "EUR")`
- `Money(1, "eur")`
- `Money(1, "Eur")`
- `Money(1, "978")`

### Integer

- `Money(1, 978)`
- `Money(10, 975)`
- `Money(100, 949)`
- `Money(1000, 392)`

### `Currency`

```python
Money(1, Currency("EUR"))
```

```python
Money(1, Currency(978))
```

```python
Money(1, Currency("978"))
```

```python
eur = Currency("EUR")
Money(1, eur)
```

```python
eur = Currency(978)
Money(1, eur)
```

```python
eur = Currency("978")
Money(1, eur)
```

```python
Money(1, Currency.EUR)
```
