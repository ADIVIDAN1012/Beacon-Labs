# Dyno Programming Language - Keywords

### Access Control
| Dyno Keyword | Equivalent         |
|------------------|------------------------|
| Covnito      | Private                |
| Shel         | Protected              |
| Avail        | Public                 |
| Internal     | Package-level access  |
| Expose       | Internal/Public exposure |

### Concurrency/Parallelism
| Dyno Keyword | Equivalent         |
|------------------|------------------------|
| Paral        | Async                  |
| Hold         | Await                  |
| Flow         | Thread                 |
| Barrier      | Lock                   |
| Permit       | Semaphore              |
| Signal       | Event                  |

### File Handling
| Dyno Keyword | Equivalent         |
|------------------|------------------------|
| Fetch        | Read                   |
| Modify       | Write                  |
| Unlock       | Open                   |
| Seal         | Close                  |

### Type Handling/Checking
| Dyno Keyword | Equivalent         |
|------------------|------------------------|
| Kind         | Type checking                   |
| Convert V To DT    | Converts any variable V to user desired data type DT |

### Inheritance
| Dyno Keyword | Equivalent         |
|------------------|------------------------|
| Adopt        | Inheritance            |
| Father       | Base Class             |
| Child        | Derived Class          |

### Memory Management
| Dyno Keyword | Equivalent         |
|------------------|------------------------|
| Slip      | Free Memory            |
| Wipe      | Garbage Collection     |

### Miscellaneous Operations
| Dyno Keyword | Equivalent         |
|------------------|------------------------|
| Authen       | Verify/Assert          |
| Transform    | Map                    |
| Reduce       | Aggregate              |

### Data Serialization
| Dyno Keyword | Equivalent         |
|------------------|------------------------|
| Pack         | Serialize              |
| Unpack       | Deserialize            |

### Event Handling
| Dyno Keyword | Equivalent         |
|------------------|------------------------|
| Listen       | Event Binding          |
| Trigger      | Emit Event             |

### Debugging/Logging
| Dyno Keyword | Equivalent         |
|------------------|------------------------|
| Log          | Debug Information      |
| Trace        | Execution Tracing      |
| Watch        | Watch Variables        |

---

### Special Features
| Dyno Keyword | Feature           |
|------------------|-----------------------|
| Spec         | Function Definition   |
| Send         | Function Return       |
| Check        | Conditional (if)      |
| Alter        | Conditional (elif)    |
| Altern       | Conditional (else)    |
| Conclude     | Finally Block         |

### Modules & Libraries
| Dyno Keyword | Equivalent         |
|------------------|------------------------|
| Use           | Import                 |
| Share         | Export                 |
| Toolkit       | Module                 |

---

### Task Handling
| Dyno Keyword | Equivalent         |
|------------------|------------------------|
| Task         | Task/Thread Creation   |
| link         | Synchronizing Tasks    |
| Flow         | Threading              |
| Signal       | Event                  |
