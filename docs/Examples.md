# Beacon Code Examples

This document provides a series of code examples to demonstrate the syntax, features, and UOP (Universal User-Oriented Programming) principles of the Beacon language.

---

## 1. Hello, World

This example shows basic input and output using `ask` and `show`.

```beacon
spec greet_user {
    name = ask("Enter your name: ")
    show("Hello, |name|!")
}

greet_user()
```

---

## 2. Type Conversion and Arithmetic

This example demonstrates how to convert text input to numbers and perform a simple calculation.

```beacon
spec calculate_sum {
    a_text = ask("Enter the first number: ")
    b_text = ask("Enter the second number: ")

    a = convert a_text to Num
    b = convert b_text to Num

    sum = a + b
    show("The sum is: |sum|")
}

calculate_sum()
```

---

## 3. Conditional Logic

Beacon uses `check`, `alter`, and `altern` for conditional branching, similar to `if`, `else if`, and `else`.

```beacon
spec check_number {
    n_text = ask("Enter a number: ")
    n = convert n_text to Num

    check n > 0 {
        show("The number is positive.")
    }
    alter n < 0 {
        show("The number is negative.")
    }
    altern {
        show("The number is zero.")
    }
}

check_number()
```

---

## 4. Looping

The `traverse` keyword is used for iterating over a range of numbers.

```beacon
spec list_squares {
    show("Squares of numbers from 1 to 5:")
    traverse i from 1 to 5 {
        show("Square of |i| is |i * i|")
    }
}

list_squares()
```

---

## 5. Error Handling

This example shows how to handle potential errors, such as division by zero, using `attempt` and `trap`.

```beacon
spec safe_divide {
    attempt {
        a = convert ask("Enter numerator: ") to Num
        b = convert ask("Enter denominator: ") to Num

        check b == 0 {
            trigger ZeroDivide
        }

        result = a / b
        show("Result: |result|")
    }
    trap ZeroDivide {
        show("Error: Cannot divide by zero.")
    }
    trap TypeFail {
        show("Error: Both inputs must be valid numbers.")
    }
}

safe_divide()
```

---

## 6. Functions and Return Values

Functions (or `spec`s) use the `forward` keyword to return a value.

```beacon
spec get_square(x) {
    forward x * x
}

spec use_square {
    result = get_square(7)
    show("The square of 7 is: |result|")
}

use_square()
```

---

## 7. Blueprints (Classes) and Objects

A `blueprint` is used to define a class. Objects are instances of blueprints.

```beacon
blueprint Car {
    shard name

    prep(own, car_name) {
        own.name = car_name
    }

    spec drive(own) {
        show("|own.name| is driving.")
    }
}

my_car = Car("BeaconX")
my_car.drive()
```

---

## 8. Modular Programming with Toolkits

Code can be organized into reusable `toolkit`s. Use `plug` to import a toolkit and `share` to export its functions.

**File: `math_utils.beacon`**

```beacon
toolkit MathOps {
    share spec square(n) {
        forward n * n
    }
}
```

**Main File:**

```beacon
plug MathOps from "math_utils.beacon"

spec main {
    result = square(5)
    show("The square from the toolkit is: |result|")
}

main()
```
