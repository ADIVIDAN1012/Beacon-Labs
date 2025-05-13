# Dyno Programming Language Syntax

## Access Control

| Dyno Keyword | Equivalent         | Syntax Example                          |
|--------------|--------------------|---------------------------------------|
| Covnito      | Private            | `Covnito varName`                      |
| Shel         | Protected          | `Shel varName`                         |
| Avail        | Public             | `Avail varName`                        |
| Internal     | Package-level access| `Internal varName`                     |
| Expose       | Internal/Public exposure | `Expose varName`                  |

## Concurrency/Parallelism

| Dyno Keyword | Equivalent         | Syntax Example                          |
|--------------|--------------------|---------------------------------------|
| Paral        | Async              | `Paral funcName() { ... }`             |
| Hold         | Await              | `Hold asyncFunc()`                      |
| Flux         | Flow               | `Flux dataStream = ...`                 |
| Barrier      | Lock               | `Barrier lockName { ... }`              |
| Permit       | Semaphore          | `Permit semName(count)`                  |
| Signal       | Event              | `Signal eventName`                      |

## File Handling

| Dyno Keyword | Equivalent         | Syntax Example                          |
|--------------|--------------------|---------------------------------------|
| Fetch        | Read               | `var data = Fetch filePath`             |
| Modify       | Write              | `Modify filePath with data`             |
| Unlock       | Open               | `Unlock filePath`                       |
| Seal         | Close              | `Seal filePath`                         |

## Type Handling/Checking

| Dyno Keyword | Equivalent         | Syntax Example                          |
|--------------|--------------------|---------------------------------------|
| Kind         | Type checking      | `kind(var)`                            |
| Convert V To DT | Convert variable V to data type DT | `Convert x To Int`         |


## Inheritance

| Dyno Keyword | Equivalent         | Syntax Example                          |
|--------------|--------------------|---------------------------------------|
| Adopt        | Inheritance        | `Child Adopt Father { ... }`            |
| Father       | Base Class         | `Toolkit Father { ... }`                 |
| Child        | Derived Class      | `Toolkit Child Adopt Father { ... }`    |

## Memory Management

| Dyno Keyword | Equivalent         | Syntax Example                          |
|--------------|--------------------|---------------------------------------|
| Slip         | Free Memory        | `Slip varName`                         |
| Wipe         | Garbage Collection | `Wipe`                                |

## Miscellaneous Operations

| Dyno Keyword | Equivalent         | Syntax Example                          |
|--------------|--------------------|---------------------------------------|
| Authen       | Verify/Assert      | `Authen condition`                     |
| Transform    | Map                | `Transform collection with func`      |
| Reduce       | Aggregate          | `Reduce collection with func`          |

## Data Serialization

| Dyno Keyword | Equivalent         | Syntax Example                          |
|--------------|--------------------|---------------------------------------|
| Pack         | Serialize          | `var packedData = Pack data`            |
| Unpack       | Deserialize        | `var data = Unpack packedData`          |

## Event Handling

| Dyno Keyword | Equivalent         | Syntax Example                          |
|--------------|--------------------|---------------------------------------|
| Listen       | Event Binding      | `Listen eventName with handler`         |
| Trigger      | Emit Event         | `Trigger eventName`                     |

## Debugging/Logging

| Dyno Keyword | Equivalent         | Syntax Example                          |
|--------------|--------------------|---------------------------------------|
| Track        | Debug Information  | `Track "message"`                      |
| Trace        | Execution Tracing  | `Trace`                               |
| Watch        | Watch Variables    | `Watch varName`                        |

## Special Features

| Dyno Keyword | Feature            | Syntax Example                          |
|--------------|--------------------|---------------------------------------|
| Spec         | Function Definition| `Spec funcName(params) { ... }`        |
| Send         | Function Return    | `Send value`                          |
| Check        | Conditional (if)   | `Check condition { ... }`              |
| Alter        | Conditional (elif) | `Alter condition { ... }`              |
| Altern       | Conditional (else) | `Altern { ... }`                       |
| Conclude     | Finally Block      | `Conclude { ... }`                     |
| Skelet       | Abstract Class     | `Skelet className { ... }`             |
| Decon        | Deconstruct        | `Decon varName into parts`             |

## System/Environment Operations

| Dyno Keyword | Equivalent         | Syntax Example                          |
|--------------|--------------------|---------------------------------------|
| Plug         | Import             | `Plug toolkitName`                     |
| Share        | Export             | `Share funcName`                       |
| Toolkit      | Module             | `Toolkit toolkitName { ... }`          |
| Bloc         | Batch/Block operation | `Bloc { ... }`                      |
| Embed        | Include/Embed resources | `Embed resourceName`               |
| Bridge       | Interface          | `Bridge interfaceName { ... }`         |
| Link         | Join               | `Link obj1 with obj2`                  |
| Belong       | Inherits from      | `className Belong baseClass`           |
| Peek         | Access             | `Peek varName`                         |
| Infuse       | Inject/Populate    | `Infuse obj with data`                  |
