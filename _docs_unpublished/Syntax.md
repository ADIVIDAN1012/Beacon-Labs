# Beacon Syntax Guide

This document provides a complete reference to the syntax of the Beacon programming language. All code blocks are enclosed in curly braces `{}` and do not require indentation.

---

## Basic Syntax

### Comments

Single-line and multi-line comments are used to add notes that are ignored by the compiler.

```beacon
< This is a single-line comment >

<^
This is a multi-line comment.
It can span several lines.
^>
```

### Variable Declaration

Variables are assigned using the `=` operator.

```beacon
my_variable = "Hello, Beacon"
user_age = 30
```

### Constants

A `firm` variable is a constant and cannot be reassigned.

```beacon
firm PI = 3.14159
```

### Output

The `show` keyword prints values to the console.

```beacon
show("Welcome to Beacon!")
show("The value of PI is |PI|")
```

---

## Functions

A function, or `spec`, is a reusable block of code.

```beacon
spec my_function(param1, param2) {
    < function body >
    forward param1 + param2 < returns a value >
}

< Calling a function >
result = my_function(10, 20)
```

A `note` can be used to add a docstring.

```beacon
spec calculate_sum(a, b) {
    note: "This spec returns the sum of two numbers."
    forward a + b
}
```

---

## Control Flow

### Conditionals

`check`, `alter`, and `altern` are used for conditional logic.

```beacon
check(x > 10) {
    show("x is greater than 10")
}
alter(x == 10) {
    show("x is exactly 10")
}
altern {
    show("x is less than 10")
}
```

### Loops

`traverse` and `until` are used for looping.

```beacon
< For loop >
traverse i from 1 to 5 {
    show("Iteration: |i|")
}

< While loop >
count = 0
until count >= 5 {
    show("Count is |count|")
    count = count + 1
}
```

---

## Error Handling

The `attempt-trap-conclude` block is used for handling errors.

```beacon
attempt {
    risky_operation()
}
trap SomeError {
    show("Caught an error: |peek|")
}
conclude {
    show("This block always executes.")
}
```

---

## Object-Oriented Syntax

### Blueprints (Classes)

A `blueprint` defines the structure for an object.

```beacon
blueprint Dog {
    shard name
    solid species = "Canine"

    prep(own, dog_name) {
        own.name = dog_name
    }

    spec bark(own) {
        show("|own.name| says woof!")
    }
}
```

### Inheritance

A `blueprint` can `adopt` from another.

```beacon
blueprint Poodle {
    adopt Dog

    spec groom(own) {
        show("|own.name| is being groomed.")
    }
}
```

### Objects

Create an instance of a `blueprint`.

```beacon
my_dog = Dog("Buddy")
my_dog.bark()
```

---

## Modules

### Toolkits

A `toolkit` is a file that contains reusable code.

```beacon
< In file "math_utils.beacon" >
toolkit Math {
    share spec add(a, b) {
        forward a + b
    }
}
```

### Importing

Use `plug` to import a `toolkit`.

```beacon
plug Math from "math_utils.beacon"

sum = Math.add(5, 10)
show("Sum from toolkit: |sum|")
```

---

## Interfaces

A `bridge` defines an interface that can be implemented by `toolkit`s or `blueprint`s.

```beacon
bridge Greeter {
    expose spec say_hello(name)
}

toolkit FormalGreeter {
    spec say_hello(name) {
        show("Greetings, |name|.")
    }
}

inlet {
    link my_greeter to FormalGreeter
    my_greeter.say_hello("Alice")
}
```
