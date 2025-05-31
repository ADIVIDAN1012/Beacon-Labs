# Dyno Programming Language - Keywords

A complete and user-oriented synonym table of Dyno keywords and their standard language equivalents (especially Python).

---

## Access Control

| Dyno Keyword | Equivalent        |
|--------------|------------------|
| avail        | public           |
| shel         | protected        |
| covnito      | private          |
| internal     | package access   |
| expose       | public/internal  |
| universe     | global           |
| outer        | nonlocal         |

---

## Function & Scope

| Dyno Keyword | Equivalent        |
|--------------|------------------|
| spec         | def              |
| den          | lambda           |
| funcall      | function call    |
| forward      | return           |
| provide      | yield            |
| scope()      | range()          |

---

## Logic Operators

| Dyno Keyword | Equivalent |
|--------------|-----------|
| also         | and       |
| either       | or        |
| no           | not       |
| alike        | is        |
| within       | in        |
| by           | as        |

---

## Conditional Blocks

| Dyno Keyword | Equivalent |
|--------------|-----------|
| check        | if        |
| alter        | elif      |
| altern       | else      |
| proceed      | pass      |

---

## Looping

| Dyno Keyword            | Equivalent |
|-------------------------|-----------|
| traverse v from x to y  | for       |
| until                   | while     |
| leave                   | break     |
| skip                    | continue  |

---

## Error Handling

| Dyno Keyword | Equivalent |
|--------------|-----------|
| attempt      | try       |
| trap         | catch     |
| conclude     | finally   |
| trigger      | raise     |
| peek         | error obj |

---

## Data Types

| Dyno Type | Equivalent |
|-----------|------------|
| bit       | bool       |
| num       | int        |
| decim     | float      |
| text      | str        |
| seal      | tuple      |
| bind      | tuple      |
| list      | list       |
| dict      | dict       |
| nil       | None       |
| on        | True       |
| off       | False      |

---

## Input/Output

| Dyno Keyword | Equivalent | Purpose                        |
|--------------|------------|--------------------------------|
| ask()        | input()    | Smart type-aware input         |
| show()       | print()    | Display output to user         |
| solve()      | eval()     | Evaluate an expression         |
| tag()        | enumerate()| Tag items with index           |

---

## Type Checking & Conversion

| Dyno Keyword        | Equivalent    |
|---------------------|---------------|
| kind()              | type()        |
| convert x to DT     | type cast     |

---

## File Handling

| Dyno Keyword | Equivalent |
|--------------|------------|
| fetch        | read       |
| modify       | write      |
| inlet        | open       |
| seal         | close      |

---

## Concurrency / Parallelism

| Dyno Keyword | Equivalent |
|--------------|------------|
| paral        | async      |
| hold         | await      |
| flux         | flow       |
| barrier      | lock       |
| permit       | semaphore  |
| signal       | event      |

---

## System & Environment

| Dyno Keyword | Equivalent |
|--------------|------------|
| plug         | import     |
| share        | export     |
| toolkit      | module     |
| source       | from       |
| embed        | embed      |
| bloc         | batch      |
| link         | join       |
| belong       | belong to  |
| infuse       | inject     |
| bridge       | interface  |

---

## OOP & Inheritance

| Dyno Keyword | Equivalent    |
|--------------|---------------|
| blueprint    | class         |
| adopt        | extends/inherit |
| prep         | constructor/init |
| own          | self/this     |
| father       | base class    |
| child        | derived class |
| skelet       | abstract class|

---

## Math & Transformation

| Dyno Keyword | Equivalent    |
|--------------|---------------|
| absol(x)     | abs(x)        |
| roff(x)      | round(x)      |
| exponent(x, y)| pow(x, y)    |
| transform    | map           |
| condense     | reduce        |

---

## Debugging & Tracing

| Dyno Keyword | Equivalent       |
|--------------|------------------|
| track        | debug            |
| trace        | trace            |
| watch        | watch variables  |

---

## Data Serialization

| Dyno Keyword | Equivalent   |
|--------------|--------------|
| pack         | serialize    |
| unpack       | deserialize  |

---

## Event Handling

| Dyno Keyword | Equivalent |
|--------------|------------|
| listen       | bind       |
| trigger      | emit       |

---

✅ **Notes**
- All keywords are lowercase by convention.
- Only **keywords** are reserved. Function-like features such as `ask()` and `show()` behave like built-ins but are not reserved unless stated.
- `funcall` is **optional** and used only in ambiguous or complex function call scenarios.

---

🧠 Let me know if you'd like this pushed directly to your GitHub or formatted as a downloadable `.md` file.