# UOP Interfaces & Interaction Logic in Beacon

Beacon's Bridge System is designed around Universal User-Oriented Programming (UOP) — allowing natural, modular, and intuitive communication between components, users, and systems. This system enables[...]

---

## 1. Core Concepts

| Beacon Keyword | Role                     | Equivalent           |
|--------------|--------------------------|---------------------|
| bridge       | Defines a UOP interface  | interface / API     |
| link         | Binds implementations    | connect / bind      |
| peek         | Access values inside bridge | get / property accessor |
| expose       | Makes bridge methods callable | public function  |
| inlet        | Entry point handler      | main() / entry()    |
| forward      | Return response to caller | return             |
| embed        | Embed resource or handler | Include resource    |

---

## 2. Declaring a Bridge Interface

```plaintext
bridge Calculator
    expose spec add a b
        forward a + b

    expose spec subtract a b
        forward a - b
```

---

## 3. Linking Bridges to Toolkits or Systems

```plaintext
toolkit MathCore
    plug Calculator

    spec main
        link calc to Calculator
        result = calc.add(5, 3)
        output(f"Result: {result}")
```

---

## 4. Inlet Blocks for Interaction Entry

Use inlet to define interaction logic entry points:

```plaintext
inlet
    output("Welcome to Beacon Interface")
    val = ask()
    bridge_id = convert val to int

    check bridge_id == 1
        link action to Calculator
        result = action.add(4, 2)
        output(f"Sum is {result}")
```

---

## 5. Nested and Embedded Bridges

```plaintext
bridge AuthBridge
    expose spec validate token
        check token == "beacon123"
            forward "Access Granted"
        forward "Access Denied"

bridge UserInterface
    embed AuthBridge

    expose spec login user_token
        result = AuthBridge.validate(user_token)
        forward result
```

---

## 6. User-Oriented Signal Flow

In a UOP design, interaction always begins with inlet, and flows through linked bridges:

```plaintext
inlet
    link user_bridge to UserInterface
    token = ask()
    response = user_bridge.login(token)
    output(response)
```

---

## 7. Summary

- Bridges = Interfaces with exposed methods
- Links = Bind a bridge to a variable/handler
- Inlets = User or system-driven entry points
- Forward = Used instead of return
- Peek = View internal states or response
- Embed = Bring in nested logic

Beacon's Bridge structure allows full modularity without breaking UOP flow, ensuring that users always interact through intentful, understandable units.
