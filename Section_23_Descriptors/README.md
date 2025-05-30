# 🧰 Section 23: Descriptors  
## Mastering Attribute Access in Python

🧩 **Learn how to control and customize attribute access in Python using descriptors**, a powerful feature that allows you to manage object state with fine-grained logic.

This section covers:
- 🧠 What are descriptors and how they work
- 📦 The difference between **data descriptors** and **non-data descriptors**
- 🔁 How to implement `__get__`, `__set__`, and `__delete__`
- 💡 Hidden notes and best practices for writing clean, reusable descriptor classes
- 🧪 Real-world examples including validation and lazy property computation



## 🧠 What You'll Learn

| Concept | Description |
|--------|-------------|
| **Descriptors** | Objects that customize attribute access via `__get__`, `__set__`, and `__delete__` |
| **Data Descriptors** | Implement both `__get__` and `__set__` (e.g., `property`) |
| **Non-data Descriptors** | Only implement `__get__` (e.g., `staticmethod`, `classmethod`) |
| **Attribute Lookup Precedence** | Data descriptors override instance attributes |
| **Use Cases** | Type checking, lazy evaluation, computed properties |
| **Best Practices** | Keep descriptors simple and focused |



## 🧱 Understanding Descriptors

Descriptors are Python’s way of **customizing attribute access**. They allow you to define behavior when getting, setting, or deleting an attribute.

🔹 Descriptor Protocol:
- `__get__(self, instance, owner)` – Called when the attribute is accessed
- `__set__(self, instance, value)` – Called when the attribute is assigned a value
- `__delete__(self, instance)` – Called when the attribute is deleted

### 🎯 When Are Descriptors Used?

Descriptors power many built-in features like:
- `property`
- `classmethod`
- `staticmethod`

You can also create your own custom descriptors to enforce rules or compute values dynamically.



## 📦 Data vs Non-data Descriptors

There are two types of descriptors:

| Type | Methods Implemented | Example |
|------|---------------------|---------|
| **Data Descriptor** | `__get__` + `__set__` or `__delete__` | `property`, custom validators |
| **Non-data Descriptor** | Only `__get__` | `staticmethod`, `classmethod` |

🔸 **Important Rule:**  
In attribute lookup:
1. **Data descriptors** take priority over instance dictionaries.
2. Then instance attributes (`__dict__`)
3. **Non-data descriptors** come next
4. Lastly, class attributes



## 🛠️ Implementing a Simple Descriptor

Let's build a simple descriptor that ensures an attribute is always a string.

```python
class StringProperty:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"{self.name} must be a string")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]
```

🔹 **Usage:**
```python
class Person:
    name = StringProperty('name')

    def __init__(self, name):
        self.name = name

p = Person("Alice")
print(p.name)   # Alice

p.name = "Bob"  # Works fine
p.name = 100   # ❌ Raises ValueError
```

## 🔐 Descriptor for Validation – Email Property

Let’s create a descriptor that validates email format before storing it.

```python
import re

class EmailDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, value):
            raise ValueError("Invalid email address")
        instance.__dict__[self.name] = value
```

🔹 **Usage:**
```python
class User:
    email = EmailDescriptor('email')

    def __init__(self, email):
        self.email = email

u1 = User("test@example.com")  # ✅ Valid
u2 = User("invalid-email")    # ❌ Raises ValueError
```



## 🧮 Computed Properties Using Descriptors

You can use descriptors to compute values on-the-fly — ideal for derived data that doesn’t need to be stored.

🔹 **Example – Lazy Evaluation of Full Name**
```python
class FullName:
    def __get__(self, instance, owner):
        return f"{instance.first} {instance.last}"

class Person:
    full_name = FullName()

    def __init__(self, first, last):
        self.first = first
        self.last = last

p = Person("John", "Doe")
print(p.full_name)  # John Doe
```

🔸 No storage needed — value is generated each time.



## 🧩 Real-World Example – Temperature Converter

Let’s build a class where temperature is stored in Celsius but accessible as Fahrenheit too, using a non-data descriptor.

```python
class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.celsius * 9 / 5 + 32

    def __set__(self, instance, value):
        instance.celsius = (value - 32) * 5 / 9

class Temperature:
    fahrenheit = Fahrenheit()

    def __init__(self, celsius=0):
        self.celsius = celsius

temp = Temperature(37)
print(temp.fahrenheit)  # 98.6

temp.fahrenheit = 100
print(temp.celsius)     # 37.777...
```

🔸 This example shows how descriptors can encapsulate logic and provide seamless access to derived values.



## 🧱 Use Case – Type Checking with Descriptors

Use descriptors to ensure type safety across multiple attributes.

```python
class IntegerField:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f"{self.name} must be an integer")
        instance.__dict__[self.name] = value

class Product:
    price = IntegerField('price')
    quantity = IntegerField('quantity')

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
```

🔹 **Usage:**
```python
prod = Product(100, 10)
prod.price = 150       # ✅ Valid
prod.quantity = "five"  # ❌ Raises ValueError
```



## 🧪 Advanced Example – Lazy Image Loader

Use a descriptor to load image data only when accessed.

```python
class LazyImageLoader:
    def __init__(self, path):
        self.path = path
        self._cache = {}

    def __get__(self, instance, owner):
        if instance not in self._cache:
            print(f"Loading image from {self.path}")
            with open(self.path, 'r') as f:
                self._cache[instance] = f.read()
        return self._cache[instance]

class Image:
    content = LazyImageLoader('image.jpg')

img = Image()
print(img.content)  # Loads and caches
print(img.content)  # Returns cached version
```

🔸 This avoids loading large resources until needed.


## 💡 Hidden Tips & Notes

- 🧩 Descriptors are defined at the class level, not per instance.
- 📦 If you're writing a data descriptor, make sure to store the actual value correctly — usually in `__dict__`.
- 🧾 Non-data descriptors (only `__get__`) can still be overridden by instance attributes.
- 🧱 Use descriptors instead of property when you want to reuse logic across multiple classes.
- 🚫 Avoid side effects in `__get__()` unless intentional (like logging or lazy loading).
- 🧵 Descriptors help reduce boilerplate and centralize logic for common patterns like validation.



## 📌 Summary

| Feature | Purpose |
|--------|---------|
| **Descriptors** | Customize attribute access with `__get__`, `__set__`, and `__delete__` |
| **Data Descriptors** | Override both get and set — take precedence over instance dict |
| **Non-data Descriptors** | Only override `__get__` |
| **Validation Logic** | Enforce rules like type checks or format validation |
| **Computed Properties** | Generate values on-demand without storing them |
| **Lazy Loading** | Defer expensive operations until needed |
| **Reusability** | Share attribute logic across multiple classes |


🎉 Congratulations! You now understand how to use **Python descriptors** to manage attribute access with precision, including how to:
- Validate input values
- Create computed properties
- Implement lazy loading
- Reuse logic across classes

Next up: 🧪 **Section 24: Metaprogramming** – learn how to dynamically create classes and manipulate code at runtime using `__new__`, metaclasses, and `dataclass`.
