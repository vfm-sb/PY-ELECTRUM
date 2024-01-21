# Valid Amount Values

The `amount` represents the amount of a money instance.
- `amount` value can be an *Integer* value.
- `amount` value can be a *Float* value.
- `amount` value can be a *Numeric String* value.
- `amount` value can be a valid *Decimal* value.

```python
>>> Money(1)
```

```python
>>> Money(9.99)
```

```python
>>> Money(1_000)
```

```python
>>> Money("1")
```

```python
>>> Money("9.99")
```

```python
>>> Money("1000")
```

```python
>>> Money(Decimal(1))
```

```python
>>> Money(Decimal(9.99))
```

```python
>>> Money(Decimal("1"))
```

```python
>>> Money(Decimal("9.99"))
```


## Integer

```python
>>> Money(1)
```

```python
>>> Money(1, "EUR")
```

```python
>>> Money(10, "BGN")
```

```python
>>> Money(100, "TRY")
```


## Float

```python
>>> Money(11.11)
```

```python
>>> Money(19.92, "EUR")
```

```python
>>> Money(20.23, "BGN")
```

```python
>>> Money(88.88, "TRY")
```


## String

```python
>>> Money("1")
```

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
>>> Money("11.11")
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


## Decimal

```python
>>> Money(Decimal(1))
```

```python
>>> Money(Decimal("1"))
```

```python
>>> Money(Decimal(11.11))
```

```python
>>> Money(Decimal("11.11"))
```

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

