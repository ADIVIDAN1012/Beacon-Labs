# Release Notes - v1.1.0: Dynamic Type Conversion

## 🎉 New Feature: Automatic Type Detection in `ask()`

The `ask()` function now automatically detects and converts user input to the appropriate data type, making Beacon even more intuitive and user-friendly!

### ✨ What's New

**Dynamic Type Conversion**
- `ask()` now intelligently converts input based on content
- Works exactly like Python's `input()` but with automatic type detection
- No need for manual `convert ... to ...` for common types

### 🔧 Type Detection Rules

| Input | Detected Type | Example |
|-------|---------------|---------|
| `42` | Number | `firm age = ask("Age: ")` → 42 (Num) |
| `3.14` | Number | `firm pi = ask("Pi: ")` → 3.14 (Num) |
| `On` | Boolean | `firm active = ask("Active: ")` → true |
| `Off` | Boolean | `firm disabled = ask("Disabled: ")` → false |
| `Nil` | Nil | `firm empty = ask("Empty: ")` → Nil |
| `hello` | Text | `firm name = ask("Name: ")` → "hello" |
| `123abc` | Text | Mixed alphanumeric → "123abc" |

### 📝 Usage Examples

```beacon
spec main() {
    < Automatically converts to number >
    firm age = ask("Enter your age: ")
    
    < Automatically converts to boolean >
    firm active = ask("Are you active? (On/Off): ")
    
    < Stores as text >
    firm name = ask("Enter your name: ")
}
```

### 🔨 Implementation Details

**Frontend Changes:**
- Updated `parser.py` to recognize `ask()` as callable expression
- Modified to support both `ask("prompt")` and legacy `ask { }` syntax

**Backend Changes:**
- Added `detect_and_convert_type()` function in `main.c`
- Implemented automatic type detection with `strtod()` for numbers
- Added AskNode JSON parser support

**Documentation:**
- Updated `README.md` with feature documentation
- Updated `builtins.md` with new `ask()` behavior
- Added comprehensive examples

### 📦 Download

**BPL.exe** (Windows Executable)
- Fully compiled standalone executable
- Includes C backend with type conversion
- No dependencies required

### 🐛 Bug Fixes
- Fixed parser to support `ask()` in expression contexts
- Updated frontend to use correct backend executable name

### 📚 Documentation
- [README.md](README.md) - Updated with dynamic type conversion feature
- [builtins.md](builtins.md) - Updated ask() documentation

---

**Full Changelog**: See commit history for detailed changes

**Installation**: Download `BPL.exe` and run your `.bpl` files:
```bash
BPL.exe your_program.bpl
```
