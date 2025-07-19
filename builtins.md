# Built-in Functions in Beacon

This document provides a comprehensive list of all built-in functions available in the Beacon language. These functions are designed to be intuitive and align with Beacon's UOP (Universal User-Oriented Programming) philosophy, providing straightforward ways to perform common tasks.

---

## Table of Contents

1. [Input & Output](#input--output)
2. [State & Type Utilities](#state--type-utilities)
3. [Data Conversion](#data-conversion)
4. [Math](#math)
5. [Sequence Manipulation](#sequence-manipulation)
6. [Functional Programming](#functional-programming)
7. [Object Introspection](#object-introspection)
8. [Control Flow](#control-flow)
9. [Miscellaneous](#miscellaneous)

---

## Input & Output

| Function      | Description                                                       | Example                           |
| ------------- | ----------------------------------------------------------------- | --------------------------------- |
| `ask(prompt)` | Prompts the user for input and returns the entered value as text. | `name = ask("Enter your name: ")` |
| `show(value)` | Displays a value to the standard output.                          | `show("Hello, Beacon!")`          |

---

## State & Type Utilities

| Function          | Description                                                                    | Example                           |
| ----------------- | ------------------------------------------------------------------------------ | --------------------------------- |
| `kind(variable)`  | Returns the data type of a variable as text (e.g., "Num", "Text").             | `type = kind(123)`                |
| `exist(variable)` | Returns `On` if a variable has been defined and is not `Nil`, otherwise `Off`. | `check exist(my_var) { ... }`     |
| `avail(variable)` | Similar to `exist`, checks for non-nil and defined state.                      | `check avail(user_input) { ... }` |

---

## Data Conversion

| Function                  | Description                                                              | Example                          |
| ------------------------- | ------------------------------------------------------------------------ | -------------------------------- |
| `convert <var> to <type>` | Converts a variable to the specified data type (`Num`, `Decim`, `Text`). | `num_val = convert "123" to Num` |
| `to_text(value)`          | Converts any value to its text representation.                           | `text_val = to_text(45.6)`       |
| `to_list(value)`          | Converts a sequence or single item into a list.                          | `list_of_chars = to_list("abc")` |

---

## Math

| Function                | Description                                     | Example                     |
| ----------------------- | ----------------------------------------------- | --------------------------- |
| `absol(number)`         | Returns the absolute value of a number.         | `positive_val = absol(-10)` |
| `round(number)`         | Rounds a decimal number to the nearest integer. | `rounded = round(4.6)`      |
| `exponent(base, power)` | Calculates `base` to the power of `power`.      | `result = exponent(2, 3)`   |
| `maximum(a, b)`         | Returns the greater of two numbers.             | `larger = maximum(10, 20)`  |
| `minimum(a, b)`         | Returns the lesser of two numbers.              | `smaller = minimum(10, 20)` |

---

## Sequence Manipulation

| Function            | Description                                                     | Example                         |
| ------------------- | --------------------------------------------------------------- | ------------------------------- |
| `length(sequence)`  | Returns the number of items in a list, text, or other sequence. | `size = length([1, 2, 3])`      |
| `reverse(sequence)` | Returns a reversed copy of a sequence.                          | `rev_list = reverse([1, 2, 3])` |
| `sort(sequence)`    | Returns a sorted copy of a sequence.                            | `sorted_list = sort([3, 1, 2])` |
| `tag(sequence)`     | Returns a list of (index, value) pairs from a sequence.         | `tagged = tag(["a", "b"])`      |

---

## Functional Programming

| Function                     | Description                                                                                         | Example                                 |
| ---------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------- |
| `apply(function, value)`     | Applies a function to a single value.                                                               | `result = apply(round, 5.6)`            |
| `map(function, sequence)`    | Applies a function to each item in a sequence and returns a new list of the results.                | `rounded_nums = map(round, [1.2, 3.8])` |
| `filter(function, sequence)` | Returns a new list containing only the items from the sequence for which the function returns `On`. | `non_nils = filter(exist, [1, Nil, 3])` |

---

## Object Introspection

| Function          | Description                                                          | Example                            |
| ----------------- | -------------------------------------------------------------------- | ---------------------------------- |
| `props(object)`   | Returns a list of the names of an object's properties (traits).      | `properties = props(my_obj)`       |
| `methods(object)` | Returns a list of the names of an object's callable methods (specs). | `callable_specs = methods(my_obj)` |

---

## Control Flow

| Function | Description                                     | Example                                 |
| -------- | ----------------------------------------------- | --------------------------------------- |
| `halt()` | Immediately stops the execution of the program. | `check user_input == "exit" { halt() }` |

---

## Miscellaneous

| Function     | Description                           | Example                  |
| ------------ | ------------------------------------- | ------------------------ |
| `time_now()` | Returns the current system timestamp. | `timestamp = time_now()` |
