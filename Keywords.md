# Dyno Language Keywords Reference

> This file lists and categorizes all official *Dyno* language keywords along with their purpose and syntax overview. Dyno is a Universal, User-Oriented Programming (UOP) language inspired by Python but designed to be more expressive and human-aligned.

---

## Access & Scope

| Keyword  | Description                           | Example                         |
|----------|---------------------------------------|---------------------------------|
| avail    | Public access modifier                | avail blueprint Example         |
| shel     | Protected access modifier             | shel int count                  |

---

## Object & User-Oriented Structure

| Keyword     | Description                           | Example                                 |
|-------------|---------------------------------------|-----------------------------------------|
| blueprint   | Defines a class-like structure        | blueprint Human:                        |
| adopt       | Inherits from another blueprint       | blueprint Student adopt Human:          |
| own         | Refers to instance itself (like self) | own-name                                |
| prep        | Constructor (like __init__)           | spec prep():                            |

---

## Functions

| Keyword | Description                | Example             |
|---------|----------------------------|---------------------|
| spec    | Defines a function         | spec greet():       |
| send    | Returns a value            | send name           |

---

## Variables & Data Types

| Keyword  | Description                 |
|----------|-----------------------------|
| int      | Integer data type           |
| float    | Floating point number       |
| double   | Double precision number     |
| long     | Long integer                |
| bool     | Boolean (true/false)        |
| str      | String                      |
| nil      | Represents a null/nothing   |

---

## Type Conversion

| Syntax                   | Description                      |
|--------------------------|----------------------------------|
| convert v to DT          | Converts variable or value v to data type DT |
| Example: convert a to int| Converts a to integer            |

---

## Access Operator

| Symbol | Description                        | Example             |
|--------|------------------------------------|---------------------|
| -      | Accesses object property or method | person-name         |

---

## String Formatting

| Syntax                   | Description                        |
|--------------------------|------------------------------------|
| f""                      | f-string style formatting          |
| Example: f"Hello {name}" | Interpolates variable name         |

---

## Loops

| Keyword   | Description                       | Example                   |
|-----------|-----------------------------------|---------------------------|
| until     | Loop until condition is false     | until x > 5:              |
| traverse  | Loop over a range                 | traverse V from 1 to 9:   |

---

## Conditional Statements

| Keyword  | Description         |
|----------|---------------------|
| check    | Conditional if      |
| alter    | Else-if             |
| altern   | Else                |

---

## Error Handling

| Keyword   | Purpose                          | Example                    |
|-----------|----------------------------------|----------------------------|
| authen    | Try block for authentication/errors | authen:                |
| trap      | Catches error                    | trap error:               |
| trigger   | Raises error                     | trigger "CustomError"     |

---

## File I/O

| Keyword  | Description               | Example                        |
|----------|---------------------------|--------------------------------|
| fetch    | Read from a file          | fetch "data.txt"              |
| modify   | Write to a file           | modify "data.txt" with data   |

---

## Concurrency

| Keyword  | Description                  | Example                          |
|----------|------------------------------|----------------------------------|
| paral    | Asynchronous execution       | paral spec fetch_data():         |

---

## Modules & Imports

| Keyword | Description                                | Example                        |
|---------|--------------------------------------------|--------------------------------|
| bring   | Imports a bundle (like `import`)           | bring bundle Math              |
| by      | Alias imported bundle or item (like `as`)  | bring bundle Math by M         |
| bundle  | Describes a module/package (like `module`) | bring bundle MyTools by Tool   |

---

## Comments

| Syntax                  | Description           |
|-------------------------|-----------------------|
| < comment >             | Single-line comment   |
| <^ multi-line ^>        | Multi-line comment    |

---

## Built-in Functions

| Function     | Description                | Example              |
|--------------|----------------------------|----------------------|
| vol()        | Returns size/length        | vol(myList)          |

---

This file will evolve with Dyno’s development and cover every syntactic and semantic keyword used in the language.
