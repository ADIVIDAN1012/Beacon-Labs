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
