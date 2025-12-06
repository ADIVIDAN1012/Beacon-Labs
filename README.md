# 🔥 Beacon Programming Language

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![C](https://img.shields.io/badge/C-GCC-green.svg)](https://gcc.gnu.org/)

**Beacon** is a revolutionary programming language built on **UOP (Universal User-Oriented Programming)**—a paradigm that prioritizes **human readability**, **intuitive syntax**, and **natural language constructs**. Unlike traditional languages that focus on machine-oriented optimizations, Beacon makes coding feel like a conversation between developer and computer.

> [!NOTE]
> Beacon is actively under development. Core features are stable and functional, while advanced features (concurrency, modules) are experimental. See [Implementation Status](#-implementation-status) below.

Beacon combines the power of modern programming with unprecedented clarity:
- **Dynamically-Typed** with runtime safety
- **Object-Oriented** with blueprints and inheritance  
- **Concurrency-First** with parallel programming primitives
- **Human-Centric** keywords that read like plain English

This repository contains the complete Beacon toolchain:
- **Python-based Frontend:** Lexer, parser, and AST generator
- **C-based Backend:** AST interpreter and runtime execution engine
- **VS Code Extension:** Syntax highlighting and language support
- **Documentation:** Comprehensive language specification and guides

---

## ✨ Key Features

### 🌟 UOP (Universal User-Oriented Programming)
Beacon's foundational philosophy that sets it apart from traditional languages:

- **Human-Centric Keywords:** Natural words like `ask` (input), `show` (print), `check` (if), `attempt` (try)
- **Intuitive Structure:** Code that follows the logical flow of human thought
- **Clarity Over Brevity:** Self-documenting code that reads like plain language
- **Universal Accessibility:** Approachable for beginners, powerful for experts

**Traditional OOP vs. Beacon UOP:**
```python
# Traditional Python (OOP)
try:
    result = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
```

```beacon
# Beacon (UOP)
attempt {
    result = convert ask("Enter number: ") to Num
} trap {
    show("Invalid input")
}
```

---

## 🚀 Implementation Status

> [!IMPORTANT]
> Beacon is actively under development. Below is a clear breakdown of **stable**, **experimental**, and **planned** features.

### ✅ Stable & Production-Ready

These features are **fully implemented and tested**:

#### Core Language
- **Variables & Constants:** `firm` declarations
- **Functions:** `spec` (functions), `forward` (return), function calls
- **I/O:** `show` (output), `ask` (input with **automatic type detection**)
- **Comments:** Single-line `< ... >`, multi-line `<^ ... ^>`, docstrings with `note`

> [!TIP]
> **Dynamic Type Conversion:** The `ask()` function automatically detects and converts user input to the appropriate type:
> - Numbers: `"42"` → `Num`, `"3.14"` → `Num`
> - Booleans: `"On"` → `true`, `"Off"` → `false`
> - Nil: `"Nil"` → `Nil`
> - Text: Everything else defaults to `Text`
>
> Example: `firm age = ask("Enter age: ")` - automatically converts numeric input!

#### Control Flow
- **Conditionals:** `check` (if), `alter` (else if), `altern` (else)
- **Loops:** `traverse` (for), `until` (while)
- **Loop Control:** `halt` (break), `proceed` (continue), `wait` (pass)

#### Error Handling
- **Try-Catch-Finally:** `attempt`, `trap`, `conclude`
- **Error Raising:** `trigger`
- **Error Inspection:** `peek` for error details

#### Data Types & Operators
- **Literals:** `Num`, `Text`, `On` (true), `Off` (false), `Nil` (null)
- **Type Conversion:** `convert ... to ...`
- **Operators:** Arithmetic (`+`, `-`, `*`, `/`), comparison (`==`, `'=`, `<`, `>`, `<=`, `>=`)
- **String Interpolation:** `"text |expression| more text"`

#### Object-Oriented Programming
- **Classes:** `blueprint` (class declaration)
- **Properties:** `shard` (fields)
- **Constructors:** `prep`
- **Self-Reference:** `own` (self/this)
- **Inheritance:** `adopt` (extends)
- **Object Creation:** `spawn` keyword

### ⚠️ Experimental Features

These features have **parser support** but require further testing and validation:

- ⚠️ **Module System:** `toolkit`, `plug`, `share` (grammar exists, file loading needs testing)
- ⚠️ **Concurrency:** `paral`, `hold`, `signal`, `listen` (keywords recognized, runtime implementation under development)
- ⚠️ **Interfaces:** `bridge`, `expose`, `link`, `embed` (parsed, runtime contracts need validation)
- ⚠️ **Access Modifiers:** `hidden`, `shielded`, `internal` (keywords exist, enforcement needs testing)
- ⚠️ **Static Members:** `solid` (keyword recognized, functionality needs verification)

### 🚧 Planned Features

Advanced features being developed:

- 🚧 **Anonymous Functions:** `den` (lambda expressions)
- 🚧 **Functional Programming:** `transform` (map), `condense` (reduce)
- 🚧 **Serialization:** `pack`, `unpack`
- 🚧 **Assertions:** `authen`
- 🚧 **Type Aliases:** `nick ... as ...`

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
- **[UOP (Universal Object Oriented Programming)](UOP.md)** - UOP paradigm and user-centric design documentation

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

> [!NOTE]
> The following examples demonstrate **stable, tested features**. See [Examples.md](Examples.md) for more comprehensive tutorials.

### Hello World
```beacon
spec greet(name) {
    show("Hello, " + name + "!")
}

greet("World")
```

### Variables and Conditionals
```beacon
spec check_greater(val) {
    check (val > 5) {
        show("val is greater than 5")
    } altern {
        show("val is not greater than 5")
    }
}

firm a = 10 
funcall check_greater(a)
funcall check_greater(3)
```

### Type Conversion
```beacon
x = On
y = Off
z = Nil

check(x == On) {
    show("x is On")
}

a = convert 10 to Text
show("Number as text: " + a)
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

### Loops
```beacon
spec list_numbers() {
    traverse i from 1 to 5 {
        show("Number: " + convert i to Text)
    }
}

list_numbers()
```

> [!TIP]
> For advanced examples including OOP, modules, and concurrency (experimental features), see the [Examples.md](Examples.md) documentation.

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

### Testing & Verification

To verify if a feature works:

1. **Write a test:** Create a `.bpl` file using the feature
2. **Compile:** Run `py frontend.py yourtest.bpl` to generate `ast.json`
3. **Execute:** Run `.\main.exe ..\ast.json` from `compiler_backend_c`
4. **Verify:** Does it produce the expected output?

See **[IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md)** for detailed feature status and testing recommendations.

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
