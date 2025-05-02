# Dyno Programming Language Syntax

Dyno is a user-oriented, Python-inspired programming language designed for simplicity and intuitiveness. This document outlines the core syntax and keywords used in Dyno.

## Control Flow

### check (in place of if)
Used for conditional checks.

```dyno
check condition:
    // Code to execute if condition is true

alter (in place of elif)

Used for additional conditions.

check condition:
    // Code to execute if condition is true
alter condition:
    // Code to execute if condition is true

altern (in place of else)

Used for the fallback condition.

check condition:
    // Code to execute if condition is true
alter condition:
    // Code to execute if condition is true
altern:
    // Code to execute if no conditions were true

Loops

traverse (in place of for)

Used to iterate through a range or collection.

traverse V from 1 to 9:
    // Code to execute in each iteration

until (in place of while)

Used to run a loop until a condition is false.

until condition:
    // Code to execute while condition is true

Functions

spec (in place of def)

Used to define functions.

spec function_name(parameters):
    // Function body

prep (in place of init)

Used for constructors in classes (blueprints).

prep constructor_name():
    // Constructor body

Error Handling

authen (in place of try)

Used for error handling, similar to try.

authen:
    // Code that may raise an error

trap (in place of catch)

Used to trap and handle errors.

authen:
    // Code that may raise an error
trap:
    // Code to execute if an error occurs

trigger (in place of raise)

Used to trigger an error.

trigger error_type:
    // Code to trigger an error

File I/O

fetch (in place of read)

Used to read data from a file.

fetch file_name:
    // Code to fetch data from the file

modify (in place of write)

Used to write data to a file.

modify file_name data:
    // Code to modify the file with data

Data Types

Dyno supports standard data types as shown below:

int: Integer data type

float: Floating point number

double: Double precision floating point number

long: Long integer


Comments

Dyno uses unique syntax for comments:

Single-line comment

< This is a single-line comment >

Multi-line comment

<^ This is a multi-line comment
   spanning multiple lines of comment ^>

Accessing Data

get (in place of dot operator)

Used to access properties or methods in an object.

object - property

Type Conversion

convert (in place of type casting)

Used to convert a variable to a desired type.

convert variable to type

Miscellaneous

vol (in place of len)

Used to get the length of a collection or string.

vol collection

nil (in place of null)

Used to represent a null value.

variable = nil
