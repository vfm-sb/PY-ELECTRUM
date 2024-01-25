# Valid Currency Values

- `currency` value can be a *String* value.
    - ISO Alphabetic Code
    - ISO Numeric Code
- `currency` value can be an *Integer* value.
    - ISO Numeric Code (Excepts ISO Numeric Codes Start with *0* or *00*)
- `currency` value can be a `Currency` instance.

**ISO Alphabetic Code**

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

**Currency Object**

```python
>>> money = Money(1, Currency.EUR)
```

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


## String (Recommended)

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


## Integer

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


## `Currency` Object

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

```python
>>> Money(1, Currency.EUR)
```

```python
>>> eur = Currency.EUR
>>> Money(1, eur)
```

