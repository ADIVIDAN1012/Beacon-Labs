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
name = ask("Enter your name: ")

---

## Classes & Objects

Blueprint Dog {
    Spec speak() {
        Show("{name} barks")
    }
}

Adopt Poodle from Dog {
    Spec speak() {
        Show("{name} yaps")
    }
}

Crate Point {
    Facet x
    Facet y
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

Hidden Spec secret() {
    < Only accessible within the class >
}

Avail Spec public_func() {
    Show("This is public")
}

Shielded Facet internal_id

Internal Spec pkg_func() {
    < Restricted to package >
}

Expose Spec api() {
    < Publicly exposed function >
}

---

## Control Flow & Loops

Check x > 0 {
    Show("Positive")
} Alter x == 0 {
    Show("Zero")
} Altern {
    Show("Negative")
}

Select color {
    Option "red" {
        Show("Red!")
    }
    Option "blue" {
        Show("Blue!")
    }
}

Traverse i from 1 to 5 {
    Show(i)
}

Until x > 10 {
    x = x + 1
}

Within x in [1,2,3] {
    Show(x)
}

Scope i from 0 to 10 {
    Show(i)
}

Halt     < break >
Proceed  < continue >
Wait     < pass >
Leap     < goto >
Mark     < label >
Be a Be b

---

## Error Handling

Attempt {
    risky_op()
} Trap Blame as e {
    Show("Error: {e}")
} Conclude {
    Show("Cleanup always runs")
}

Peek error
Blame MyError("fail")

---

## Boolean, Null, Identity

On
Off
Nil

---

## Import/Export/Modules

Plug math
Share Spec api() {
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
    Show("In a block")
}

Embed resource "logo.png"

Bridge Drawable {
    Spec draw()
}

Link a, b
Infuse config

Universal counter

Launch main() {
    Show("Starting program!")
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

< End of Syntax Reference ># Beacon Programming Language – Complete Syntax Reference

<^
This document describes the syntax of every Beacon language keyword and major feature.
Each Beacon keyword replaces a mainstream programming keyword with the same structure, but blocks always use { }.
No indentation or : is required for blocks.
Comments use < ... > and <^ ... ^>.
^>

---

## Variable Assignment

num = 10
name = ask("Enter your name: ")

---

## Classes & Objects

Blueprint Dog {
    Spec speak() {
        Show("{name} barks")
    }
}

Adopt Poodle from Dog {
    Spec speak() {
        Show("{name} yaps")
    }
}

Crate Point {
    Facet x
    Facet y
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

Hidden Spec secret() {
    < Only accessible within the class >
}

Avail Spec public_func() {
    Show("This is public")
}

Shielded Facet internal_id

Internal Spec pkg_func() {
    < Restricted to package >
}

Expose Spec api() {
    < Publicly exposed function >
}

---

## Control Flow & Loops

Check x > 0 {
    Show("Positive")
} Alter x == 0 {
    Show("Zero")
} Altern {
    Show("Negative")
}

Select color {
    Option "red" {
        Show("Red!")
    }
    Option "blue" {
        Show("Blue!")
    }
}

Traverse i from 1 to 5 {
    Show(i)
}

Until x > 10 {
    x = x + 1
}

Within x in [1,2,3] {
    Show(x)
}

Scope i from 0 to 10 {
    Show(i)
}

Halt     < break >
Proceed  < continue >
Wait     < pass >
Leap     < goto >
Mark     < label >
Be a Be b

---

## Error Handling

Attempt {
    risky_op()
} Trap Blame as e {
    Show("Error: {e}")
} Conclude {
    Show("Cleanup always runs")
}

Peek error
Blame MyError("fail")

---

## Boolean, Null, Identity

On
Off
Nil

---

## Import/Export/Modules

Plug math
Share Spec api() {
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
    Show("In a block")
}

Embed resource "logo.png"

Bridge Drawable {
    Spec draw()
}

Link a, b
Infuse config

Universal counter

Launch main() {
    Show("Starting program!")
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

< End of Syntax Reference ># Beacon Programming Language – Complete Syntax Reference

<^
This document describes the syntax of every Beacon language keyword and major feature.
Each Beacon keyword replaces a mainstream programming keyword with the same structure, but blocks always use { }.
No indentation or : is required for blocks.
Comments use < ... > and <^ ... ^>.
^>

---

## Variable Assignment

num = 10
name = ask("Enter your name: ")

---

## Classes & Objects

Blueprint Dog {
    Spec speak() {
        Show("{name} barks")
    }
}

Adopt Poodle from Dog {
    Spec speak() {
        Show("{name} yaps")
    }
}

Crate Point {
    Facet x
    Facet y
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

Hidden Spec secret() {
    < Only accessible within the class >
}

Avail Spec public_func() {
    Show("This is public")
}

Shielded Facet internal_id

Internal Spec pkg_func() {
    < Restricted to package >
}

Expose Spec api() {
    < Publicly exposed function >
}

---

## Control Flow & Loops

Check x > 0 {
    Show("Positive")
} Alter x == 0 {
    Show("Zero")
} Altern {
    Show("Negative")
}

Select color {
    Option "red" {
        Show("Red!")
    }
    Option "blue" {
        Show("Blue!")
    }
}

Traverse i from 1 to 5 {
    Show(i)
}

Until x > 10 {
    x = x + 1
}

Within x in [1,2,3] {
    Show(x)
}

Scope i from 0 to 10 {
    Show(i)
}

Halt     < break >
Proceed  < continue >
Wait     < pass >
Leap     < goto >
Mark     < label >
Be a Be b

---

## Error Handling

Attempt {
    risky_op()
} Trap Blame as e {
    Show("Error: {e}")
} Conclude {
    Show("Cleanup always runs")
}

Peek error
Blame MyError("fail")

---

## Boolean, Null, Identity

On
Off
Nil

---

## Import/Export/Modules

Plug math
Share Spec api() {
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
    Show("In a block")
}

Embed resource "logo.png"

Bridge Drawable {
    Spec draw()
}

Link a, b
Infuse config

Universal counter

Launch main() {
    Show("Starting program!")
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