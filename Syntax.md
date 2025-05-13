# Syntax for Dyno Programming Language

## Variable Declaration
Variables in Dyno are dynamically typed, allowing developers to assign values without explicitly defining their types. This makes coding more intuitive and reduces the overhead of type management.

``` 
var name = "Dyno"
var age = 25
```

## Conditional Statements

Dyno provides a structured way to handle decision-making with its conditional syntax.

### Check
Used for standard if conditions.

```
check condition {
    <Code executes if condition is true>
}
```

### Alter
Acts as an else if, allowing multiple conditions.

```
check condition {
    <Code executes if condition is true>
} alter another_condition {
    <Code executes if another_condition is true>
}
```

### Altern
Functions like else, executing when no prior conditions are met.

```
check condition {
    <Code executes if condition is true>
} altern {
    <Code executes if no condition is true>
}
```

## Loops

### Until
Executes code while a condition remains true, similar to while loops.

```
until condition {
    <Code executes until condition is false>
}
```

### Traverse
Iterates over a range, similar to for loops.

```
traverse variable from 1 to 10 {
    <Code executes for each iteration>
}
```

## Functions

### Spec
Defines reusable blocks of code.

```
spec function_name() {
    <Function body>
}
```

### Funcall
Invokes a function.

```
funcall function_name()
```

### Send
Returns a value from a function.

```
send result
```

## Error Handling

### Attempt
Handles operations that may cause errors.

```
attempt {
    <Code that might throw an error>
}
```

### Trap
Captures errors, preventing application crashes.

```
attempt {
    <Code that might throw an error>
} trap error {
    <Handle the error>
}
```

### Conclude
Executes code regardless of error occurrence.

```
attempt {
    <Code that might throw an error>
} trap error {
    <Handle the error>
} conclude {
    <Code to execute always>
}
```

## Data Types

### Kind
Checks a variable's type.

```
kind(variable)
```

### Convert
Converts a variable to a specified type.

```
convert variable to int
```

## Memory Management

### Slip
Frees allocated memory.

```
slip variable
```

### Wipe
Initiates garbage collection.

```
wipe variable
```

## Miscellaneous Operations

### Authen
Performs validation or authentication checks.

```
authen condition
```

### Transform
Applies a function to a list, modifying its contents.

```
transform list with function
```

### Reduce
Aggregates list elements using a function.

```
reduce list with function
```

## Event Handling

### Listen
Binds an event to a handler.

```
listen event to handler
```

### Trigger
Emits an event.

```
trigger event
```

## File Handling

### Fetch
Reads data from a file.

```
fetch file
```

### Modify
Writes data to a file.

```
modify file with data
```

### Unlock
Opens a file for operations.

```
unlock file
```

### Seal
Closes a file.

```
seal file
```

## Type Handling

### Nick
Defines a type alias.

```
nick alias = existing_type
```

### Iden
Verifies if a variable matches a specific type.

```
iden(variable, type)
```

## Inheritance

### Adopt
Allows a class to inherit from a parent.

```
blueprint Child adopt Parent
```

### Father
Defines the base class.

```
blueprint Parent
```

### Child
Creates a derived class.

```
blueprint Child adopt Parent
```

## Concurrency and Parallelism

### Paral
Marks a task as asynchronous.

```
paral task
```

### Hold
Waits for asynchronous tasks to finish.

```
hold task
```

### Flux
Manages threads and parallel execution.

```
flux task
```

### Barrier
Creates concurrency locks.

```
barrier lock
```

### Permit
Handles semaphores.

```
permit semaphore
```

### Signal
Manages event-driven parallel execution.

```
signal event
```

## Miscellaneous

### Procsys
Defines a system with procedural components.

```
procsys example
```

### Bloc
Groups tasks for structured execution.

```
bloc group
```

### Skelet
Establishes a framework for systems.

```
skelet structure
```

### Decon
Breaks down structures for analysis.

```
decon structure
