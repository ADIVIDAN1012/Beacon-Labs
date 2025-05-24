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
output()        | print()       | Outputs text or data to user console

## Type Handling/Checking
Dyno Keyword        | Equivalent
--------------------|-------------------------------
Kind                | Type checking
convert V to DT     | Convert variable to desired type

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
Reduce          | Aggregate

## Data Serialization
Dyno Keyword    | Equivalent
----------------|-----------------------
Pack            | Serialize
Unpack          | Deserialize

## Event Handling
Dyno Keyword    | Equivalent
----------------|-----------------------
Listen          | Event Binding
Trigger         | Emit Event

## Debugging/Logging
Dyno Keyword    | Equivalent
----------------|-----------------------
Track           | Debug Information
Trace           | Execution Tracing
Watch           | Watch Variables

## Special Features
Dyno Keyword    | Equivalent
----------------|------------------------
Spec            | Function Definition
Forward         | Function Return
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
Check           | If in error block | Conditional evaluation
Peek            | Exception object  | View the error info from Trap block