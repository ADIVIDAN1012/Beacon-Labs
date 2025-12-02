# 🔥 Beacon Programming Language

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![C](https://img.shields.io/badge/C-GCC-green.svg)](https://gcc.gnu.org/)

**Beacon** is a modern, dynamically-typed, object-oriented programming language designed with a focus on **concurrency**, **safety**, and **expressiveness**. With an intuitive syntax and powerful features, Beacon aims to make parallel programming accessible while maintaining code clarity and robustness.

This repository contains the complete Beacon toolchain:
- **Python-based Frontend:** Lexer, parser, and AST generator
- **C-based Backend:** AST interpreter and runtime execution engine
- **VS Code Extension:** Syntax highlighting and language support
- **Documentation:** Comprehensive language specification and guides

---

## ✨ Key Features

### 🎯 Core Language Features
- **Dynamic Typing:** Flexible type system with runtime type checking
- **Object-Oriented:** Full OOP support with blueprints (classes), inheritance, and polymorphism
- **Unique Syntax:** Distinctive keywords like `spec` (function), `blueprint` (class), `traverse` (for), and more
- **Rich Standard Library:** Built-in functions for common operations

### ⚡ Concurrency & Parallelism
- **Parallel Execution:** `paral` keyword for parallel function execution
- **Async/Await:** `hold` for awaiting parallel operations
- **Event-Driven:** `signal` and `listen` for event-based programming
- **Thread-Safe:** Built-in concurrency primitives

### 🛡️ Error Handling & Safety
- **Structured Error Handling:** `attempt-trap-conclude` blocks (try-catch-finally)
- **Error Inspection:** `peek` keyword for error details
- **Assertions:** `authen` for runtime validation
- **Type Safety:** Runtime type checking and conversion with `convert`

### 📦 Modularity
- **Toolkit System:** Organize code with `toolkit` (modules)
- **Import/Export:** `plug` and `share` for code reusability
- **Access Modifiers:** `hidden`, `shielded`, `internal`, `expose` for encapsulation
- **Interfaces:** `bridge` for defining contracts between components

### 🔧 Advanced Features
- **Functional Programming:** `transform` (map) and `condense` (reduce)
- **Serialization:** `pack` and `unpack` for data persistence
- **Static Members:** `solid` keyword for class-level variables and methods
- **Constants:** `firm` for immutable values
- **Docstrings:** `note` for inline documentation

---

## 📚 Documentation

Explore the comprehensive documentation to learn more about Beacon:

- **[Keywords Reference](Keywords.md)** - Complete dictionary of all Beacon keywords
- **[Syntax Guide](Syntax.md)** - Language syntax and grammar
- **[Examples](Examples.md)** - Code examples and tutorials
- **[Built-in Functions](builtins.md)** - Standard library reference
- **[Error Handling](error.md)** - Error types and handling patterns
- **[Toolkits/Modules](toolkit.md)** - Module system documentation
- **[Bridges (Interfaces)](Bridge.md)** - Interface specifications
- **[Library Reference](Lib.md)** - Extended library documentation
- **[UOP (Unique Object Protocol)](UOP.md)** - Object protocol specification

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10 or higher**
- **C Compiler** (GCC recommended for Windows, or Clang/MSVC)
- **Git** (for cloning the repository)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ADIVIDAN1012/Beacon-Labs.git
   cd Beacon-Labs
   ```

2. **Set up Python environment (optional but recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

### Building the Compiler

#### Step 1: Compile the C Backend

Navigate to the C backend directory and build:

```bash
cd compiler_backend_c
.\build.bat
```

This generates `main.exe` - the Beacon runtime interpreter.

#### Step 2: Write Your First Beacon Program

Create a file `hello.bpl`:

```beacon
spec main() {
    show("Hello, Beacon! 🔥")
}

main()
```

#### Step 3: Compile to AST

From the `compiler_frontend_py` directory:

```bash
cd ..\compiler_frontend_py
py frontend.py ..\hello.bpl
```

This generates `ast.json` in the project root.

#### Step 4: Execute Your Program

From the `compiler_backend_c` directory:

```bash
cd ..\compiler_backend_c
.\main.exe ..\ast.json
```

Output:
```
Hello, Beacon! 🔥
```

---

## 💡 Quick Examples

### Hello World
```beacon
spec greet(name) {
    show("Hello, " + name + "!")
}

greet("World")
```

### Object-Oriented Programming
```beacon
blueprint Person {
    shard name
    shard age
    
    prep(n, a) {
        own.name = n
        own.age = a
    }
    
    spec introduce() {
        show("Hi, I'm " + own.name + " and I'm " + convert own.age to Text + " years old.")
    }
}

firm person = Person("Alice", 30)
person.introduce()
```

### Error Handling
```beacon
attempt {
    firm result = convert "not a number" to Num
} trap {
    show("Error: " + peek)
} conclude {
    show("Cleanup complete")
}
```

### Parallel Execution
```beacon
paral spec compute(x) {
    forward x * x
}

firm result = hold compute(10)
show(result)  < Output: 100 >
```

More examples can be found in [Examples.md](Examples.md).

---

## 🏗️ Project Structure

```
Beacon-Labs/
├── compiler_frontend_py/     # Python-based lexer, parser, AST generator
├── compiler_backend_c/        # C-based interpreter and runtime
├── beacon-vscode-extension/   # VS Code language extension
├── beacon-website/            # Official Beacon website
├── bpl-icon-theme/           # Icon theme for .bpl files
├── tests/                    # Test suite
├── cJSON/                    # JSON parsing library (dependency)
├── assets/                   # Project assets
├── *.md                      # Documentation files
└── README.md                 # This file
```

---

## 🛠️ Development

### VS Code Extension

Install the Beacon VS Code extension for syntax highlighting and language support:

1. Open the `beacon-vscode-extension` folder in VS Code
2. Press `F5` to launch a new VS Code window with the extension loaded
3. Open any `.bpl` file to see syntax highlighting

### Running Tests

```bash
cd tests
py test_runner.py
```

---

## 🌐 Website

Visit the official Beacon website for interactive tutorials and playground:

```bash
cd beacon-website
# Follow GITHUB_PAGES_SETUP.md or REDEPLOY_WEBSITE.md for deployment
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Whether it's bug fixes, new features, documentation improvements, or examples:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📧 Contact & Links

- **Repository:** [https://github.com/ADIVIDAN1012/Beacon-Labs](https://github.com/ADIVIDAN1012/Beacon-Labs)
- **Issues:** [Report a bug or request a feature](https://github.com/ADIVIDAN1012/Beacon-Labs/issues)

---

**Made with ❤️ by the Beacon Team**

*Light the way with Beacon* 🔥
