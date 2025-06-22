# Beacon Modular System

## Overview

Beacon uses a lightweight, semantic, and UOP-compliant modular system built around three core keywords:

- **plug** – for importing modules
- **share** – for exporting functions, data, or interfaces
- **toolkit** – to define a reusable, self-contained module

This system is designed for clarity, reusability, and structured interaction between logic components.

---

## 1. toolkit – Define a Module

A toolkit is a logical unit that can contain:

- Functions (`spec`)
- Blueprints (classes)
- Constants, shared data
- Embedded bridges (optional interfaces)

**Example:**

```
toolkit MathOps
    share PI = 3.1416

    spec square x
        forward x * x

    spec cube x
        forward x * x * x
```

---

## 2. share – Expose from Toolkit

Inside a toolkit, use `share` to export:

- Constants
- Functions
- Blueprints

Only shared elements can be accessed externally.

**Example:**

```
toolkit Messages
    share greeting = "Welcome!"
    share spec shout msg
        forward msg + "!!"
```

---

## 3. plug – Import a Toolkit

Use `plug` to bring external toolkits into scope. You may also use `by` to alias the import.

**Syntax:**

```
plug ToolkitName
```

or

```
plug ToolkitName by Alias
```

**Example:**

```
plug MathOps
plug Messages by Msg

spec run
    area = square 5
    output(area)
    output(Msg.shout("Hello"))
```

---

## 4. Best Practices

- Keep each toolkit focused on one domain (e.g., FileOps, UI, Auth).
- Always share only what’s necessary.
- Use `by` for aliases when importing multiple toolkits with overlapping names.

---

## 5. Modular Flow Example

```
toolkit Auth
    share spec verify pass
        check pass == "beacon123"
            forward true
        altern
            forward false

plug Auth

spec login
    output("Enter pass:")
    p = ask()
    result = verify p
    check result
        output("Access granted.")
    altern
        output("Access denied.")
```

---

## Conclusion

Beacon's modular system is built for clarity and simplicity. It brings together the accessibility of scripting with the power of full module-based programming — made universally understandable.

---
