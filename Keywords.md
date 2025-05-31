# Dyno Programming Language - Keywords and Built-in Functions

## Access Control
| Dyno Keyword | Equivalent       | Purpose                          |
|--------------|------------------|---------------------------------|
| covnito     | private           | Private access modifier          |
| shel        | protected         | Protected access modifier        |
| avail       | public            | Public access modifier           |
| internal    | package-level     | Package/internal access          |
| expose      | internal/public   | Internal or public exposure      |

## Concurrency / Parallelism
| Dyno Keyword | Equivalent   | Purpose                          |
|--------------|--------------|---------------------------------|
| paral       | async         | Asynchronous operation           |
| hold        | await         | Await async result               |
| barrier     | lock          | Lock/synchronization             |
| permit      | semaphore     | Semaphore control                |
| signal      | event         | Event signaling                 |

## File Handling
| Dyno Keyword | Equivalent   | Purpose                          |
|--------------|--------------|---------------------------------|
| fetch       | read          | Read from file                  |
| modify      | write         | Write to file                  |
| inlet       | open          | Open file                      |
| seal        | close         | Close file                     |

## User Input / Output
| Dyno Keyword | Equivalent   | Purpose                          |
|--------------|--------------|---------------------------------|
| ask()       | input()       | Take user input, auto-casts type|
| show()      | print()       | Output text/data to user console|

## Type Handling / Checking
| Dyno Keyword        | Equivalent  | Purpose                         |
|---------------------|-------------|--------------------------------|
| kind()              | type()      | Get type of variable           |
| convert variable to Type | N/A       | Convert variable to desired data type (syntax: `convert v to int`) |

## Inheritance
| Dyno Keyword | Equivalent   | Purpose                          |
|--------------|--------------|---------------------------------|
| adopt       | inheritance   | Inheritance keyword             |
| father      | base class    | Base/parent class               |
| child       | derived class | Derived/child class             |

## Memory Management
| Dyno Keyword | Equivalent     | Purpose                         |
|--------------|----------------|--------------------------------|
| slip        | free memory     | Free allocated memory           |
| wipe        | garbage collect | Run garbage collection          |

## Control Flow
| Dyno Keyword | Equivalent | Purpose                          |
|--------------|------------|---------------------------------|
| check       | if         | Conditional if                  |
| alter       | elif       | Else-if                        |
| altern      | else       | Else                          |
| attempt     | try        | Try block                      |
| trap        | catch      | Catch errors                   |
| conclude    | finally    | Finally block                  |
| trigger     | raise      | Raise error                   |

## Functions
| Dyno Keyword | Equivalent | Purpose                          |
|--------------|------------|---------------------------------|
| spec        | def         | Function definition             |
| den         | lambda      | Lambda/anonymous function       |
| forward     | return      | Return from function            |
| funcall     | N/A         | Optional keyword to explicitly call functions (used for clarity in complex calls) |

## Modules / Imports / Exports
| Dyno Keyword | Equivalent | Purpose                          |
|--------------|------------|---------------------------------|
| plug        | import      | Import module                   |
| share       | export      | Export module/function          |
| toolkit     | module      | Module/package                  |

## Classes and Interfaces
| Dyno Keyword | Equivalent | Purpose                          |
|--------------|------------|---------------------------------|
| blueprint   | class       | Class definition                |
| skelet      | abstract class | Abstract class               |
| bridge      | interface   | Interface declaration           |

## Blocks & Structure
| Dyno Keyword | Equivalent | Purpose                          |
|--------------|------------|---------------------------------|
| bloc        | block/batch| Block of code or batch operation|
| embed       | embed      | Embed resource/data             |

## Associations
| Dyno Keyword | Equivalent | Purpose                          |
|--------------|------------|---------------------------------|
| link        | join       | Join/link components            |
| belong      | belongs to | Association/ownership           |

## Variable Access
| Dyno Keyword | Equivalent | Purpose                          |
|--------------|------------|---------------------------------|
| peek        | access/view| Access or view property/value   |
| infuse      | inject/populate | Inject or populate data      |

## Data Serialization
| Dyno Keyword | Equivalent | Purpose                          |
|--------------|------------|---------------------------------|
| pack        | serialize  | Serialize data                  |
| unpack      | deserialize| Deserialize data                |

## Event Handling
| Dyno Keyword | Equivalent | Purpose                          |
|--------------|------------|---------------------------------|
| listen      | event bind | Bind event listener             |
| trigger     | emit event | Emit/trigger event             |

## Debugging / Logging
| Dyno Keyword | Equivalent | Purpose                          |
|--------------|------------|---------------------------------|
| track       | debug info | Track debug info                |
| trace       | exec trace | Trace execution flow            |
| watch       | watch vars | Watch variables                 |

## Miscellaneous Operations
| Dyno Keyword | Equivalent | Purpose                          |
|--------------|------------|---------------------------------|
| authen      | verify/assert| Verification/assertion         |
| transform   | map         | Transform/map function          |
| condense    | reduce      | Reduce/aggregate function       |

## Built-in Functions (with parentheses)
| Dyno Function | Equivalent   | Purpose                        |
|---------------|--------------|-------------------------------|
| ask()         | input()      | Takes user input, auto-casts type |
| show()        | print()      | Output to user console          |
| kind()        | type()       | Returns type of variable        |
| scope()       | range()      | Generate a sequence/range       |
| tag()         | enumerate()  | Enumerate items with index      |
| solve()       | eval()       | Evaluate expression dynamically |

## Data Types (Synonyms)
| Dyno Keyword | Equivalent | Purpose                          |
|--------------|------------|---------------------------------|
| num          | int        | Integer numeric type             |
| decim        | float      | Floating point decimal number    |
| bit          | bool       | Boolean true/false               |
| text         | string     | Text/String                     |
| nil          | null       | Null or no value                |
| firm         | const      | Constant/immutable value        |

---

*Notes:*

- `convert` is a keyword used in syntax form: