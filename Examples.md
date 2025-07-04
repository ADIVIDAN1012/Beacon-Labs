# Beacon Sample Programs

This document provides complete example programs written in the Beacon Programming Language to demonstrate syntax, control flow, file handling, error management, and modular UOP structure.

---

## 1. Hello Beacon – Basic Output and Input

```
spec greet_user
    name = ask("Enter your name:")
    output("Hello, |name|!")
    forward nil

funcall greet_user()
```

---

## 2. Type Conversion and Arithmetic

```
spec calc_sum
    a = ask("Enter first number:")
    b = ask("Enter second number:")
    sum = a + b
    output("Sum is: |sum|")
    forward nil

funcall calc_sum()
```

---

## 3. Control Flow (if-elif-else using check-alter-altern)

```
spec check_number
    n = ask("Enter a number:")

    check n > 0
        output("Positive number")
    alter n < 0
        output("Negative number")
    altern
        output("Zero")
    forward nil

funcall check_number()
```

---

## 4. Looping with traverse

```
spec list_squares
    traverse i from 1 to 5
        output("Square of |i| is |i * i|")
    forward nil

funcall list_squares()
```

---

## 5. File Handling with inlet, fetch, modify, seal

```
spec file_demo
    file = inlet("data.txt", "write")
    file.modify("This is Beacon File System.")
    file.seal()

    file = inlet("data.txt", "read")
    content = file.fetch()
    output("File says: |content|")
    file.seal()
    forward nil

funcall file_demo()
```

---

## 6. Error Handling using attempt, trap, trigger, conclude

```
spec error_test
    attempt
        x = ask("Enter number:")
        result = 10 / x
        output("Result: |result|")
    trap ZeroDivisionError by e
        output("Cannot divide by zero.")
    trap ValueError by e
        output("Invalid input.")
    conclude
        output("Execution completed.")
    forward nil

funcall error_test()
```

---

## 7. Function with Return (forward)

```
spec get_square(x)
    forward x * x

spec use_square
    result = funcall get_square(7)
    output("Square is: |result|")
    forward nil

funcall use_square()
```

---

## 8. Using Blueprint (Classes)

```
blueprint Car
    prep(own, name)
        own.name = name

    spec drive(own)
        output("|own.name| is driving.")
    forward nil

mycar = Car("BeaconX")
funcall mycar.drive()
```

---

## 9. Modular Programming using plug, share, toolkit

File: math_toolkit.beacon

```
toolkit MathOps

spec square(n)
    forward n * n

share square
```

Main File:

```
plug MathOps

spec run
    result = funcall square(4)
    output("Square from toolkit: |result|")
forward nil

funcall run()
```

# Beacon Programming Language - Keywords

## Access Control

```
covnito spec private_spec
    output("This is private")
forward nil

shel spec protected_spec
    output("This is protected")
forward nil

avail spec public_spec
    output("This is public")
forward nil

internal spec package_spec
    output("This is package-level access")
forward nil

expose spec exposed_spec
    output("This is internal/public exposure")
forward nil
```

## Concurrency/Parallelism

```
paral spec async_task
    hold some_async_operation()
    output("Async task completed")
forward nil

flux spec data_flow
    output("Data flowing")
forward nil

barrier spec lock_example
    permit lock
    output("Locked section")
    signal event
forward nil
```

## File Handling

```
spec file_ops
    file = inlet("file.txt", "write")
    file.modify("Writing to file")
    file.seal()

    file = inlet("file.txt", "read")
    content = file.fetch()
    output("File content: |content|")
    file.seal()
forward nil
```

## Type Handling/Checking

```
spec type_check
    kind var_type = kind("int")
    forward nil
```

## Inheritance

```
blueprint Father
    spec greet(own)
        output("Hello from Father")
    forward nil

blueprint Child belong Father
    spec greet(own)
        output("Hello from Child")
    forward nil

child = Child()
funcall child.greet()
```

## Memory Management

```
spec memory_ops
    slip some_memory
    wipe garbage_collector
forward nil
```

## Miscellaneous Operations

```
spec misc_ops
    authen user
    transform data
    reduce data
forward nil
```

## Data Serialization

```
spec serialization
    pack data
    unpack data
forward nil
```

## Event Handling

```
spec event_handling
    listen event
    trigger event
forward nil
```

## Debugging/Logging

```
spec debugging
    track info
    trace execution
    watch variable
forward nil 
```

## Special Features

```
spec special_features
    spec my_function
    check condition
    alter condition
    altern
    conclude
    skelet skel_class
    decon object
    forward nil
```

## System/Environment Operations

```
plug toolkit

share function

toolkit MyToolkit

bloc batch_operation

embed resource

bridge interface

link join

belong inheritance

peek access

infuse inject
forward nil
```

---
