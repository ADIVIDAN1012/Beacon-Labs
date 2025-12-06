# 🔥 Beacon Programming Language

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

**Beacon** is a revolutionary programming language built on **UOP (Universal User-Oriented Programming)**. It prioritizes **human readability** and **intuition**, making coding feel like a natural conversation.

> [!NOTE]
> Beacon is actively under development. Core features are stable, but advanced features like concurrency are experimental.

---

## ✨ Why Beacon?

- **Human-Centric:** Uses natural keywords like `ask`, `show`, `check`, and `attempt`.
- **Readability First:** Code reads like plain English, reducing cognitive load.
- **Modern Power:** Object-oriented, dynamic typing, and concurrency-ready.

### UOP in Action

**Traditional Python:**
```python
try:
    result = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
```

**Beacon:**
```beacon
attempt {
    result = convert ask("Enter number: ") to Num
} trap {
    show("Invalid input")
}
```

---

## 🚀 Getting Started

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ADIVIDAN1012/Beacon-Labs.git
   cd Beacon-Labs
   ```

2. **Build the Runtime:**
   ```bash
   cd compiler_backend_c
   .\build.bat
   cd ..
   ```

### Running Your First Program

1. Create a file named `hello.bpl`:
   ```beacon
   show("Hello, Beacon! 🔥")
   ```

2. Run it (Frontend -> Backend):
   ```bash
   # Generate AST
   py compiler_frontend_py/frontend.py hello.bpl
   
   # Run Interpreter
   .\compiler_backend_c\main.exe ast.json
   ```

---

## 💡 Examples

### String Interpolation
```beacon
firm name = "Adi"
show("Hello |name|!") 
```

### Functions
```beacon
spec greet(name) {
    show("Hello, |name|!")
}

greet("World")
```

### Conditionals
```beacon
firm x = 10
check (x > 5) {
    show("x is distinct")
}
```

### Loops
```beacon
traverse i from 1 to 5 {
    show("Count: |i|")
}
```

> [!TIP]
> See **[Examples.md](docs/Examples.md)** for more tutorials and advanced usage!

---

## 📚 Documentation

- **[Keywords Reference](docs/Keywords.md)**
- **[Syntax Guide](docs/Syntax.md)**
- **[Built-in Functions](docs/builtins.md)**
- **[UOP Specification](docs/UOP.md)**

For developers interested in contributing, please see **[CONTRIBUTING.md](docs/CONTRIBUTING.md)**.

---

**Made with ❤️ by the Beacon Team**
*Light the way with Beacon* 🔥
