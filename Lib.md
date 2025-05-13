# Dyno Standard Libraries 

Dyno’s standard library collection is built to support its Universal User-Oriented Programming (UOP) paradigm and core language principles. Every library module uses only unique, domain-specific names and avoids conflicts with existing language ecosystems. Below is the structured hierarchy:

---

## 1. Core & Runtime Utilities

### dyno.core

Core utilities and base operations.

- abort(): Stops program execution.
- ping(): Confirms runtime is active.
- ok() / nope(): Used for truthy logic.
- input(): Basic input handling.
- print(): Basic output handling.

### dyno.io

Input/output stream management.

- read()
- write()
- flush()

### dyno.string

String manipulation utilities.

- trim()
- split()
- join()
- replace()
- format()

### dyno.collection

Collection data structures and utilities.

- list()
- set()
- map()
- queue()
- stack()

### dyno.concurrent

Concurrency and parallelism utilities.

- spawn()
- lock()
- unlock()
- wait()
- signal()

### dyno.track

Logging and tracking system behavior.

- track.info()
- track.warn()
- track.crit()

### dyno.time

Time and date management.

- now()
- pause(ms)
- clock()

### dyno.rand

Random generation and entropy utilities.

- pick()
- coin()
- roll(dice)

---

## 2. User-Oriented Libraries

### dyno.bridge

UOP Interfaces and interaction handlers.

- bridge.define()
- bridge.map()
- bridge.link()

### dyno.peer

Manages user and identity information.

- iden()
- authen()
- peek()

### dyno.hub

Communication and event triggers.

- send()
- receive()
- forward()

---

## 3. Structural & Logical

### dyno.logic

Control flow utilities.

- both, either, deny
- flux for conditional flow structures.

### dyno.nick

User-defined type nicknaming.

- nick Data as Integer

### dyno.bloc

Functional blocks and procedural flows.

- bloc do()
- bloc onfail()
- bloc retry()

### dyno.trap

Error and exception handling.

- attempt, trap, trigger, conclude

---

## 4. Math, Data & Transformation

### dyno.math

Arithmetic, scientific, and geometric calculations.

- absol(), exponent(), Roff()
- scope() for sequence generation.

### dyno.kind

Data type discovery.

- kind(), convert, plug()

### dyno.infuse

Data structures and transformations.

- infuse.list()
- infuse.seal()
- infuse.map()

---

## 5. Files & Persistence

### dyno.file

File operations and data persistence.

- fetch(), modify()
- lock(), unlock()

### dyno.logix

Persistent workflow scripting.

- track(), retrack()

---

## 6. Networking & Communication

### dyno.net

Basic network communications.

- ping.remote()
- plug.remote()

### dyno.sigma

Signals and real-time streams.

- emit(), receive(), observe()

---

## 7. DevTools & Meta

### dyno.meta

Introspection and reflection.

- belong()
- kind()
- peek()

### dyno.skelet

Structural blueprints.

- blueprint, procsys, skelet

### dyno.decon

Destructuring utilities.

- decon — shorthand for deconstruct.

---

## 8. Experimental & Plug-ins

### dyno.toolkit

Modular plug-and-play extensions.

- plug bridge from toolkit
- plug infuse from toolkit

### dyno.funcall

Function call wrappers and decorators.

- funcall.delayed()
- funcall.parallel()

---

## 9. Custom Libraries (Cus-libs)

Dyno supports the creation of custom libraries, allowing programmers to define and manage their own reusable code modules tailored to their specific needs.

- define(): Define a new custom library.
- import(): Import a custom library into a project.
- list(): List available custom libraries.
- remove(): Remove a custom library.

---
