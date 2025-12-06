# Error Handling in Beacon

Error handling in Beacon is designed to be expressive, clear, and aligned with the UOP (Universal User-Oriented Programming) philosophy. Instead of traditional `try-catch-finally` blocks, Beacon uses an `attempt-trap-conclude` structure that reads more like natural language.

---

## 1. Core Keywords

| Keyword | Role | Equivalent | Description |
|---|---|---|---|
| `attempt` | Begins a monitored block | `try` | Encloses code that might raise an error. |
| `trap` | Catches a specific error | `catch` / `except` | Defines a block to handle a specific type of error. |
| `conclude` | Final execution block | `finally` | Contains code that will always run, regardless of whether an error occurred. |
| `trigger` | Raises an error | `raise` / `throw` | Manually initiates an error. |
| `Blame` | The error object type | `Exception` | Represents the error itself, which can be inspected. |
| `peek` | Accesses error details | (none) | A special variable inside a `trap` block that holds the error message. |

---

## 2. Common Error Types

Beacon includes several built-in error types to cover common failure scenarios:

| Error Type | Description |
|---|---|
| `TypeFail` | Occurs on a type mismatch or invalid data conversion. |
| `ZeroDivide` | Triggered when attempting to divide by zero. |
| `NilAccess` | Raised when trying to use a `Nil` value as if it were a valid object. |
| `IndexOver` | Occurs when an index is outside the valid range of a sequence. |
| `KeyVoid` | Raised when a key is not found in a dictionary or map. |
| `Denied` | Triggered due to a lack of permissions or failed authentication. |
| `Missing` | Occurs when a required resource or value is not found. |
| `Timeout` | Raised when an operation exceeds its allowed time. |
| `FailGeneral` | A generic error for unspecified problems. |

---

## 3. Basic Error Handling

The `attempt-trap-conclude` structure is the foundation of error handling in Beacon.

```beacon
attempt {
    num = convert "abc" to Num
    show("Conversion successful.")
}
trap TypeFail {
    show("Could not convert the text to a number.")
}
conclude {
    show("Execution finished.")
}
```

---

## 4. Triggering Errors

You can manually `trigger` an error. This is useful for enforcing constraints in your own functions.

```beacon
spec set_age(new_age) {
    check new_age < 0 {
        trigger TypeFail with "Age cannot be negative."
    }
    own.age = new_age
}
```

---

## 5. Accessing Error Details with `peek`

Inside a `trap` block, the special variable `peek` contains the message or data associated with the error.

```beacon
attempt {
    trigger FailGeneral with "Something went wrong."
}
trap FailGeneral {
    show("Error caught: |peek|") < Output: Error caught: Something went wrong. >
}
```

---

## 6. Handling Multiple Error Types

You can chain multiple `trap` blocks to handle different types of errors from a single `attempt` block.

```beacon
spec divide(a, b) {
    check kind(a) != "Num" or kind(b) != "Num" {
        trigger TypeFail with "Both inputs must be numbers."
    }
    check b == 0 {
        trigger ZeroDivide
    }
    forward a / b
}

attempt {
    result = divide(10, 0)
    show("Result: |result|")
}
trap ZeroDivide {
    show("Cannot divide by zero.")
}
trap TypeFail {
    show("Invalid input: |peek|")
}
```

