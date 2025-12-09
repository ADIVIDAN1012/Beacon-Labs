# Beacon Standard Library

The Beacon Standard Library is a collection of built-in `toolkits` that provide essential functionalities. These libraries are designed to be consistent with Beacon's UOP principles, offering intuitive and powerful tools for common programming tasks.

---

## Core Libraries

### `core`
The `core` library provides fundamental functions for interacting with the runtime.
- `core.halt()`: Stops program execution.
- `core.ping()`: Confirms that the runtime is active and responsive.
- `core.time()`: Returns the current system time.

### `math`
The `math` library contains functions for numerical operations.
- `math.abs(number)`: Returns the absolute value.
- `math.round(number)`: Rounds a number to the nearest integer.
- `math.pow(base, exp)`: Calculates an exponent.
- `math.max(a, b)`: Returns the greater of two numbers.
- `math.min(a, b)`: Returns the lesser of two numbers.
- `math.random()`: Returns a random number.

---

## Data Handling

### `text`
The `text` library offers tools for string manipulation.
- `text.trim(string)`: Removes leading/trailing whitespace.
- `text.split(string, delimiter)`: Splits a string into a list.
- `text.join(list, delimiter)`: Joins a list of strings into one.
- `text.replace(string, old, new)`: Replaces occurrences of a substring.
- `text.format(template, values)`: Formats a string with placeholders.

### `collection`
The `collection` library provides and manages data structures.
- `collection.list()`: Creates a list.
- `collection.dict()`: Creates a dictionary (key-value map).
- `collection.set()`: Creates a set of unique items.

### `serial`
The `serial` library is used for data serialization and deserialization.
- `serial.pack(object)`: Serializes an object to a storable format (e.g., JSON).
- `serial.unpack(data)`: Deserializes data back into an object.

---

## System & I/O

### `io`
The `io` library manages input and output streams.
- `io.read(source)`: Reads data from a source (e.g., file, network).
- `io.write(destination, data)`: Writes data to a destination.
- `io.flush(stream)`: Flushes an output buffer.

### `file`
The `file` library provides a user-friendly interface for file system operations.
- `file.open(path, mode)`: Opens a file and returns a handle.
- `file.read(handle)`: Reads the content of an open file.
- `file.write(handle, content)`: Writes content to an open file.
- `file.close(handle)`: Closes an open file.
- `file.exists(path)`: Checks if a file or directory exists.

---

## Networking

### `net`
The `net` library provides tools for network communication.
- `net.connect(address)`: Establishes a network connection.
- `net.send(connection, data)`: Sends data over a connection.
- `net.receive(connection)`: Receives data from a connection.
- `net.ping(host)`: Pings a remote host to check for connectivity.

---

## Concurrency

### `concurrent`
The `concurrent` library enables parallel execution of code.
- `concurrent.spawn(spec)`: Runs a `spec` in a new thread or process.
- `concurrent.lock()`: Acquires a lock for synchronizing access to shared resources.
- `concurrent.unlock()`: Releases a lock.
- `concurrent.signal()`: Sends a signal to coordinate between concurrent tasks.

---

## Development & Debugging

### `debug`
The `debug` library provides tools for inspecting and debugging code.
- `debug.track(message)`: Logs a debug message.
- `debug.watch(variable)`: Monitors a variable for changes.
- `debug.trace()`: Prints the current execution trace.

### `meta`
The `meta` library allows for introspection and reflection.
- `meta.kindof(variable)`: Gets the type of a variable.
- `meta.props(object)`: Lists the properties of an object.
- `meta.methods(object)`: Lists the methods of an object.
