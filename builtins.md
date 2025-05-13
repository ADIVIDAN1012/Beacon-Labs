# Dyno Programming Language – Built-in Functions  
**Version:** v1.0 | **Format:** Universal User-Oriented Programming (UOP)  

---

## Overview

This document lists all built-in functions available in Dyno. These functions are designed to be intuitive, concise, and consistent with Dyno’s natural-language syntax. They support common operations like type checking, user input, mathematical computation, and sequence processing.

---

## Table of Contents

1. [Type & Value Utilities](#type--value-utilities)  
2. [Input & Output](#input--output)  
3. [Math Functions](#math-functions)  
4. [Sequence Utilities](#sequence-utilities)  
5. [Conversion Functions](#conversion-functions)  
6. [Functional Utilities](#functional-utilities)  
7. [Object Utilities](#object-utilities)  
8. [Miscellaneous](#miscellaneous)  

---

## Type & Value Utilities

| Function | Description                          | Dyno Example               |
|----------|------------------------------------|---------------------------|
| `kind(x)`| Returns the data type of x.         | ```output(kind(7))```      |
| `avail(x)`| Checks if x is defined and usable. | ```output(avail(y))```     |
| `exist(x)`| Checks if x exists (is not nil).    | ```output(exist(myObj))``` |

---

## Input & Output

| Function | Description                                   | Dyno Example               |
|----------|-----------------------------------------------|---------------------------|
| `ask(DT)`| Takes user input and converts it to the specified data type. | ```age = ask(int)```       |
| `output(x)`| Displays or prints the value.                | ```output("Hello, Dyno!")```|
| `tag(seq)`| Returns indexed pairs from a sequence.       | ```output(tag(["a", "b"]))```|

---

## Math Functions

| Function       | Description                      | Dyno Example                 |
|----------------|--------------------------------|-----------------------------|
| `absol(x)`     | Returns the absolute value.     | ```output(absol(-5))```      |
| `Roff(x)`      | Rounds to the nearest whole number. | ```output(Roff(4.6))```  |
| `exponent(x, y)`| Returns x to the power of y.   | ```output(exponent(2, 3))``` |
| `maximum(a, b)`| Returns the greater of two values. | ```output(maximum(3, 9))```|
| `minimum(a, b)`| Returns the lesser of two values. | ```output(minimum(3, 9))```|

---

## Sequence Utilities

| Function   | Description                  | Dyno Example                 |
|------------|------------------------------|-----------------------------|
| `length(x)`| Returns the number of elements. | ```output(length([1, 2, 3]))``` |
| `reverse(x)`| Reverses the order of elements. | ```output(reverse([1, 2, 3]))``` |
| `sort(x)`  | Returns a sorted version of the input. | ```output(sort([3, 1, 2]))``` |

---

## Conversion Functions

| Function           | Description                      | Dyno Example                 |
|--------------------|--------------------------------|-----------------------------|
| `convert v to DT`  | Converts variable v to data type DT. | ```convert age to float```  |
| `to_text(x)`       | Converts any value to text.     | ```output(to_text(89))```    |
| `to_list(x)`       | Converts a value into a list.   | ```output(to_list("abc"))``` |

---

## Functional Utilities

| Function       | Description                          | Dyno Example                   |
|----------------|------------------------------------|-------------------------------|
| `apply(f, x)`  | Applies function f to value x.      | ```output(apply(Roff, 5.6))```|
| `map(f, seq)`  | Applies function to each item in sequence. | ```output(map(Roff, [1.2, 3.4]))``` |
| `filter(f, s)` | Filters items where function returns true. | ```output(filter(exist, values))``` |

---

## Object Utilities

| Function    | Description                      | Dyno Example                 |
|-------------|--------------------------------|-----------------------------|
| `props(x)`  | Returns a list of attributes.   | ```output(props(obj))```     |
| `methods(x)`| Returns callable methods of x.  | ```output(methods(obj))```   |

---

## Miscellaneous

| Function    | Description                      | Dyno Example                 |
|-------------|--------------------------------|-----------------------------|
| `time_now()`| Returns current timestamp.       | ```output(time_now())```     |
| `halt()`    | Stops execution immediately.     | ```halt()```                 |
