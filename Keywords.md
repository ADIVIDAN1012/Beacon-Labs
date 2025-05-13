# Dyno Programming Language - Keywords

### *Access Control*
| *Dyno Keyword* | *Equivalent*         |
|----------------|----------------------|
| *Covnito*      | Private              |
| *Shel*         | Protected            |
| *Avail*        | Public               |
| *Internal*     | Package-level access |
| *Expose*       | Internal/Public exposure |

### *Concurrency/Parallelism*
| *Dyno Keyword* | *Equivalent*         |
|----------------|----------------------|
| *Paral*        | Async                |
| *Hold*         | Await                |
| *Flux*         | Flow                 |
| *Barrier*      | Lock                 |
| *Permit*       | Semaphore            |
| *Signal*       | Event                |

### *File Handling*
| *Dyno Keyword* | *Equivalent*         |
|----------------|----------------------|
| *Fetch*        | Read                 |
| *Modify*       | Write                |
| *inlet*        | Open                 |
| *Seal*         | Close                |

### *Type Handling/Checking*
| *Dyno Keyword*     | *Equivalent*         |
|--------------------|----------------------|
| *Kind*             | Type checking        |
| *Convert V To DT*  | Converts any variable V to user desired data type DT |

### *Inheritance*
| *Dyno Keyword* | *Equivalent*         |
|----------------|----------------------|
| *Adopt*        | Inheritance          |
| *Father*       | Base Class           |
| *Child*        | Derived Class        |

### *Memory Management*
| *Dyno Keyword* | *Equivalent*         |
|----------------|----------------------|
| *Slip*         | Free Memory          |
| *Wipe*         | Garbage Collection   |

### *Miscellaneous Operations*
| *Dyno Keyword* | *Equivalent*         |
|----------------|----------------------|
| *Authen*       | Verify/Assert        |
| *Transform*    | Map                  |
| *Reduce*       | Aggregate            |

### *Data Serialization*
| *Dyno Keyword* | *Equivalent*         |
|----------------|----------------------|
| *Pack*         | Serialize            |
| *Unpack*       | Deserialize          |

### *Event Handling*
| *Dyno Keyword* | *Equivalent*         |
|----------------|----------------------|
| *Listen*       | Event Binding        |
| *Trigger*      | Emit Event           |

### *Debugging/Logging*
| *Dyno Keyword* | *Equivalent*         |
|----------------|----------------------|
| *Track*        | Debug Information    |
| *Trace*        | Execution Tracing    |
| *Watch*        | Watch Variables      |

### *Special Features*
| *Dyno Keyword* | *Feature*            |
|----------------|----------------------|
| *Spec*         | Function Definition  |
| *Send*         | Function Return      |
| *Check*        | Conditional (if)     |
| *Alter*        | Conditional (elif)   |
| *Altern*       | Conditional (else)   |
| *Conclude*     | Finally Block        |
| *Skelet*       | Abstract Class       |
| *Decon*        | Deconstruct          |

### *System/Environment Operations*
| *Dyno Keyword* | *Equivalent*         |
|----------------|----------------------|
| *Plug*         | Import               |
| *Share*        | Export               |
| *Toolkit*      | Module               |
| *Bloc*         | Batch/Block operation|
| *Embed*        | Include/Embed resources|
| *Bridge*       | Interface            |
| *Link*         | Join                 |
| *Belong*       | Inherits from        |
| *Peek*         | Access               |
| *Infuse*       | Inject/Populate      |

### *Error Handling*
| *Dyno Keyword* | *Equivalent*         | *Purpose*                          |
|----------------|----------------------|----------------------------------|
| *attempt*      | try                  | Begin a block that may raise an error |
| *trap*         | catch                | Handle a specific error           |
| *conclude*     | finally              | Always run code regardless of errors |
| *trigger*      | raise                | Manually raise an error           |
| *check*        | if                   | Conditional check inside error blocks |
| *peek*         | Exception object     | View the error message/data caught in trap |
