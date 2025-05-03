# Dyno Language Built-ins

> This file lists all the built-in functions available in the *Dyno* programming language.

---

## Mathematical Operations

| Function   | Description                               | Example                          |
|------------|-------------------------------------------|----------------------------------|
| **sumit()** | Returns the sum of elements.             | `sumit([1, 2, 3])` returns `6`  |
| **diff()**  | Returns the difference between elements.  | `diff([5, 3])` returns `2`      |
| **prod()**  | Returns the product of elements.         | `prod([2, 3, 4])` returns `24`  |
| **quot()**  | Returns the quotient of division.        | `quot(10, 2)` returns `5`       |
| **rem()**   | Returns the remainder of a division.     | `rem(10, 3)` returns `1`        |
| **elev()**  | Returns the result of exponentiation.    | `elev(2, 3)` returns `8`        |
| **absol()** | Returns the absolute value.              | `absol(-5)` returns `5`         |
| **roff()**  | Rounds a number to the nearest integer.  | `roff(3.6)` returns `4`         |

---

## String & Data Manipulation

| Function     | Description                               | Example                              |
|--------------|-------------------------------------------|--------------------------------------|
| **conjoin()**| Joins elements together.                  | `conjoin(['a', 'b', 'c'], '-')` returns `'a-b-c'` |
| **splitter()**| Splits elements based on a delimiter.    | `splitter('a,b,c', ',')` returns `['a', 'b', 'c']` |
| **swap()**   | Swaps two elements.                       | `swap([1, 2])` returns `[2, 1]`      |
| **style()**  | Applies a style transformation.           | `style(text, 'bold')` returns `'bold text'` |
| **slice()**  | Extracts a portion of a collection.       | `slice([1, 2, 3, 4], 1, 3)` returns `[2, 3]` |

---

## Input/Output

| Function     | Description                               | Example                             |
|--------------|-------------------------------------------|-------------------------------------|
| **readin()** | Reads input data.                         | `readin()` prompts user for input   |
| **writeout()**| Writes output data.                      | `writeout('Hello World')` prints `'Hello World'` |

---

## Memory & Collection Operations

| Function     | Description                               | Example                          |
|--------------|-------------------------------------------|----------------------------------|
| **create()** | Creates a new instance or structure.      | `create([1, 2, 3])` returns `[1, 2, 3]` |
| **erase()**  | Erases or removes an element.             | `erase([1, 2, 3], 2)` returns `[1, 3]` |
| **locate()** | Finds the position of an element.         | `locate([1, 2, 3], 2)` returns `1`  |
| **order()**  | Sorts or arranges elements.               | `order([3, 1, 2])` returns `[1, 2, 3]` |

---

## Miscellaneous Operations

| Function     | Description                               | Example                        |
|--------------|-------------------------------------------|--------------------------------|
| **logit()**  | Logs a value for debugging or output.     | `logit('Error: Something went wrong')` |
| **parse_resp()**| Parses a response or data.              | `parse_resp('Response Data')`  |
| **connect()**| Establishes a connection.                 | `connect('server')`            |
| **close_conn()**| Closes a connection.                    | `close_conn('server')`         |
| **randgen()**| Generates a random value.                 | `randgen(1, 100)` returns a random number between 1 and 100 |
| **shuffle()**| Shuffles elements randomly.               | `shuffle([1, 2, 3])` returns a shuffled list like `[2, 3, 1]` |
| **reverse()**| Reverses the order of elements.           | `reverse([1, 2, 3])` returns `[3, 2, 1]` |
| **bound()**  | Binds or ties elements together.          | `bound([1, 2], [3, 4])` returns `[(1, 3), (2, 4)]` |

---

## File Operations

| Function     | Description                               | Example                            |
|--------------|-------------------------------------------|------------------------------------|
| **fetch()**  | Fetches data from a file.                 | `fetch('file.txt')` returns content from file |
| **modify()** | Writes or modifies data in a file.        | `modify('file.txt', 'New Data')`  |

---

## System Operations

| Function     | Description                               | Example                             |
|--------------|-------------------------------------------|-------------------------------------|
| **sync()**   | Syncs data or system state.               | `sync()` syncs the system state.   |
| **exit()**   | Exits or terminates a process.            | `exit()` terminates the program.   |
