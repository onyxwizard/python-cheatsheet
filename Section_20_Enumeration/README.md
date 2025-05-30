# 🧩 Section 20: Enumeration  
## Working with Enums in Python

🔢 **Learn how to use enumerations (`Enum`) in Python** to define sets of named values — perfect for representing fixed, related constants like days of the week, status codes, or colors.

This section will teach you:
- 🧱 How to define an enumeration class
- 🧷 Understanding enum aliases and how to prevent them using `@unique`
- 🚀 Using `auto()` to generate unique values automatically
- 📦 Customize and extend enum classes with methods and logic
- 💡 Hidden tips and best practices for working with enums



## 🧠 What You'll Learn

| Concept | Description |
|--------|-------------|
| **Enumeration (`Enum`)** | A class that represents a set of constants |
| **Enum Members** | Named values inside an enum (e.g., `Color.RED`) |
| **Aliases** | Multiple names pointing to the same value |
| **`@enum.unique`** | Enforce uniqueness of member values |
| **`auto()`** | Automatically assign values to members |
| **Custom Methods** | Extend enums with custom behavior |
| **Extending Enums** | Create base enums to be inherited |
| **Iterating Members** | Loop through all members of an enum |



## 🧱 Defining an Enumeration

Use `Enum` from the `enum` module to create an enumeration class.

🔹 **Example – Define a simple color enum**
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

🔸 Each member has a name and a value:

```python
print(Color.RED)        # Output: Color.RED
print(Color.RED.name)   # Output: RED
print(Color.RED.value)  # Output: 1
```



## 🔍 Accessing Enum Members

You can access members by **name**, **value**, or **index**.

🔹 **By Name:**
```python
print(Color['GREEN'])  # Output: Color.GREEN
```

🔹 **By Value:**
```python
print(Color(2))        # Output: Color.GREEN
```

🔹 **Iterate Over Members:**
```python
for color in Color:
    print(color)
# Output:
# Color.RED
# Color.GREEN
# Color.BLUE
```



## 🧷 Enum Aliases – Same Value, Different Names

Enums allow multiple names to share the same value. These are called **aliases**.

🔹 **Example – Status Code Aliases**
```python
from enum import Enum

class StatusCode(Enum):
    OK = 200
    SUCCESS = 200  # alias of OK
    NOT_FOUND = 404
```

🔸 Here, `StatusCode.SUCCESS` is just an alias of `StatusCode.OK`.

🔹 **Check if two members are the same:**
```python
print(StatusCode.OK is StatusCode.SUCCESS)  # True
```



## 🚫 Prevent Duplicates with `@unique`

To ensure all values are unique, decorate your enum with `@unique` from the `enum` module.

🔹 **Example – Force Unique Values**
```python
from enum import Enum, unique

@unique
class PaymentStatus(Enum):
    PENDING = 1
    COMPLETED = 2
    REFUNDED = 3
```

🔸 If you try to duplicate a value:
```python
class PaymentStatus(Enum):
    PENDING = 1
    PROCESSING = 1  # ❌ ValueError: duplicate values found
```



## 🚀 Auto-generate Values with `auto()`

Avoid manually assigning values by using `auto()` — it auto-increments integer values starting from 1.

🔹 **Example – Use `auto()` to assign values**
```python
from enum import Enum, auto

class OrderStatus(Enum):
    PENDING = auto()
    SHIPPED = auto()
    DELIVERED = auto()

print(OrderStatus.DELIVERED.value)  # Output: 3
```

🔸 This makes enum definitions cleaner and less error-prone.



## 📦 Customize and Extend Enum Classes

Enums are full-fledged classes — so you can add methods and custom logic.

🔹 **Example – Add `__str__` method**
```python
class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3

    def __str__(self):
        return f"{self.name} ({self.value})"
```

🔹 **Usage:**
```python
print(Day.MONDAY)  # Output: Day.MONDAY (1)
```



## 🧰 Real-World Example – API Response Status

Let’s build an enum to represent HTTP response statuses with custom string formatting.

```python
from enum import Enum, auto

class ResponseStatus(Enum):
    OK = auto()
    CREATED = auto()
    BAD_REQUEST = auto()
    UNAUTHORIZED = auto()
    FORBIDDEN = auto()
    NOT_FOUND = auto()
    INTERNAL_SERVER_ERROR = auto()

    def __str__(self):
        return f"{self.name.replace('_', ' ').title()} ({self.value})"

    @property
    def is_success(self):
        return self in [ResponseStatus.OK, ResponseStatus.CREATED]
```

🔹 **Usage:**
```python
status = ResponseStatus.NOT_FOUND
print(status)              # Output: Not Found (404)
print(status.is_success)   # Output: False
```



## 🧬 Extend Custom Enum Classes

You can define a base `Enum` class and extend it with shared functionality.

🔹 **Example – Ordered Enum Comparison**

```python
from enum import Enum
from functools import total_ordering

@total_ordering
class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

    def __lt__(self, other):
        if isinstance(other, Priority):
            return self.value < other.value
        return NotImplemented
```

🔹 **Usage:**
```python
print(Priority.LOW < Priority.HIGH)  # True
```

🔸 This allows you to compare enum members based on their values.



## 📋 Iterating Over Enum Members

Enums are iterable, making it easy to list or process all options.

🔹 **Example – List All Days**
```python
class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

for day in Day:
    print(day.name)
```

🔸 Useful for generating dropdowns, validation checks, or logging available options.



## 🧱 Make Your Own Reusable Base Enum Class

Create a base class with reusable logic across different enums.

🔹 **Example – Base Enum with Helper Method**
```python
from enum import Enum

class CustomEnum(Enum):
    @classmethod
    def list_values(cls):
        return [member.value for member in cls]

class UserRole(CustomEnum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

print(UserRole.list_values())  # ['admin', 'user', 'guest']
```



## 🛑 Enums Are Immutable

Once defined, you cannot modify enum members or values.

🔹 **Example – Attempt to Modify Fails**
```python
try:
    Color.RED = 4  # ❌ Raises TypeError
except TypeError as e:
    print(e)
```

🔸 This ensures stability and prevents accidental changes.



## 💡 Hidden Tips & Notes

- 🧩 Use uppercase names for enum members by convention.
- 🧱 Prefer `auto()` unless specific values are required.
- 🧾 Avoid duplicate values unless explicitly needed (use `@unique` to enforce).
- 🧪 Use enums instead of strings or integers for better readability and safety.
- 📦 Add custom methods like `__str__`, `__repr__`, or properties to enhance usability.
- 🧵 You can iterate over enums for dynamic UIs, validation, or configuration.
- 🧠 Use enums for states, modes, categories, or any fixed set of choices.



## 📌 Summary

| Feature | Purpose |
|--------|---------|
| `class MyEnum(Enum)` | Define a new enumeration |
| `MyEnum.member_name` | Access a specific enum member |
| `MyEnum(member_value)` | Get member by value |
| `@unique` | Ensure all values are unique |
| `auto()` | Generate automatic values |
| `__str__`, `__repr__` | Customize output format |
| Properties / Methods | Add logic to enums |
| Inheritance | Build reusable enum base classes |
| Immutability | Prevent runtime modifications |



🎉 Congratulations! You now understand how to define and work with **Python enums**, including:
- Creating basic and advanced enumerations
- Managing aliases and ensuring uniqueness
- Using `auto()` for clean value assignment
- Adding methods and extending enums
- Iterating and checking members
- Keeping your code safe with immutability

Next up: 🧱 **Section 21: SOLID Principles** – learn how to write maintainable, scalable object-oriented designs.
