# Dyno Sample Programs

This document provides complete example programs written in the Dyno Programming Language to demonstrate syntax, control flow, file handling, error management, and modular UOP structure.

---

## 1. Hello Dyno – Basic Output and Input

```
spec greet_user
    output("Enter your name:")
    name = ask()
    output(f"Hello, {name}!")
forward

funcall greet_user()
```

---

## 2. Type Conversion and Arithmetic

```
spec calc_sum
    output("Enter two numbers:")
    a = ask()
    b = ask()
    convert a to int
    convert b to int
    sum = a + b
    output(f"Sum is: {sum}")
forward

funcall calc_sum()
```

---

## 3. Control Flow (if-elif-else using check-alter-altern)

```
spec check_number
    output("Enter a number:")
    n = ask()
    convert n to int

    check n > 0
        output("Positive number")
    alter n < 0
        output("Negative number")
    altern
        output("Zero")
forward

funcall check_number()
```

---

## 4. Looping with traverse

```
spec list_squares
    traverse i from 1 to 5
        output(f"Square of {i} is {i * i}")
forward

funcall list_squares()
```

---

## 5. File Handling with inlet, fetch, modify, seal

```
spec file_demo
    file = inlet("data.txt", "write")
    file.modify("This is Dyno File System.")
    file.seal()

    file = inlet("data.txt", "read")
    content = file.fetch()
    output(f"File says: {content}")
    file.seal()
forward

funcall file_demo()
```

---

## 6. Error Handling using attempt, trap, trigger, conclude

```
spec error_test
    attempt
        output("Enter number:")
        x = ask()
        convert x to int
        result = 10 / x
        output(f"Result: {result}")
    trap ZeroDivisionError by e
        output("Cannot divide by zero.")
    trap ValueError by e
        output("Invalid input.")
    conclude
        output("Execution completed.")
forward

funcall error_test()
```

---

## 7. Function with Return (forward)

```
spec get_square(x)
    convert x to int
    forward x * x

spec use_square
    result = funcall get_square(7)
    output(f"Square is: {result}")
forward

funcall use_square()
```

---

## 8. Using Blueprint (Classes)

```
blueprint Car
    prep(own, name)
        own.name = name

    spec drive(own)
        output(f"{own.name} is driving.")
forward

mycar = Car("DynoX")
funcall mycar.drive()
```

---

## 9. Modular Programming using plug, share, toolkit

File: math_toolkit.dyno

```
toolkit MathOps

spec square(n)
    convert n to int
    forward n * n

share square
```

Main File:

```
plug MathOps

spec run
    result = funcall square(4)
    output(f"Square from toolkit: {result}")
forward

funcall run()
```
