# 🧪 Section 24: Metaprogramming  
## Understanding `__new__`, `type`, and Metaclasses in Python

🔮 **Learn how to write code that writes or manipulates other code at runtime** using metaprogramming techniques like:
- `__new__` method
- `type()` function
- Custom metaclasses
- Metaclass-based feature injection
- `dataclass` for auto-generated methods

This section gives you a deep understanding of **how classes are created**, how to manipulate them dynamically, and when to use these advanced features effectively.



## 🧠 What You'll Learn

| Concept | Description |
|--------|-------------|
| `__new__()` | Control object creation before `__init__` |
| `type()` | Built-in class factory — the default metaclass |
| **Metaclasses** | Classes that create other classes |
| **Metaclass Example** | Injecting functionality into multiple classes |
| `@dataclass` | Automatically generate special methods like `__init__` and `__repr__` |
| 💡 Hidden notes on best practices, pitfalls, and real-world uses |



## 🛠️ The `__new__` Method – Controlling Object Creation

The `__new__()` method is called **before `__init__()`** and is responsible for creating the instance.

🔹 **Example – Customizing Instance Creation**
```python
class Person:
    def __new__(self, name):
        print("Creating new instance")
        return super().__new__(self)

    def __init__(self, name):
        self.name = name
        print("Initializing instance")

p = Person("Alice")
```

🔸 **Output:**
```
Creating new instance
Initializing instance
```

🔹 **Use Case – Singleton Pattern**
```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

🔸 This ensures only one instance ever exists.



## 🧱 Using `type()` to Dynamically Create Classes

Python allows dynamic class creation using the built-in `type()` function.

🔹 **Basic Syntax:**
```python
type(name, bases, attrs)
```

- `name`: Name of the class
- `bases`: Tuple of base classes
- `attrs`: Dictionary of attributes and methods

🔹 **Example – Dynamic Class Creation**
```python
def say_hello(self):
    print(f"Hello, I'm {self.name}")

Person = type('Person', (), {
    'name': None,
    '__init__': lambda self, name: setattr(self, 'name', name),
    'greet': say_hello
})

p = Person("Alice")
p.greet()  # Hello, I'm Alice
```

🔸 This is useful in frameworks, plugins, or DSL (domain-specific language) generation.



## 🔮 What is a Metaclass?

A **metaclass** is a class whose instances are **classes**. It defines how a class behaves — think of it as a **class for classes**.

🔹 **Default Metaclass:** `type`
```python
class MyClass:
    pass

print(type(MyClass))  # <class 'type'>
```

🔸 All classes are instances of `type`.



## 🧬 Define Your Own Metaclass

Create a custom metaclass by inheriting from `type`.

🔹 **Example – Add a timestamp on class creation**
```python
import time

class TimestampMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f"[{time.time()}] Creating class {name}")
        return super().__new__(cls, name, bases, attrs)

class MyNewClass(metaclass=TimestampMeta):
    pass
```

🔸 Every time a class with this metaclass is defined, it logs a timestamp.



## 🧩 Metaclass Example – Auto-Inject Methods

Inject common functionality across many classes using a metaclass.

🔹 **Example – Add `log()` to all classes**
```python
class LoggerMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['log'] = lambda self, msg: print(f"[{self.__class__.__name__}] {msg}")
        return super().__new__(cls, name, bases, attrs)

class Animal(metaclass=LoggerMeta):
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    pass

dog = Dog("Buddy")
dog.log("Woof!")  # [Dog] Woof!
```

🔸 This pattern helps inject logging, validation, or serialization logic automatically.



## 📦 Use Case – Enforce Interface Requirements

Use metaclasses to ensure certain methods are implemented.

🔹 **Example – Require `save()` method**
```python
from abc import ABCMeta, abstractmethod

class ModelMeta(ABCMeta):
    def __new__(cls, name, bases, namespace):
        if 'save' not in namespace:
            raise TypeError("Must implement save()")
        return super().__new__(cls, name, bases, namespace)

class DatabaseModel(metaclass=ModelMeta):
    @abstractmethod
    def save(self):
        pass

class User(DatabaseModel):
    def save(self):
        print("Saving user to DB...")

u = User()
u.save()
```

🔸 If `save()` is missing, Python raises an error at class definition time.



## 🧰 Real-World Example – Auto-register Subclasses

Use a metaclass to automatically register subclasses — great for plugin systems.

🔹 **Example – Plugin Registry**
```python
class PluginMeta(type):
    registry = {}

    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        name = getattr(new_class, 'name', None)
        if name:
            cls.registry[name] = new_class
        return new_class

class Plugin(metaclass=PluginMeta):
    name = None

class EmailPlugin(Plugin):
    name = "email"

class SmsPlugin(Plugin):
    name = "sms"
```

🔹 **Usage – Get class by name:**
```python
plugin_name = "email"
plugin_class = PluginMeta.registry[plugin_name]
plugin = plugin_class()
```



## 📐 `@dataclass` – Reduce Boilerplate Code

Introduced in Python 3.7, `@dataclass` automatically generates `__init__`, `__repr__`, and more.

🔹 **Example – Simple data model**
```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    in_stock: bool = True

product = Product("Laptop", 999.0)
print(product)  # Product(name='Laptop', price=999.0, in_stock=True)
```

🔸 Other options include:
- `@dataclass(order=True)` – enable comparisons
- `@dataclass(frozen=True)` – make immutable objects
- `@dataclass(kw_only=True)` – force keyword-only arguments



## 🧪 Advanced Example – Audit Log Metaclass

Build a metaclass that adds audit capabilities to any class.

```python
import time

class AuditableMeta(type):
    def __new__(cls, name, bases, attrs):
        original_init = attrs.get('__init__', lambda self: None)

        def wrapped_init(self, *args, **kwargs):
            print(f"[Audit] Initializing {name} at {time.time()}")
            original_init(self, *args, **kwargs)

        attrs['__init__'] = wrapped_init
        return super().__new__(cls, name, bases, attrs)

class Order(metaclass=AuditableMeta):
    def __init__(self, order_id):
        self.order_id = order_id

order = Order(123)
# Output: [Audit] Initializing Order at 1681005123.123
```



## 💡 Hidden Tips & Notes

- 🧩 `__new__` is used less often than `__init__`, but it's essential for immutables like `str`, `int`, and `tuple`.
- 🧱 `type()` is the default metaclass — don’t override unless necessary.
- 🧾 Metaclasses affect class creation, not instance creation.
- 📦 Use metaclasses for cross-cutting concerns like logging, validation, or registration.
- 🚫 Don't overuse metaclasses — prefer composition and decorators where possible.
- 🧵 Metaclasses can be combined with `classmethod` and `abstractmethod` for powerful design patterns.
- 🧠 `@dataclass` reduces boilerplate for data models — use it instead of manually writing `__init__` and `__repr__`.



## 📌 Summary

| Feature | Purpose |
|--------|---------|
| `__new__()` | Control instance creation before initialization |
| `type()` | Dynamically create classes at runtime |
| **Metaclass** | Define behavior for class creation |
| **Custom Metaclass** | Inject methods, enforce requirements, auto-register subclasses |
| `@dataclass` | Auto-generate `__init__`, `__repr__`, etc. |
| **Best Practice** | Prefer composition and avoid complex metaprogramming unless necessary |



🎉 Congratulations! You now understand how to **write and use metaprogramming features** in Python, including:
- How to control object creation with `__new__`
- How to dynamically create classes with `type()`
- How to define and use custom metaclasses
- When and how to use `@dataclass` to reduce boilerplate

Next up: 🧾 **Section 25: Exceptions in OOP** – learn how to handle exceptions inside classes and build your own exception hierarchy.
