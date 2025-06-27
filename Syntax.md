# Beacon Programming Language – Complete Syntax Reference

<^
This document describes the syntax of every Beacon language keyword and major feature.
Each Beacon keyword replaces a mainstream programming keyword with the same structure, but blocks always use { }.
No indentation or : is required for blocks.
Comments use < ... > and <^ ... ^>.
^>

---

## Variable Assignment

num = 10
name = ask("Enter}

Adopt Dog from Animal {
    Spec speak() {
        show("{name} barks")
    }
}

Crate Point {
    facet x
    facet y
}

Facet age
Fetch age
Assign age

Morph operator +(a, b) {
    Forward a.value + b.value
}

Model T

---

## Constants and Statics

Firm PI = 3.14
Solid counter = 0

---

## Access Control

Covnito spec secret() {
    < Only accessible within the class >
}

Avail spec public_func() {
    show("This is public")
}

Shel facet internal_id

Internal spec pkg_func() {
    < Restricted to package >
}

Expose spec api() {
    < Publicly exposed function >
}

---

## Control Flow

Check x > 0 {
    show("Positive")
} Alter x == 0 {
    show("Zero")
} Altern {
    show("Negative")
}

Select color {
    Option "red" {
        show("Red!")
    }
    Option "blue" {
        show("Blue!")
    }
}

Traverse i from 1 to 5 {
    show(i)
}

Until x > 10 {
    x = x + 1
}

Within x in [1,2,3] {
    show(x)
}

Scope i from 0 to 10 {
    show(i)
}

---

## Loops and Loop Control

Traverse i from 1 to 5 {
    if i == 3 {
        Skip
    }
    show(i)
}

Until x < 5 {
    Ignore
    x = x - 1
}

---

## Try/Catch/Finally (Error Handling)

Attempt {
    risky_op()
} Trap Blame as e {
    show("Error: {e}")
} Conclude {
    show("Cleanup always runs")
}

Peek error
Blame MyError("fail")
Trigger Blame("fail")

---

## Boolean, Null, Identity

On
Off
Nil

Be a Be b

---

## Import/Export/Modules

Plug math
Share spec api() {
    < Exported function >
}

Toolkit utils

Source math from "toolkit/math"

---

## File Handling

Inlet file = open("data.txt")
Fetch line = file.Fetch()
Modify file.Modify("New data")
Seal file

---

## User I/O

Ask name = ask("Enter your name: ")
Show("Welcome, {name}")

---

## Serialization

Pack data = Pack(obj)
Unpack obj = Unpack(data)

---

## Event Handling

Listen button.Click, handler
Trigger event

---

## Debugging/Logging

Track("Debug info")
Trace("Tracing execution")
Watch var

---

## System/Environment Operations

Bloc {
    Plug math
    show("In a block")
}

Embed resource "logo.png"

Bridge Drawable {
    Spec draw()
}

Link a, b
Infuse config

Universal counter

Launch main() {
    show("Starting program!")
}

---

## Memory Management

Slip ptr
Wipe cache

---

## Generics

Model T

---

## Lambda (Anonymous Functions)

Den = (a, b) => a + b

---

## Comments

< This is a single-line comment >

<^
This is a multi-line comment.
Spanning multiple lines.
^>

Note: "This is a docstring for a function or class"

---

## Enum/Tag

Tag Color {
    RED
    BLUE
}

---

## Miscellaneous Operations

Authen x == y
Transform arr, f
Condense arr, f
Solve expr

---

< End of Syntax Reference >