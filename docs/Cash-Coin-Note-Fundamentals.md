# Fundamentals of Cash & Coin & Note (Banknote) Classes

In addition to `Money`, Py-Electrum also contains `Coin`, `Note`/ `Banknote` and `Cash` classes that represent real-world **Coin**, **Banknote** and **Cash** concepts to a some extend.

`Coin`, `Note`/`Banknote` and `Cash` classes are specialised extensions of the `Money` class, designed to represent designated units of a currency. The constructors of these classes ensure coherence with real-world scenarios, where currencies define specific denominations, adding nuance to physical currency systems.

A `Coin` object can only be instantiated with the predefined subunits of the given currency.

A `Note` or`Banknote` object can only be instantiated with the predefined units of the given currency. The `Note` and `Banknote` classes are identical; the choice between them is a matter of user preference.

`Cash` objects are combination of `Coin` and `Banknote` objects. They can be instantiated both with predefined unit and subunit values of the given currency.

