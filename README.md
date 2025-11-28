<<<<<<< HEAD
# Beacon Language

Beacon is a dynamically-typed, object-oriented programming language with a focus on concurrency and safety. This repository contains the Python-based frontend and C-based backend for the Beacon compiler.

## Features

- **Dynamically-Typed:** Types are checked at runtime, providing flexibility.
- **Object-Oriented:** Supports blueprints (classes), inheritance, and objects.
- **Concurrency:** Provides features for parallel execution, including `paral`, `hold`, `signal`, and `listen`.
- **Error Handling:** Includes `attempt-trap-conclude` blocks for robust error handling.
- **Modules:** Supports toolkits for organizing and reusing code.

### Implemented Keywords

- `convert ... to ...`: Type conversion
- `note`: Docstrings for functions and blueprints
- `prep`: Constructors for blueprints
- `adopt`: Inheritance for blueprints
- `own`: Self-reference within blueprints
- `peek`: Error peeking in `trap` blocks

## Getting Started

### Prerequisites

- Python 3.10+
- C Compiler (GCC recommended)

### Building and Running

1. **Compile the C backend (from `compiler_backend_c`):**

   ```
   .\build.bat
   ```

   This produces `main.exe`.

2. **Generate AST JSON with the Python frontend (from `compiler_frontend_py`):**

   ```
   python frontend.py <path-to-source>.bpl
   ```

   This writes `..\ast.json` at the project root.

3. **Run the backend on the generated AST (from `compiler_backend_c`):**

   ```
   .\main.exe ..\ast.json
   ```
=======
# Beacon Programming Language

Welcome to the official repository for Beacon, a **user-oriented programming language** designed for clarity, simplicity, and intuitive coding. Beacon's core philosophy is Universal User-Oriented Programming (UOP), which prioritizes human-readable syntax and a natural logical flow over complex, machine-centric constructs.

This repository contains the complete documentation for the Beacon language, including its syntax, standard library, and core principles.

---

## About Beacon

Beacon was created to bridge the gap between human thought and code. It is designed for a wide range of users—from beginners and educators to experienced developers and domain experts.

### Core Philosophy
- **Human-Centric Syntax:** Keywords like `ask`, `show`, `check`, and `attempt` make code easy to read and write.
- **Intuitive Structure:** The language is structured to be predictable and easy to follow.
- **Clarity Over All:** Beacon's design emphasizes clear, self-documenting code.

---

## Key Features

- **User-Oriented Syntax:** A simple, expressive syntax based on the principles of UOP.
- **Modular by Design:** Organize code into reusable `toolkits`.
- **Clear Error Handling:** A straightforward `attempt-trap` system for managing errors.
- **Powerful Interfaces:** Use `bridge`s to define clean contracts between components.
- **Object-Oriented:** Supports classes (`blueprint`s), inheritance (`adopt`), and other OOP features.

---

## Documentation

This repository serves as the central source of truth for Beacon's documentation.

| Document | Description |
|---|---|
| **[Start Here](./index_doc.md)** | The main index for all documentation. |
| **[UOP Philosophy](./UOP.md)** | Learn about the core principles behind Beacon. |
| **[Syntax Reference](./Syntax.md)** | A complete guide to the language's syntax. |
| **[Keywords](./Keywords.md)** | A dictionary of all keywords and their meanings. |
| **[Built-in Functions](./builtins.md)** | A reference for all standard functions. |
| **[Standard Library](./Lib.md)** | An overview of the built-in `toolkits`. |
| **[Error Handling](./error.md)** | A guide to the `attempt-trap` system. |
| **[Toolkits (Modules)](./toolkit.md)** | Learn how to create and use modules. |
| **[Bridge Interfaces](./Bridge.md)** | A guide to defining interfaces. |
| **[Code Examples](./Examples.md)** | See practical examples of Beacon code. |

---

## Getting Started

To get started with Beacon, we recommend reading the **[UOP Philosophy](./UOP.md)** to understand its core concepts, followed by the **[Syntax Reference](./Syntax.md)** to learn the basics of the language. The **[Code Examples](./Examples.md)** are a great resource for seeing the language in action.
>>>>>>> b6c5e32b5b83935ac26efd256f5e7d0972be5d72
