# Beacon Standard Libraries 

Beacon’s standard library collection is built to support its Universal User-Oriented Programming (UOP) paradigm and core language principles. Every library module uses only unique, domain-specific key[...]

---

## 1. Core & Runtime Utilities

### beacon.core

Core utilities and base operations.

- abort(): Stops program execution.
- ping(): Confirms runtime is active.
- ok() / nope(): Used for truthy logic.
- input(): Basic input handling.
- print(): Basic output handling.

### beacon.io

Input/output stream management.

- read()
- write()
- flush()

### beacon.string

String manipulation utilities.

- trim()
- split()
- join()
- replace()
- format()

### beacon.collection

Collection data structures and utilities.

- list()
- set()
- map()
- queue()
- stack()

### beacon.concurrent

Concurrency and parallelism utilities.

- spawn()
- lock()
- unlock()
- wait()
- signal()

### beacon.track

Logging and tracking system behavior.

- track.info()
- track.warn()
- track.crit()

### beacon.time

Time and date management.

- now()
- pause(ms)
- clock()

### beacon.rand

Random generation and entropy utilities.

- pick()
- coin()
- roll(dice)

---

## 2. User-Oriented Libraries

### beacon.bridge

UOP Interfaces and interaction handlers.

- bridge.define()
- bridge.map()
- bridge.link()

### beacon.peer

Manages user and identity information.

- iden()
- authen()
- peek()

### beacon.hub

Communication and event triggers.

- send()
- receive()
- forward()

---

## 3. Structural & Logical

### beacon.logic

Control flow utilities.

- both, either, deny
- flux for conditional flow structures.

### beacon.nick

User-defined type nicknaming.

- nick Data as Integer

### beacon.bloc

Functional blocks and procedural flows.

- bloc do()
- bloc onfail()
- bloc retry()

### beacon.trap

Error and exception handling.

- attempt, trap, trigger, conclude

---

## 4. Math, Data & Transformation

### beacon.math

Arithmetic, scientific, and geometric calculations.

- absol(), exponent(), Roff()
- scope() for sequence generation.

### beacon.kind

Data type discovery.

- kind(), convert, plug()

### beacon.infuse

Data structures and transformations.

- infuse.list()
- infuse.seal()
- infuse.map()

---

## 5. Files & Persistence

### beacon.file

File operations and data persistence.

- fetch(), modify()
- lock(), unlock()

### beacon.logix

Persistent workflow scripting.

- track(), retrack()

---

## 6. Networking & Communication

### beacon.net

Basic network communications.

- ping.remote()
- plug.remote()

### beacon.sigma

Signals and real-time streams.

- emit(), receive(), observe()

---

## 7. DevTools & Meta

### beacon.meta

Introspection and reflection.

- belong()
- kind()
- peek()

### beacon.skelet

Structural blueprints.

- blueprint, procsys, skelet

### beacon.decon

Destructuring utilities.

- decon — shorthand for deconstruct.

---

## 8. Experimental & Plug-ins

### beacon.toolkit

Modular plug-and-play extensions.

- plug bridge from toolkit
- plug infuse from toolkit

### beacon.funcall

Function call wrappers and decorators.

- funcall.delayed()
- funcall.parallel()

---

## 9. Custom Libraries (Cus-libs)

Beacon supports the creation of custom libraries, allowing programmers to define and manage their own reusable code modules tailored to their specific needs.

- define(): Define a new custom library.
- import(): Import a custom library into a project.
- list(): List available custom libraries.
- remove(): Remove a custom library.

---
