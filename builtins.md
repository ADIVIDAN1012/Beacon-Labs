# Dyno Language Built-in Functions

> This file lists official *Dyno* built-in functions that support math, string, and general-purpose operations. These functions are universal and work across all Dyno applications.

---

## Math Functions

| Function    | Description                          | Example                |
|-------------|--------------------------------------|------------------------|
| absol(v)   | Returns the absolute value           | absol(-9) → 9          |
| elev(x, y) | Raises x to the power of y           | elev(2, 3) → 8         |
| roff(v)    | Rounds off a float to nearest int    | roff(2.6) → 3          |

---

## Length & Size

| Function  | Description                     | Example                |
|-----------|---------------------------------|------------------------|
| vol(obj) | Returns length or size of object | vol("Dyno") → 4        |

---

## String Functions

| Function        | Description                          | Example                          |
|-----------------|--------------------------------------|----------------------------------|
| merge(s1, s2)  | Concatenates two strings             | merge("Hi ", "there") → "Hi there" |

---

This file evolves as more core utilities are added to Dyno's ecosystem.
