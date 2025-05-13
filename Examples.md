# Dyno Sample Programs

This document provides complete example programs written in the Dyno Programming Language to demonstrate syntax, control flow, file handling, error management, and modular UOP structure.

---

## 1. Hello Dyno – Basic Output and Input

```
spec greet_user
    output("Enter your name:")
    name = ask()
    output(f"Hello, {name}!")
    forward nil

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
    forward nil

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
    forward nil

funcall check_number()
```

---

## 4. Looping with traverse

```
spec list_squares
    traverse i from 1 to 5
        output(f"Square of {i} is {i * i}")
    forward nil

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
    forward nil

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
    forward nil

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
        output(f"{own.name} is driving.")
    forward nil

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
forward nil

funcall run()
```

# Dyno Programming Language - Keywords

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
    output(f"File content: {content}")
    file.seal()
forward nil
```

## Type Handling/Checking

```
spec type_check
    kind var_type = kind("int")
    convert a to int
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
