# Beacon Programming Language — Syntax

## Variable Assignment


var = 10
name = ask("Enter your name: ")
flag = off    <false boolean value>


---

## Data Types and Conversions

- Dynamic typing like Python
- Use convert variable to DataType for type conversion


Integer = convert val to num
flt = convert val to decim
txt = convert val to text
bitflag = convert val to bit


---

## Input / Output


name = ask("Enter your name: ")
show("Hello, {name}")
show("Welcome!")   <works without variables too>


> Beacon supports embedded variables in strings using {} syntax similar to Python f-strings but **without needing the f"" prefix**.

---

## Functions

- Define functions using spec
- Use funcall to call functions (optional for simple calls, recommended for clarity on complex calls)
- Use forward to return values


spec greet():
    show("Hello World")

funcall greet()

spec add(a, b):
    forward a + b

result = funcall add(5, 3)
show("Sum is {result}")


---

## Control Flow

### Conditional Statements


check x > 10:
    show("Greater than 10")
alter x == 10:
    show("Equal to 10")
altern:
    show("Less than 10")


### Loops

- Use until instead of while


i = 0
until i > 10:
    show("Count {i}")
    i = i + 1


- Use traverse keyword from start to end instead of for


traverse i from 1 to 5:
    show("Number {i}")


---

## Error Handling


attempt:
    <risky code here>
trap ErrorType as e:
    show("Error occurred: {e}")
conclude:
    show("This runs always")


---

## Keywords and Operators (Partial)

| Beacon Keyword | Python Equivalent | Notes                             |
|--------------|-------------------|----------------------------------|
| spec         | def               | function definition              |
| funcall      | ()                | function call                   |
| forward      | return            | return value                    |
| check        | if                | conditional                    |
| alter        | elif              | else if                       |
| altern       | else              | else                         |
| until        | while             | loop                         |
| traverse     | for               | for loop                    |
| ask          | input             | input                        |
| show         | print             | output                       |
| condense     | reduce            | reduce/fold                 |
| authen       | authentication    | auth check                 |
| off          | False             | boolean false                 |
| both         | and               | logical AND                   |
| no           | not               | logical NOT                   |
| either       | or                | logical OR                    |
| erase        | del               | delete variable              |
| ignore       | continue          | continue                    |
| skip         | break             | break                      |
| spill        | yield             | yield                      |
| source       | from              | import from                |
| universal    | global            | global                    |
| within       | in                | membership                |
| equal        | is                | identity                  |

---

## Comments

- Single-line comment:


< This is a single-line comment >


- Multi-line comment:


<^
This is
a multi-line comment
^>


---

## Notes

- Assignment uses =, not a keyword.
- Dynamic typing means no need for explicit variable declaration keywords.
- String interpolation uses {} without f"".
- Use funcall optionally for clarity in function calls.
- convert variable to Type is the syntax for type conversion.
- Keywords have unique synonyms to avoid clashes and keep language clean.
