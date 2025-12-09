# Bridge Interfaces in Beacon

A **Bridge** is a fundamental concept in Beacon's Universal User-Oriented Programming (UOP) model. It serves as a formal interface for defining how different parts of a system, or the system and a user, can interact. Bridges ensure that communication is structured, predictable, and aligned with the user-oriented nature of the language.

---

## 1. Core Concepts

| Keyword | Role in Bridge | Description |
|---|---|---|
| `bridge` | Defines the interface | Declares a new bridge, specifying the methods it exposes. |
| `spec` | Defines a method | A function or procedure exposed by the bridge. |
| `expose` | Makes a `spec` public | Marks a bridge method as accessible from outside. |
| `forward` | Returns a value | Used within a `spec` to send a result back to the caller. |
| `link` | Connects to a bridge | Binds a variable to a bridge implementation, allowing its methods to be called. |
| `inlet` | Entry point for interaction | A special block that often initiates interaction with a bridge. |

---

## 2. Declaring a Bridge

A `bridge` is declared with a name and a set of `exposed` specifications (`spec`). These specs define the "contract" of the bridge.

```beacon
bridge Calculator {
    expose spec add(a, b)
    expose spec subtract(a, b)
}
```

---

## 3. Implementing a Bridge

A `toolkit` or `blueprint` can implement a bridge's `spec`s. The implementation contains the actual logic for the exposed methods.

```beacon
toolkit BasicMath {
    spec add(a, b) {
        forward a + b
    }

    spec subtract(a, b) {
        forward a - b
    }
}
```

---

## 4. Linking and Using a Bridge

To use a bridge, you `link` a variable to an implementation that fulfills the bridge's contract. This allows you to call the bridge's methods on the linked variable.

```beacon
< Assuming BasicMath toolkit is available >

inlet {
    link my_calculator to BasicMath

    sum = my_calculator.add(10, 5)
    show("Sum: |sum|") < Output: Sum: 15 >

    difference = my_calculator.subtract(10, 5)
    show("Difference: |difference|") < Output: Difference: 5 >
}
```

---

## 5. Nested and Embedded Bridges

Bridges can be composed. You can `embed` one bridge within another to create more complex interaction patterns, such as adding an authentication layer to a user interface.

```beacon
bridge AuthBridge {
    expose spec validate(token)
}

toolkit SimpleAuth {
    spec validate(token) {
        check token == "beacon123" {
            forward "Access Granted"
        }
        forward "Access Denied"
    }
}

bridge UserInterface {
    embed AuthBridge
    expose spec login(user_token)
}

toolkit AppUI {
    link auth to SimpleAuth

    spec login(user_token) {
        result = auth.validate(user_token)
        forward result
    }
}
```

---

## 6. User-Oriented Signal Flow

In a UOP design, interaction typically starts at an `inlet` and flows through `linked` bridges. This ensures a clear and predictable path for data and control.

```beacon
inlet {
    link ui to AppUI
    
    token = ask("Enter your token: ")
    response = ui.login(token)
    
    show(response)
}
```

---

## 7. Summary

- **Bridges** define the "what" (the interface and its methods).
- **Toolkits** or **Blueprints** provide the "how" (the implementation of those methods).
- **Links** connect the "what" to the "how," making the bridge usable.
- **Inlets** are the starting points for user interaction with the system through bridges.

Beacon's bridge system promotes a clean separation of concerns, making code more modular, reusable, and easier to understand from a user's perspective.
