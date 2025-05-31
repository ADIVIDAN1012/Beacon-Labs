# Dyno Programming Language – Keywords

This document outlines the **keywords** and **built-in functions** used in the Dyno programming language.

---

## 🧩 Keywords

### Access Control
| Dyno Keyword | Equivalent           |
|--------------|----------------------|
| Covnito      | private              |
| Shel         | protected            |
| Avail        | public               |
| Internal     | package-level access |
| Expose       | internal/public exposure |

### Concurrency / Parallelism
| Dyno Keyword | Equivalent   |
|--------------|--------------|
| Paral        | async        |
| Hold         | await        |
| Flux         | flow         |
| Barrier      | lock         |
| Permit       | semaphore    |
| Signal       | event        |

### Control Flow
| Dyno Keyword | Equivalent |
|--------------|------------|
| Check        | if         |
| Alter        | elif       |
| Altern       | else       |
| Choose       | switch     |
| When         | case       |
| Conclude     | finally    |
| Attempt      | try        |
| Trap         | catch      |

### Inheritance & Class
| Dyno Keyword | Equivalent     |
|--------------|----------------|
| Adopt        | inheritance    |
| Father       | base class     |
| Child        | derived class  |
| Blueprint    | class          |
| Skelet       | abstract class |

### System / Environment
| Dyno Keyword | Equivalent           |
|--------------|----------------------|
| Plug         | import               |
| Share        | export               |
| Toolkit      | module               |
| Bloc         | block/batch operation|
| Embed        | embed resources      |
| Bridge       | interface            |
| Link         | join                 |
| Belong       | belongs to           |
| Infuse       | inject/populate      |

### Error Handling
| Dyno Keyword | Equivalent | Purpose                 |
|--------------|------------|-------------------------|
| Attempt      | try        | Begin risky code block  |
| Trap         | catch      | Catch errors            |
| Conclude     | finally    | Always executes block   |
| Trigger      | raise      | Manually raise an error |
| Check        | if (error) | Conditional in error block|
| Peek         | exception  | View error info         |

---

## ⚙️ Built-in Functions

### User I/O
| Function  | Equivalent | Purpose                          |
|-----------|------------|----------------------------------|
| ask()     | input()    | Ask for user input and auto-cast |
| output()  | print()    | Output text/data to console       |

### Type Handling and Conversion
| Function           | Equivalent | Purpose                          |
|--------------------|------------|----------------------------------|
| kind()             | type()     | Return data type of value        |
| convert v to DT    | type cast  | Convert variable v to data type  |

### Data Transformation
| Function     | Equivalent | Purpose                                   |
|--------------|------------|-------------------------------------------|
| transform()  | map()      | Apply function to each item in iterable   |
| condense()   | reduce()   | Aggregate iterable into a single value    |

### Data Serialization
| Function  | Equivalent    | Purpose                                  |
|-----------|---------------|------------------------------------------|
| pack()    | serialize()   | Convert object to storable format        |
| unpack()  | deserialize() | Restore data from serialized format      |

### Debugging and Logging
| Function  | Purpose                            |
|-----------|------------------------------------|
| track()   | Print debug information            |
| trace()   | Trace code execution path          |
| watch()   | Observe variable value changes     |

### File Handling
| Function  | Equivalent | Purpose                 |
|-----------|------------|-------------------------|
| fetch()   | read()     | Read contents from file  |
| modify()  | write()    | Write contents to file   |
| inlet()   | open()     | Open a file             |
| seal()    | close()    | Close an open file      |

---

# Notes

- Keywords like `kind()`, `ask()`, `output()`, `transform()`, `condense()` etc. are **functions** and always include parentheses in usage.
- Keywords like `Check`, `Alter`, `Altern`, `Choose`, `When` etc. are **control flow keywords** and used without parentheses.
- The keyword `convert` is used with syntax: `convert v to DT` where `v` is a variable and `DT` is a type.
- The keyword `Choose` is the Dyno synonym for `switch` and `When` is the synonym for `case`.
- `condense()` is the unique synonym for `reduce()` to avoid conflicts with reserved words.
- Error handling keywords include `Attempt` (try), `Trap` (catch), `Conclude` (finally), `Trigger` (raise), and `Peek` for exception inspection.

---

This file is a living document and will be updated as Dyno evolves.