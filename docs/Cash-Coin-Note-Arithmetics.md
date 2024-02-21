# Cash & Coin & Note Arithmetics

<br>

## `Cash + Cash = Money`

```python
>>> Cash(0.10, "EUR") + Cash(2, "EUR")
>>> Money(2.10, "EUR")
```

```python
>>> Cash(50, "EUR") + Cash(10, "EUR")
>>> Money(60.00, "EUR")
```

```python
>>> Cash(50, "EUR") + Cash(0.50, "EUR")
>>> Money(50.50, "EUR")
```

## `Coin + Coin = Money`

```python
>>> Coin(0.10, "EUR") + Coin(2, "EUR")
>>> Money(2.10, "EUR")` # or EUR(2.10)
```

```python
>>> Coin(0.1, "EUR") + Coin(0.01, "EUR")
>>> Money(0.11, "EUR") # or EUR(0.11)
```

## `Note + Note = Money`

```python
>>> Note(50, "EUR") + Note(10, "EUR")
>>> Money(60.00, "EUR") # or EUR(60.00)
```

```python
>>> Note(200, "EUR") + Note(5, "EUR")
>>> Money(205.00, "EUR") # or EUR(205.00)
```

## `Coin + Note = Money`

```python
>>> Coin(0.5, "EUR") + Note(10, "EUR")
>>> Money(10.50, "EUR") # or EUR(10.50)
```

```python
>>> Note(50, "EUR") + Coin(2, "EUR")
>>> Money(52.00, "EUR") # or EUR(52.00)
```

## `Cash + Coin + Note = Money`

```python
>>> Cash(10, "EUR") + Coin(1, "EUR") + Note(100, "EUR")
>>> Money(111.00, "EUR")
```

```python
>>> Cash(0.01, "EUR") + Coin(1, "EUR") + Note(10, "EUR")
>>> Money(11.01, "EUR")
```

## `Cash + Coin + Note + Money = Money`

```python
>>> Cash(10, "EUR") + Coin(0.5, "EUR") + Note(5, "EUR") + Money(9.99, "EUR")
>>> Money(25.49, "EUR") # or EUR(25.49)
```
