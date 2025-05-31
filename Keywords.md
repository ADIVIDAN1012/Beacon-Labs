# Dyno Programming Language - Keywords

## Access Control
Dyno Keyword | Equivalent       | Purpose
-------------|------------------|-----------------------------------
Covnito      | private          | Private access modifier
Shel         | protected        | Protected access modifier
Avail        | public           | Public access modifier
Internal     | package-level    | Package/internal access modifier
Expose       | internal/public  | Internal or public exposure

## Concurrency / Parallelism
Dyno Keyword | Equivalent       | Purpose
-------------|------------------|-------------------------------
Paral        | async            | Asynchronous operation
Hold         | await            | Await async result
Flux         | flow             | Data flow control
Barrier      | lock             | Lock/synchronization
Permit       | semaphore        | Semaphore control
Signal       | event            | Event signaling

## File Handling
Dyno Keyword | Equivalent       | Purpose
-------------|------------------|-------------------------------
Fetch        | read             | Read from file
Modify       | write            | Write to file
Inlet        | open             | Open file/resource
Seal         | close            | Close file/resource

## User I/O
Dyno Keyword | Equivalent       | Purpose
-------------|------------------|------------------------------
ask()        | input()          | Take user input, auto-cast type
show()       | print()/output() | Output to user console

## Type Handling / Checking
Dyno Keyword     | Equivalent     | Purpose
-----------------|----------------|-------------------------------
Kind()           | type()         | Get type of variable
convert V to DT  | type conversion| Convert variable to desired type

## Data Types (Dyno Synonyms)
Dyno Keyword | Equivalent | Purpose
-------------|------------|-----------------------------------------
Num          | int        | Integer numeric type
Decim        | float      | Floating point decimal number
Bit          | bool       | Boolean true/false (smallest binary unit)
Text         | string     | Text or string data
Nil          | nil/null   | Null or no value
Firm         | const      | Constant, immutable value

## Inheritance
Dyno Keyword | Equivalent       | Purpose
-------------|------------------|-------------------------------
Adopt        | inheritance      | Inheritance keyword
Father       | base class       | Base or parent class
Child        | derived class    | Derived or child class

## Memory Management
Dyno Keyword | Equivalent       | Purpose
-------------|------------------|--------------------------
Slip         | free memory      | Free allocated memory
Wipe         | garbage collect  | Run garbage collection

## Miscellaneous Operations
Dyno Keyword | Equivalent       | Purpose
-------------|------------------|------------------------------
Authen       | verify/assert    | Verification/assertion
Transform    | map              | Transform/map function
Condense     | reduce           | Reduce/aggregate function

## Data Serialization
Dyno Keyword | Equivalent       | Purpose
-------------|------------------|-------------------------------
Pack         | serialize        | Serialize data
Unpack       | deserialize      | Deserialize data

## Event Handling
Dyno Keyword | Equivalent       | Purpose
-------------|------------------|-------------------------
Listen       | event bind       | Bind event listener
Trigger      | emit event       | Emit/trigger event

## Debugging / Logging
Dyno Keyword | Equivalent       | Purpose
-------------|------------------|-------------------------
Track        | debug info       | Track debug information
Trace        | execution trace  | Trace execution flow
Watch        | watch variables  | Watch variable changes

## Special Features / Control Flow
Dyno Keyword | Equivalent       | Purpose
-------------|------------------|-----------------------------
Spec         | function def     | Function definition
Funcall      | function call    | Function call (optional for clarity)
Forward      | return           | Return from function
Check        | if               | Conditional if
Alter        | elif             | Else-if condition
Altern       | else             | Else condition
Conclude     | finally          | Finally block
Skelet       | abstract class   | Abstract class definition
Decon        | deconstruct      | Pattern deconstruction
Den          | lambda           | Lambda/anonymous function

## System / Environment Operations
Dyno Keyword | Equivalent       | Purpose
-------------|------------------|--------------------------------
Plug         | import           | Import module or library
Share        | export           | Export module or function
Toolkit      | module           | Module or package
Bloc         | block/batch      | Block of code or batch operation
Embed        | embed resources  | Embed resource or data
Bridge       | interface        | Interface declaration
Link         | join             | Join/link components
Belong       | belongs to       | Association or ownership
Peek         | access/view      | Access or view property/value
Infuse       | inject/populate  | Inject or populate data

## Error Handling
Dyno Keyword | Equivalent       | Purpose
-------------|------------------|-------------------------------------------
Attempt      | try              | Begin risky code block
Trap         | catch            | Catch and handle errors
Conclude     | finally          | Always executes
Trigger      | raise            | Manually raise an error
Check        | if in error block| Conditional evaluation in error handling
Peek        | exception object | View error info in trap block

## Expressions and Evaluation
Dyno Keyword | Equivalent       | Purpose
-------------|------------------|------------------------------
Solve        | eval             | Evaluate or execute expressions dynamically
Scope        | range            | Range or sequence
Tag          | enumerate        | Enumerate with index