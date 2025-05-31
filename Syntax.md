# Dyno Programming Language - Keywords

## Access Control
Dyno Keyword    | Equivalent
----------------|-----------------------
Covnito         | Private
Shel            | Protected
Avail           | Public
Internal        | Package-level access
Expose          | Internal/Public exposure

## Concurrency / Parallelism
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
Ask()           | input()       | Takes user input, auto-casts to type
Show()          | print()       | Outputs text or data to user console

## Type Handling / Checking
Dyno Keyword        | Equivalent
--------------------|-------------------------------
Kind                | Type checking
Convert V to DT     | Convert variable to desired data type

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
Condense        | Reduce (aggregate)

## Data Serialization
Dyno Keyword    | Equivalent
----------------|-----------------------
Pack            | Serialize
Unpack          | Deserialize

## Event Handling
Dyno Keyword    | Equivalent
----------------|-----------------------
Listen          | Event Binding
Trigger         | Emit Event / Raise Error

## Debugging / Logging
Dyno Keyword    | Equivalent
----------------|-----------------------
Track           | Debug Information
Trace           | Execution Tracing
Watch           | Watch Variables

## Special Features
Dyno Keyword    | Equivalent
----------------|------------------------
Spec            | Function Definition
Funcall         | Function Call (optional for clarity)
Forward         | Return (send)
Check           | If
Alter           | Elif
Altern          | Else
Conclude        | Finally Block
Skelet          | Abstract Class
Decon           | Deconstruct Pattern
Den             | Lambda

## System / Environment Operations
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
Source          | From
Universal       | Global

## Error Handling
Dyno Keyword    | Equivalent        | Purpose
----------------|-------------------|-------------------------------------------
Attempt         | Try               | Begin risky code block
Trap            | Catch             | Catch and handle error
Conclude        | Finally           | Always executes
Trigger         | Raise             | Manually raise an error
Peek            | Exception object  | View the error info from Trap block

## Control Flow Keywords
Dyno Keyword    | Equivalent
----------------|-----------------------
Skip            | Continue
Ignore          | Pass (do nothing)
Break           | Break loop
Until           | While (loop until condition)
Using           | With (resource management)
Spill           | Yield (unique synonym for generators)
Both            | And
Either          | Or
No              | Not
Off             | False
Nil             | None
On              | True
Erase           | Del

## Condition / Boolean Keywords
Dyno Keyword    | Equivalent
----------------|-----------------------
Is              | Is
Within          | In
Assert          | Assert

## Data Types Synonyms
Dyno Keyword    | Equivalent
----------------|-----------------------
Num             | Int
Bit             | Bool
Text            | Str
Decim           | Float
Den             | Lambda
Seal            | Tuple

## Others
Dyno Keyword    | Equivalent
----------------|-----------------------
Solve           | Eval