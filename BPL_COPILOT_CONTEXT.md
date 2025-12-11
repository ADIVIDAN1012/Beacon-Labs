# Beacon Programming Language (BPL) v2.0 Context

**Overview**
Beacon (BPL) is a custom interpreted language with a Python frontend (Lexer/Parser) and a C-based Runtime (Interpreter). It communicates via a JSON AST.

## 1. Syntax & Structure

### Comments
- **Single-line:** `< This is a comment >`
- **Multi-line:** `<^ This is a 
multi-line comment ^>`

### Variables & Constants
- **Constants:** `firm name = value` (Immutable)
- **Variables:** `name = value` (Mutable, created on assignment)
- **Types:** `Num` (Integer/Float), `Text` (String), `On`/`Off` (Boolean), `Nil`
- **String Interpolation:** `"Value: |variable|"`

### Collections (Packs)
- **Syntax:** `pack(item1, item2, ...)`
- **Access:** `list~>0` (The `~>` operator is the **exclusive** access operator; `.` is invalid)
- **Example:**
  ```beacon
  firm numbers = pack(1, 2, 3)
  firm mixed = pack("A", 42, On)
  ```

### Control Flow
**Conditionals:**
```beacon
when x > 10:
    show "High"
otherwise when x > 5:
    show "Medium"
otherwise:
    show "Low"
done
```

traverse i from 1 to 10:
    show i
done

traverse num from 1 to numbers~>count:
    show numbers~>num
done
```

### Functions
- **Keyword:** `spec`
- **Return:** `forward value` or `giving value` (deprecated)
```beacon
spec add(a, b):
    forward a + b
done

firm result = add(10, 20)
```

### Error Handling
```beacon
attempt:
    trigger "ErrorName"
trap "ErrorName":
    show "Caught error"
done
```

## 2. Object-Oriented Programming (OOP)

### Blueprints (Classes)
```beacon
blueprint Dog:
    has name
    has age

    < Constructor >
    prep (n, a):
        own~>name = n
        own~>age = a
    done

    < Method >
    spec bark:
        show "|own~>name| says Woof!"
    done
done
```

### Instantiation & Usage
```beacon
< Spawn creates instance >
firm myDog = spawn Dog("Buddy", 5)

< Method call >
myDog~>bark()

< Attribute access >
show myDog~>age
```

## 3. Modules
- **Import:** `bring "module_name"`
- **Toolkit (Library):** `toolkit Math:` ... `done`

## 4. Execution Model
1. **Frontend (Python):** Parses `.bpl` -> Generates `.bpl.json` (AST).
2. **Runtime (C):** Loads `.bpl.json` -> Executes logic.
   - **Performance:** Near-native C execution.
   - **Memory:** Reference counting / Manual scope management (v2.0).

## 5. Key Keywords
`firm`, `show`, `spec`, `prep`, `blueprint`, `spawn`, `pack`, `each`, `when`, `otherwise`, `attempt`, `trap`, `trigger`, `forward`, `own`, `adopt` (Inheritance).
