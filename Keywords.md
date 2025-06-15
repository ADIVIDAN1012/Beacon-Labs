# Dyno Programming Language - Keywords

## Access Control
Dyno Keyword    | Equivalent
----------------|-----------------------
Covnito         | Private
Shel            | Protected
Avail           | Public
Internal        | Package-level access
Expose          | Internal/Public exposure

## Concurrency/Parallelism
Dyno Keyword    | Equivalent
----------------|-----------------------
Paral           | Async
Hold            | Await
Flux            | Flow
Barrier         | Lock
Permit          | Semaphore
Signal          | Event

## File Handling
Dyno Keyword    | Equivalent
----------------|-----------------------
Fetch           | Read
Modify          | Write
Inlet           | Open
Seal            | Close

## User I/O
Dyno Keyword    | Equivalent    | Purpose
----------------|---------------|----------------------------------------
ask()           | input()       | Takes user input, auto-casts to type
show()          | print()       | Outputs text or data to user console

## Type Handling/Checking
Dyno Keyword        | Equivalent
--------------------|-------------------------------
kind()              | type()         | Function: Get type of variable
convert V to DT     | Convert        | Keyword: Convert variable V to data type DT

## Inheritance
Dyno Keyword    | Equivalent
----------------|-----------------------
Adopt           | Inheritance
Father          | Base Class
Child           | Derived Class

## Memory Management
Dyno Keyword    | Equivalent
----------------|-----------------------
Slip            | Free Memory
Wipe            | Garbage Collection

## Miscellaneous Operations
Dyno Keyword    | Equivalent
----------------|-----------------------
Authen          | Verify/Assert
Transform       | Map
Condense        | Reduce
Den             | Lambda Expression (anonymous function)

## Data Serialization
Dyno Keyword    | Equivalent
----------------|-----------------------
Pack            | Serialize
Unpack          | Deserialize

## Event Handling
Dyno Keyword    | Equivalent
----------------|-----------------------
Listen          | Event Binding
Trigger         | Raise Event/Error

## Debugging/Logging
Dyno Keyword    | Equivalent
----------------|-----------------------
Track           | Debug Information
Trace           | Execution Tracing
Watch           | Watch Variables

## Special Features
Dyno Keyword    | Equivalent
----------------|------------------------
Spec            | Function Definition (like def)
Forward         | Return/Send value from function
Funcall         | Function Call (optional for clarity in complex code)
Check           | If
Alter           | Elif
Altern          | Else
Conclude        | Finally Block
Skelet          | Abstract Class
Decon           | Deconstruct Pattern

## System/Environment Operations
Dyno Keyword    | Equivalent
----------------|-----------------------------
Plug            | Import
Share           | Export
Toolkit         | Module
Bloc            | Block/Batch Operation
Embed           | Embed Resources
Bridge          | Interface
Link            | Join
Belong          | Belongs To
Peek            | Access/View
Infuse          | Inject/Populate

## Error Handling
Dyno Keyword    | Equivalent        | Purpose
----------------|-------------------|-------------------------------------------
Attempt         | Try               | Begin risky code block
Trap            | Catch             | Catch and handle error
Conclude        | Finally           | Always executes
Trigger         | Raise             | Manually raise an error
Check           | Conditional in error handling
Peek            | Exception Object  | View error info from Trap block

## Control Flow Keywords
Dyno Keyword    | Equivalent
----------------|-----------------------
Skip            | Continue
Ignore          | Pass (do nothing)
Break           | Break loop
Until           | While (loop until condition)
Using           | With (resource management)
Give            | Yield (produce value lazily)
Spill           | Yield (unique synonym for generators)
Both            | And
No              | Not
Off             | False
Nil             | None
On              | True
Erase           | Del
Source          | From
Universal       | Global
Within          | In
Is              | Is
Assert          | Assert
Both            | And
Or              | Or

## Data Types Synonyms
Dyno Keyword    | Equivalent
----------------|-----------------------
Num             | Int
Decim           | Float
Bit             | Bool
Text            | String
Den             | Lambda (anonymous function)

## Additional Keywords
Dyno Keyword    | Equivalent
----------------|-----------------------
Scope()         | Range()
Tag()           | Enum()
Solve()          | eval() 