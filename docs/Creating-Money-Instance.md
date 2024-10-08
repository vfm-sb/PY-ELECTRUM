# Creating Money Instance

The `Money` Class can be instantiated in various ways.

(In Version 1) `Money` Class accepts two arguments; `amount` and `currency`.

The `amount` represents the amount of a money instance.
- `amount` value can be an *Integer* value.
- `amount` value can be a *Float* value.
- `amount` value can be a *Numeric String* value.
- `amount` value can be a valid *Decimal* value.

The `currency` represents the `Currency` of a money instance.
- `currency` value can be a *String* value.
    - ISO Alphabetic Code
    - ISO Numeric Code
- `currency` value can be an *Integer* value.
    - ISO Numeric Code (Excepts ISO Numeric Codes Start with *0* or *00*)
- `currency` value can be a `Currency` instance.

## Rules

- The `amount` value should adhere to the appropriate **decimal precision** specified for the given currency.


## Money Object Varieties

### `Money(amount, currency_object)`

```python
>>> eur = Currency("EUR")
>>> money = Money(1, eur)
```

```python
>>> eur = Currency(978)
>>> money = Money(1, eur)
```

```python
>>> eur = Currency("978")
>>> money = Money(1, eur)
```

### `Money(amount, iso_alphabetic_code)`

```python
>>> Money(1, "EUR")
```

```python
>>> Money(10, "BGN")
```

```python
>>> Money(100, "TRY")
```

```python
>>> Money(1000, "JPY")
```


### `Money(amount, iso_numeric_code)`

**ISO Numeric Code** can be `int` or `str`.
> As Long as ISO Numeric Code Doesn't Start with *0* or *00*

**ISO Numeric Code (int)**

```python
>>> Money(1000, 392) # 392 is equal to "JPY"
```

```python
>>> Money(100, 949) # 949 is equal to "TRY"
```

```python
>>> Money(10, 975) # 975 is equal to "BGN"
```

```python
>>> Money(1, 978) # 978 is equal to "EUR"
```

**ISO Numeric Code (str)**

```python
>>> Money(1000, "392") # "392" is equal to "JPY"
```

```python
>>> Money(100, "949") # "949" is equal to "TRY"
```

```python
>>> Money(10, "975") # "975" is equal to "BGN"
```

```python
>>> Money(1, "978") # "978" is equal to "EUR"
```

**ISO Numeric Code (str-Only Exceptions)**

If Currency's ISO Numeric Code Starts with *0* or *00*, The Argument Must Be `str`
> Arguments like `008`  or `032`, etc. will raise `InvalidCurrencyError`


```python
>>> Money(5000, "008") # Albanian Lek (ALL)
```

```python
>>> Money(1_000_000, "032") # Argentinian Peso (ARS)
```

<br>

## Money `amount` Value Varieties


### Integer

```python
>>> Money(1, "EUR")
```

```python
>>> Money(10, "BGN")
```

```python
>>> Money(100, "TRY")
```


### Float

```python
>>> Money(19.92, "EUR")
```

```python
>>> Money(20.23, "BGN")
```

```python
>>> Money(88.88, "TRY")
```


### String

```python
>>> Money("1", "EUR")
```

```python
>>> Money("10", "BGN")
```

```python
>>> Money("100", "TRY")
```

```python
>>> Money("19.92", "EUR")
```

```python
>>> Money("20.23", "BGN")
```

```python
>>> Money("88.88", "TRY")
```


### Decimal

```python
>>> Money(Decimal(1), "EUR")
```

```python
>>> Money(Decimal("1"), "EUR")
```

```python
>>> Money(Decimal(19.92), "EUR")
```

```python
>>> Money(Decimal("19.92"), "EUR")
```



## Money `currency` Value Varieties

### String (Recommended)

```python
>>> Money(1, "EUR")
```

```python
>>> Money(1, "eur")
```

```python
>>> Money(1, "Eur")
```

```python
>>> Money(1, "978")
```


### Integer

```python
>>> Money(1, 978)
```

```python
>>> Money(10, 975)
```

```python
>>> Money(100, 949)
```

```python
>>> Money(1000, 392)
```


### `Currency`

```python
>>> Money(1, Currency("EUR"))
```

```python
>>> Money(1, Currency(978))
```

```python
>>> Money(1, Currency("978"))
```

```python
>>> eur = Currency("EUR")
>>> Money(1, eur)
```

```python
>>> eur = Currency(978)
>>> Money(1, eur)
```

```python
>>> eur = Currency("978")
>>> Money(1, eur)
```

