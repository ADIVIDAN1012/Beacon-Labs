# Dyno Language Built-in Functions Reference

> This file lists all core built-in functions officially supported in the *Dyno* programming language. These functions enhance user productivity by providing essential utilities out-of-the-box.

---

## Mathematical Functions

| Function       | Description                            | Example                     |
|----------------|----------------------------------------|-----------------------------|
| absol(x)       | Returns absolute value of x            | absol(-10) → 10             |
| exponent(a, b) | Returns a raised to the power of b     | exponent(2, 3) → 8          |
| Roff(x)        | Rounds a number to nearest integer     | Roff(2.6) → 3               |

---

## String Operations

| Function         | Description                            | Example                              |
|------------------|----------------------------------------|--------------------------------------|
| concat(s1, s2)   | Concatenates two strings               | concat("Hi", "There") → "HiThere"    |

---

## List & Collection Functions

| Function     | Description                            | Example                     |
|--------------|----------------------------------------|-----------------------------|
| vol(x)       | Returns the number of items in x      | vol([1, 2, 3]) → 3          |

---

## Type Conversion

> Handled using the `convert v to DT` syntax as specified in **Keywords.md**.

---

## File Operations

> See `fetch` and `modify` under the **File I/O** section of **Keywords.md**.

---

This file will grow as Dyno evolves, and new built-ins will be added to match the language's expressiveness and user-oriented philosophy.
