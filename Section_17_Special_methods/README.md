# 🧪 Section 17: Special Methods (Dunders)  
## Master Python Magic Methods

🧠 **Learn how to customize the behavior of your classes** using special methods (also known as **dunder methods**, because they start and end with double underscores `__`).

These methods allow you to define what happens when built-in operations like:
- Printing an object (`print(obj)`)
- Comparing objects (`obj1 == obj2`)
- Hashing for use in sets/dicts
- Truth testing (`if obj:`)
- Object destruction

are used on instances of your class.



## 🧠 What You'll Learn

- 🖨️ `__str__()` – Return a user-friendly string representation
- 🧾 `__repr__()` – Return an unambiguous, developer-friendly representation
- ✅ `__eq__()` – Define equality between two objects
- 🔢 `__hash__()` – Make objects hashable for use in sets or as dict keys
- 🚦 `__bool__()` – Control truthiness of an object
- 🗑️ `__del__()` – Handle cleanup before object destruction
- 💡 Hidden notes and best practices for writing clean, idiomatic dunder methods



## 🖨️ `__str__` – Human-readable Output

Used by `print()` and `str()` to get a **user-friendly** string representation.

🔹 **Example – Customizing output**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

p = Person("Alice", 30)
print(p)  # Output: Alice, 30 years old
```

🔸 If `__str__` is not defined, Python falls back to `__repr__`.



## 🧾 `__repr__` – Developer-friendly Representation

Used by `repr()` and in the REPL to show **unambiguous** representations. Useful for debugging.

🔹 **Example – Debugging output**
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"
```

🔸 **Best Practice:** The output should ideally be valid Python code that can recreate the object.



## ✅ `__eq__` – Define Equality Logic

By default, custom objects are compared by identity (memory address). Use `__eq__()` to compare by value instead.

🔹 **Example – Compare by values**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

p1 = Point(2, 3)
p2 = Point(2, 3)

print(p1 == p2)  # True
```

🔸 This lets you check if two objects have the same data, not just if they're the same instance.



## 🔢 `__hash__` – Enable Use in Sets & Dictionaries

If you want to store instances of a class in a set or as dictionary keys, you must define `__hash__()`.

🔹 **Example – Make Point hashable**
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

p1 = Point(2, 3)
p2 = Point(2, 3)

s = {p1, p2}
print(s)  # Output: {Point(x=2, y=3)}
```

🔸 Ensure that `__hash__()` returns the same value for objects considered equal.



## 🚦 `__bool__` – Determine Truthiness

Controls whether an object evaluates to `True` or `False` in boolean contexts like `if`, `while`, etc.

🔹 **Example – Customize object truth value**
```python
class Order:
    def __init__(self, items):
        self.items = items

    def __bool__(self):
        return len(self.items) > 0

order = Order([])
if order:
    print("Order has items")
else:
    print("Order is empty")  # This will print
```

🔸 By default, any custom object returns `True`. Override this to make logic more intuitive.



## 🗑️ `__del__` – Cleanup Before Destruction

Called when an object is about to be destroyed by the garbage collector.

🔹 **Example – Logging deletion**
```python
class TempFile:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")

    def __del__(self):
        print(f"{self.name} deleted")

f = TempFile("temp.txt")
del f
```

🔸 **Note:** Don’t rely on `__del__` for critical resource management (like file closing). Use context managers (`with`) or explicit close methods instead.



## 📌 Real-World Example – User Account Class

Let’s apply multiple dunder methods to a realistic class:

```python
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return f"User({self.username}, {self.email})"

    def __repr__(self):
        return f"User(username='{self.username}', email='{self.email}')"

    def __eq__(self, other):
        return self.username == other.username and self.email == other.email

    def __hash__(self):
        return hash((self.username, self.email))

    def __bool__(self):
        return bool(self.username)

# Usage
u1 = User("alice", "alice@example.com")
u2 = User("alice", "alice@example.com")

print(u1)               # User(alice, alice@example.com)
print(repr(u1))         # User(username='alice', email='alice@example.com')
print(u1 == u2)         # True
print(hash(u1))         # Same hash as u2

users = {u1, u2}
print(users)             # {User(username='alice', email='alice@example.com')}
```



## 💡 Hidden Tips & Notes

- 🧩 Always implement both `__eq__` and `__hash__` together — if you override one, you should override the other.
- 📝 `__repr__` should ideally return something that could recreate the object (e.g., `eval(repr(obj))` works).
- 🧱 Avoid side effects in `__del__` — it's not guaranteed to run immediately.
- 🧵 Use `__bool__` to control logic like `if user:` rather than checking attributes manually.
- 🧠 Prefer immutable types for hashable objects — mutable objects should not be hashable.
- 🧹 Consider using `@dataclass(eq=True)` to auto-generate `__eq__`, `__repr__`, and more.



## 📌 Summary

| Method | Purpose |
|--------|---------|
| `__str__()` | Readable string representation (`print()`, `str()`) |
| `__repr__()` | Unambiguous, developer-friendly representation (`repr()`) |
| `__eq__()` | Define object equality |
| `__hash__()` | Allow use in sets and as dict keys |
| `__bool__()` | Control truth value |
| `__del__()` | Called before object destruction |



🎉 Congratulations! You now understand how to **customize the behavior of your Python classes** using **special (dunder) methods** like `__str__`, `__repr__`, `__eq__`, and more.

Next up: 🔐 **Section 18: Property Management** – learn how to control attribute access and validation using `@property` and setters.
