# 🧬 Section 22: Multiple Inheritance  
## Understanding and Using Multiple Inheritance in Python

🔁 **Learn how to create classes that inherit from multiple parent classes** — a powerful but sometimes confusing feature of Python’s object-oriented programming.

This section covers:
- 🧱 What is multiple inheritance?
- 🧭 How Python resolves method calls using MRO (Method Resolution Order)
- 🔄 The use of `super()` in multiple inheritance
- 🧩 Mixin classes for reusable behavior
- 💡 Hidden tips, best practices, and common pitfalls



## 🧠 What You'll Learn

| Concept | Description |
|--------|-------------|
| **Multiple Inheritance** | A class inherits from more than one base class |
| **MRO – Method Resolution Order** | Determines the order in which methods are resolved |
| **`super()`** | Calls the next class in the MRO, often used in constructors |
| **Mixins** | Classes that provide reusable functionality without being full base classes |
| **Diamond Problem** | When two parent classes share a common ancestor |
| **Avoiding Tight Coupling** | Design clean hierarchies without breaking encapsulation |



## 🧱 Introduction to Multiple Inheritance

In Python, a class can inherit from multiple parent classes. This allows you to combine behaviors from different sources into a single class.

🔹 **Basic Syntax:**
```python
class ChildClass(Parent1, Parent2, Parent3):
    pass
```

🔹 **Example – Flying Car**
```python
class Car:
    def start(self):
        print("Starting Car")

class Flyable:
    def fly(self):
        print("Flying Mode Activated")

class FlyingCar(Car, Flyable):
    pass
```

🔸 **Usage:**
```python
flying_car = FlyingCar()
flying_car.start()  # From Car
flying_car.fly()     # From Flyable
```

---

## 🧭 Method Resolution Order (MRO)

Python uses a depth-first, left-to-right algorithm called **MRO** to determine which method to call when multiple parents define the same method.

🔹 **Check MRO:**
```python
print(FlyingCar.__mro__)
# Output: (<class 'FlyingCar'>, <class 'Car'>, <class 'Flyable'>, <class 'object'>)
```

🔸 Or use:
```python
help(FlyingCar)  # Shows full MRO tree
```



## 🔁 Using `super()` with Multiple Inheritance

Use `super()` carefully in multiple inheritance to ensure all parent `__init__` methods are called correctly.

🔹 **Example – Proper Initialization**
```python
class Vehicle:
    def __init__(self):
        print("Initializing Vehicle")

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("Initializing Car")

class Flyable(Vehicle):
    def __init__(self):
        super().__init__()
        print("Initializing Flyable")

class FlyingCar(Car, Flyable):
    def __init__(self):
        super().__init__()
        print("Finalizing FlyingCar")
```

🔸 **Usage:**
```python
car = FlyingCar()
# Output:
# Initializing Vehicle
# Initializing Flyable
# Initializing Car
# Finalizing FlyingCar
```

📌 This works because of **C3 linearization**, Python's MRO algorithm.


## 🧩 Real-World Example – Employee with Skills and Dependents

Let’s build a system where an `Employee` class inherits from both `Person` and a mixin class that adds JSON serialization support.

### 🧱 Base Class – Person
```python
class Person:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} initialized")
```

### 🧩 Mixin – JSON Support
```python
class JsonSerializableMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)
```

### 🧬 Combining Both – Employee
```python
class Employee(Person, JsonSerializableMixin):
    def __init__(self, name, role, salary):
        super().__init__(name)
        self.role = role
        self.salary = salary
```

🔸 **Usage:**
```python
emp = Employee("Alice", "Developer", 90000)
print(emp.to_json())  # {"name": "Alice", "role": "Developer", "salary": 90000}
```



## 🧰 Introducing Mixin Classes

A **mixin** is a class that provides methods to other classes through inheritance but is not meant to be instantiated on its own.

🔹 **Example – Logging Mixin**
```python
class Loggable:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")
```

🔹 **Using Mixin in a Class**
```python
class User(Person, Loggable):
    def __init__(self, name):
        super().__init__(name)

user = User("Bob")
user.log("Logged in")  # [User] Logged in
```

🔸 Mixins help reduce code duplication by grouping reusable logic like logging, caching, or validation.



## 🧨 Avoiding the Diamond Problem

The **diamond problem** occurs when a child class inherits from two classes that both inherit from the same parent.

🔹 **Classic Diamond Problem:**
```python
class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    pass
```

🔸 Now calling `D().greet()` will run `B.greet()` since it comes first in MRO.

🔹 **Why? Because of C3 Linearization:**
```python
print(D.__mro__)
# D -> B -> C -> A -> object
```

🔸 This ensures only one path is followed — avoiding ambiguity.


## 🧪 Real-World Use Case – Payment Gateway System

Let’s create a system where a payment processor can support multiple interfaces.

### 🧱 Base Classes
```python
class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError()

class RefundProcessor:
    def process_refund(self, amount):
        raise NotImplementedError()
```

### 🧩 Mixins
```python
class LoggingMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class AuditMixin:
    def audit(self, action):
        print(f"Audit: {action}")
```

### 🧬 Combined Processor
```python
class HybridPaymentProcessor(PaymentProcessor, RefundProcessor, LoggingMixin, AuditMixin):
    def process_payment(self, amount):
        self.log(f"Processing payment of ${amount}")
        self.audit("payment_processed")
        print(f"Paid ${amount}")

    def process_refund(self, amount):
        self.log(f"Processing refund of ${amount}")
        self.audit("refund_processed")
        print(f"Refunded ${amount}")
```

🔸 **Usage:**
```python
processor = HybridPaymentProcessor()
processor.process_payment(100)
# Output:
# [LOG] Processing payment of $100
# Audit: payment_processed
# Paid $100
```



## 💡 Hidden Tips & Notes

- 🧩 Use `__mro__` or `help(Class)` to inspect method resolution order.
- 🧱 Always call `super().__init__()` in parent classes to ensure proper initialization.
- 📦 Prefer shallow inheritance trees — deep ones become hard to maintain.
- 🧵 Mixins should have clear names like `JsonSerializable`, `Loggable`, `CacheMixin`.
- 🧾 Mixins shouldn’t have their own state unless necessary — keep them lightweight.
- 🚫 Don't overuse multiple inheritance — prefer composition (`has-a`) over inheritance (`is-a`) when possible.
- 🧠 Understand the **C3 linearization algorithm** used by Python for MRO.


## 📌 Summary

| Feature | Purpose |
|--------|---------|
| **Multiple Inheritance** | Combine features from multiple parent classes |
| **MRO (Method Resolution Order)** | Define which method gets called in case of conflict |
| **`super()`** | Call parent logic safely across multiple paths |
| **Mixins** | Add reusable behavior without deep hierarchies |
| **Diamond Problem** | Occurs when two classes share a common ancestor |
| **Best Practice** | Keep inheritance chains shallow and meaningful |


🎉 Congratulations! You now understand how to effectively use **multiple inheritance in Python**, including how to resolve conflicts with MRO and how to write modular, reusable mixins.

Next up: 🧰 **Section 23: Descriptors** – learn how to manage attribute access at a deeper level using descriptors.