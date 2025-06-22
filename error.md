# Error Handling in Beacon

Beacon uses a clean and expressive approach to error management based on UOP (Universal User-Oriented Programming). It prioritizes clarity over verbosity.

---

## 1. Core Error Handling Keywords

| Beacon Keyword | Equivalent     | Purpose                                      |
|----------------|---------------|----------------------------------------------|
| attempt        | try           | Begin a block that may raise an error        |
| trap           | catch         | Handle a specific error                      |
| conclude       | finally       | Always run code regardless of errors         |
| trigger        | raise         | Manually raise an error                      |
| check          | if            | Conditional check inside error blocks        |
| peek           | Exception obj | View the error message/data caught in trap   |

---

## 2. Built-in Error Types

| Error Name   | Meaning                            |
|--------------|------------------------------------|
| TypeFail     | Type mismatch or invalid conversion|
| ZeroDivide   | Division by zero attempted         |
| NilAccess    | Accessed a nil (null) value        |
| IndexOver    | Index out of valid range           |
| KeyVoid      | Missing key in a bind (dictionary) |
| Denied       | Access or permission denied        |
| Missing      | Expected item not provided         |
| Timeout      | Operation took too long            |
| SyntaxBreak  | Invalid Beacon syntax encountered  |
| FailGeneral  | Unspecified or general failure     |

---

## 3. Error Handling Syntax Example

```plaintext
attempt
    x = ask("Enter a number:")
    y = 10 / x
    output("Result is |y|")
trap ZeroDivide
    output("You can't divide by zero.")
trap TypeFail
    output("Input must be a valid number.")
conclude
    output("Division attempt concluded.")
```

---

## 4. Raising Custom Errors with trigger

```plaintext
spec safe_sqrt val
    check val < 0
        trigger TypeFail by "Negative values not allowed."
    forward val ** 0.5
```

---

## 5. Accessing Error Info with peek

```plaintext
attempt
    trigger FailGeneral by "Custom failure triggered."
trap FailGeneral by peek
    output("Error caught: |peek|")
```

---

## 6. Multi-Trap & Conditional Errors

```plaintext
attempt
    x = ask("Enter a number:")

    check x == 0
        trigger ZeroDivide

    check x < 0
        trigger TypeFail by "Negative numbers not accepted."

    result = 100 / x
    output("Result is |result|")
trap ZeroDivide
    output("Division by zero is not allowed.")
trap TypeFail by peek
    output("Type error occurred: |peek|")
conclude
    output("Finished checking input.")
```

---

