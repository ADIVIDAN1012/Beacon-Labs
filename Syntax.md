# Dyno Syntax Reference

---

## Variables and Data Types

Dyno is dynamically typed. You don't need to declare types explicitly. Variables are assigned using the = operator.


x = 42
name = "Dyno"
flag = true
data = [1, 2, 3]


### Type Conversion


convert x to float
convert val to string


### Type Checking


kind(x)


---

## Functions

Use spec to define a function. Use send to return a value.


spec greet():
    output("Hello")

spec add(a, b):
    send a + b


Call functions with funcall.


funcall greet()


---

## Conditionals

Use check, alter, and altern:


check x > 0:
    output("Positive")
alter x == 0:
    output("Zero")
altern:
    output("Negative")


---

## Loops

### Traverse Loop (like for)


traverse i from 1 to 5:
    output(i)


### Until Loop (like while)


until x == 5:
    x = x + 1


---

## Error Handling


attempt:
    riskyFunc()
trap error:
    output("Error occurred")
conclude:
    output("Done")


---

## Object Orientation

Use blueprint for classes. prep defines the constructor. own refers to the current object.


blueprint Person:
    prep(n):
        own.name = n
    spec greet():
        output("Hi, I am " + own.name)


Use adopt for inheritance:


blueprint Student adopt Person:
    prep(n, id):
        Person.prep(n)
        own.id = id


---

## User-Oriented Programming (UOP)

Use bridge to define user interaction interfaces.


bridge Login:
    ask username
    ask password
    send authen(username, password)


---

## Lambda Functions

Use den:

square = den x: x * x


---

## Comments

Single-line:

< This is a comment >


Multi-line:
<^
This is a 
multi-line comment
^>


---

## File I/O


fetch("file.txt")
modify("file.txt", content)


---

## Other Keywords

- flux – for control flow management
- trap, trigger – for error handling
- bloc – for grouped code execution
- peek() – access value without altering
- belong() – membership check
- infuse() – insert or push into collections
- tag() – enumerate elements
- track() – log or trace behaviour
- forward – send data from functions
- plug – load or connect toolkits
- toolkit – collection of reusable code
- link – join collections
- bridge – user interface definition
- decon – deconstruct data
- skelet – structure declaration
- procsys – encapsulated logic (procedures)
