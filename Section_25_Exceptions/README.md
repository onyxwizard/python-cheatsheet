# 🧾 Section 25: Exceptions in OOP  
## Handling and Raising Exceptions in Object-Oriented Python

⚙️ **Learn how to handle and raise exceptions effectively within classes**, create custom exception hierarchies, and ensure your object-oriented code remains robust and maintainable.

This section covers:
- 🧠 Exception handling inside class methods
- 📦 How to raise exceptions from objects
- 🔄 Raise an exception from another exception with context (`raise ... from`)
- 🧩 Creating custom exception classes for better error categorization
- 💡 Hidden tips and best practices for working with exceptions in OOP



## 🧠 What You'll Learn

| Concept | Description |
|--------|-------------|
| **Exception Handling in Classes** | Use `try...except` blocks inside methods |
| **Raising Exceptions** | Throw errors using `raise` inside a method |
| **Chaining Exceptions** | Use `raise ... from` to show cause of error |
| **Custom Exception Classes** | Define your own exception types for clarity |
| **Error Propagation** | Handle or propagate exceptions up the call stack |
| **Best Practices** | When to catch, when to raise, and how to organize exception logic |



## 🛠️ Exception Handling Inside Class Methods

Just like regular functions, you can use `try...except` blocks inside methods to handle runtime errors gracefully.

🔹 **Example – Safe division inside a class**
```python
class Calculator:
    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print("Cannot divide by zero")
            return None
```

🔹 **Usage:**
```python
calc = Calculator()
print(calc.divide(10, 0))  # Output: Cannot divide by zero → None
```

🔸 This keeps your program running even if an error occurs during execution.



## 🚨 Raising Exceptions in Methods

Sometimes, it's better to **raise an exception** than silently fail — especially when validation fails.

🔹 **Example – Validate input before processing**
```python
class Order:
    def __init__(self, item_count):
        if item_count <= 0:
            raise ValueError("Order must have at least one item")
        self.item_count = item_count
```

🔹 **Usage:**
```python
try:
    order = Order(0)
except ValueError as e:
    print(f"Validation failed: {e}")
```

🔸 This ensures that invalid states are caught early and handled appropriately.


## 🔁 Raising One Exception From Another

Use `raise ... from` to provide additional context when converting one exception into another.

🔹 **Example – Translate low-level exceptions**
```python
class FileReader:
    def __init__(self, filename):
        try:
            self.file = open(filename, 'r')
        except FileNotFoundError as ex:
            raise ValueError(f"File '{filename}' not found") from ex
```

🔹 **Usage:**
```python
try:
    reader = FileReader("nonexistent.txt")
except ValueError as e:
    print(f"Caught error: {e}")
    print("Original cause:", repr(e.__cause__))
```

🔸 This helps with debugging by showing both the high-level error and its root cause.


## 🧱 Creating Custom Exception Classes

Create your own exception hierarchy to make errors more meaningful and easier to catch.

🔹 **Example – Custom exceptions for a payment system**
```python
class PaymentError(Exception):
    """Base class for all payment-related errors"""
    pass

class InvalidPaymentMethod(PaymentError):
    def __init__(self, method):
        super().__init__(f"Invalid payment method: {method}")

class InsufficientFunds(PaymentError):
    def __init__(self, balance, amount):
        super().__init__(
            f"Insufficient funds. Balance: ${balance}, Required: ${amount}"
        )
```

🔹 **Usage:**
```python
def process_payment(method, amount, balance):
    if method not in ['credit_card', 'paypal']:
        raise InvalidPaymentMethod(method)
    if amount > balance:
        raise InsufficientFunds(balance, amount)

try:
    process_payment('bitcoin', 100, 200)
except InvalidPaymentMethod as e:
    print(f"[Payment] {e}")
```

🔸 This makes your error messages clearer and allows you to catch specific types of errors.



## 🧩 Real-World Example – Temperature Converter with Custom Errors

Let’s build a temperature conversion system with meaningful exception handling.

### 🧱 Define Custom Exceptions
```python
class ConversionError(Exception):
    pass

class InvalidUnitError(ConversionError):
    def __init__(self, unit):
        super().__init__(f"Unsupported unit: {unit}")
```

### 🧪 Conversion Logic with Exception Handling
```python
def convert_temperature(value, from_unit, to_unit):
    valid_units = ('celsius', 'fahrenheit', 'kelvin')
    
    if from_unit not in valid_units:
        raise InvalidUnitError(from_unit)
    if to_unit not in valid_units:
        raise InvalidUnitError(to_unit)

    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return value * 9/5 + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
```

🔹 **Usage:**
```python
try:
    temp = convert_temperature(100, 'celcius', 'fahrenheit')
except InvalidUnitError as e:
    print(f"Conversion failed: {e}")
```



## 🧬 Extend Custom Exception Hierarchy

You can define multiple exception types that inherit from a base exception class to allow catching broad or specific errors.

🔹 **Example – Error hierarchy**
```python
class AppError(Exception):
    pass

class InputError(AppError):
    pass

class DatabaseError(AppError):
    pass

class NotFoundError(DatabaseError):
    pass
```

🔹 **Usage:**
```python
try:
    raise NotFoundError("User not found")
except DatabaseError as e:
    print(f"Database error: {e}")
```

🔸 This is useful in larger applications where different layers may raise different types of exceptions.



## 🧰 Best Practices for Exceptions in OOP

| Practice | Description |
|---------|-------------|
| 🧱 Always inherit from `Exception`, not `BaseException` | For application-specific errors |
| 🧩 Keep exception classes lightweight | Just override `__init__` and maybe `__str__` |
| 📦 Group related exceptions under a common base class | E.g., `AppError`, `PaymentError` |
| 🧾 Raise exceptions early and clearly | Don't hide errors in silent returns |
| 🔁 Convert low-level exceptions to higher-level ones | With `raise ... from` for debugging |
| 🛑 Avoid bare `except:` clauses | Catch specific exceptions instead |
| 🧠 Use docstrings in custom exceptions | Helps with documentation and clarity |
| 📝 Log exceptions in production | Especially those raised in complex systems |



## 🧪 Advanced Example – User Management System

Let’s implement a user management system with custom exceptions and proper error handling.

### 🧱 Define Custom Exception Hierarchy
```python
class UserError(Exception):
    pass

class UserNotFoundError(UserError):
    pass

class DuplicateUserError(UserError):
    pass
```

### 🧩 Implement Service with Exceptions
```python
class UserService:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email):
        if username in self.users:
            raise DuplicateUserError(username)
        self.users[username] = email

    def get_user_email(self, username):
        if username not in self.users:
            raise UserNotFoundError(username)
        return self.users[username]
```

🔹 **Usage:**
```python
service = UserService()

try:
    service.add_user("alice", "alice@example.com")
    service.add_user("alice", "another@example.com")
except DuplicateUserError as e:
    print(f"Duplicate user: {e}")
```



## 💡 Hidden Tips & Notes

- 🧠 All custom exceptions should inherit from `Exception`, not `BaseException`.
- 📦 Define custom exceptions once and reuse them across your project.
- 🧵 Prefer raising exceptions over returning error codes or `None`.
- 🧾 Use `__repr__()` or `__str__()` in custom exceptions for better logging.
- 🧐 Use `try...except` to handle external failures (files, APIs), but validate input early.
- 🧠 Exceptions should be part of your design — not just added after bugs appear.
- 🧩 Use `finally` to clean up resources like files or connections even if an exception is raised.


## 📌 Summary

| Feature | Purpose |
|--------|---------|
| **Handling in Methods** | Use `try...except` inside class logic |
| **Raising Exceptions** | Prevent invalid object state or inputs |
| **`raise ... from`** | Chain exceptions for debugging and context |
| **Custom Exception Classes** | Improve error categorization and readability |
| **Exception Hierarchy** | Organize errors by type and severity |
| **Best Practices** | Keep exceptions clear, consistent, and well-documented |



🎉 Congratulations! You now understand how to work with **exceptions in object-oriented Python**, including:
- Handling exceptions inside class methods
- Raising exceptions for invalid states
- Chaining exceptions for debugging
- Defining and organizing custom exception hierarchies
- Applying best practices in real-world scenarios

This completes our full roadmap from **Python fundamentals to advanced object-oriented programming**!



## 🎯 Final Roadmap Overview

Here’s a quick recap of all sections:

### Fundamentals
- Variables, Strings, Numbers, Booleans, Constants, Comments, Type Conversion

### Operators
- Arithmetic, Assignment, Comparison, Logical

### Control Flow
- `if...else`, Ternary Operator, `for`, `while`, `break`, `continue`, `pass`

### Functions
- Define, Call, Default parameters, Keyword arguments, Recursive, Lambda, Docstrings

### Lists
- List operations, Tuples, Comprehensions, Slicing, Sorting, Unpacking

### Dictionaries
- Dictionary operations, Comprehensions

### Sets
- Set operations, Comprehensions, Frozen sets

### Exception Handling
- `try...except`, `else`, `finally`, `raise`, `raise ... from`

### Loops (Advanced)
- `for...else`, `while...else`, Emulate `do...while`

### More on Functions
- `*args`, `**kwargs`, Partial functions, Type hints

### Modules & Packages
- Importing modules, Working with packages, `__name__`, Private functions

### Working with Files
- Read, Write, Append, Rename, Delete, CSV

### Working Directories
- Get current directory, Traverse files, Create/delete directories

### Strings
- Raw strings, F-strings, Escape sequences

### Third-party Packages
- `pip`, `requirements.txt`, Virtual environments, `pipenv`

### OOP Basics
- Class definition, Instance vs class variables, `__init__`, Static methods

### Special Methods
- `__str__`, `__repr__`, `__eq__`, `__hash__`, `__bool__`, `__del__`

### Property Management
- `@property`, setters, read-only properties, computed values

### Inheritance
- Single inheritance, `super()`, `__slots__`, Abstract base classes

### Enumeration
- Define fixed sets of constants with `Enum`, prevent duplicates with `@unique`, auto-generate values with `auto()`

### SOLID Principles
- SRP, OCP, LSP, ISP, DIP

### Descriptors
- `__get__`, `__set__`, data vs non-data descriptors

### Metaprogramming
- `__new__`, dynamic class creation with `type()`, custom metaclasses, `dataclass`

### Exceptions in OOP
- Handle and raise exceptions inside classes
- Define custom exception hierarchies
- Use `raise ... from` for debugging



📌 You’ve completed a comprehensive journey through Python programming — from basic syntax to advanced object-oriented patterns.

🎯 Fork this repository, follow along, and start building clean, scalable, and maintainable Python applications today!
