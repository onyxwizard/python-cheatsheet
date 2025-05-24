# 🧬 Section 16: Classes and Objects  
## Object-Oriented Programming in Python

🧩 **Learn the core concepts of object-oriented programming (OOP)** in Python — including classes, objects, instance and class variables, constructors (`__init__`), private attributes, and static methods.

This section gives you a solid foundation to start building reusable, modular, and maintainable code using OOP principles in Python.



## 🧠 What You'll Learn

- 🧱 How to define a **class** and create **objects**
- 📦 Understand **instance variables** vs **class variables**
- 🔐 Use **private attributes** for encapsulation
- 🛠️ Define and use the `__init__()` constructor method
- 📌 Differentiate between **methods** and **functions**
- 📎 Use **static methods** to group utility functions inside a class
- 💡 Hidden notes and best practices for writing clean class-based code



## 🧱 Defining a Class

A **class** is a blueprint or template for creating objects. It defines the structure and behavior that all instances of the class will have.

🔹 **Syntax:**
```python
class ClassName:
    # class body
```

🔹 **Example – Person class**
```python
class Person:
    pass
```

🔸 You can create an object (instance) from a class like this:
```python
person = Person()
print(person)  # Output: <__main__.Person object at 0x...>
```



## 🚶 Creating Objects

An **object** is an instance of a class. Every time you instantiate a class, you get a new object with its own state.

🔹 **Example – Create multiple Person objects**
```python
p1 = Person()
p2 = Person()

print(p1 == p2)  # Output: False (they are different objects)
```



## 📦 Instance Variables

Instance variables store data unique to each object. They are usually defined inside the `__init__()` method.

🔹 **Example – Add name and age to Person**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print(p1.name, p1.age)  # Alice 30
print(p2.name, p2.age)  # Bob 25
```

🔸 Each instance has its own copy of the `name` and `age`.



## 🧱 Class Variables

Class variables are shared across all instances of a class. They are useful for constants or shared state.

🔹 **Example – Track number of people**
```python
class Person:
    count = 0  # Class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print(Person.count)  # Output: 2
```

🔸 All instances access the same `count`. Changes reflect globally.


<img width="732" alt="class" src="https://github.com/user-attachments/assets/7dc9a8fd-ab21-4b62-b60c-c53c473b65df" />

## 🔒 Private Attributes

Prefix with `_` for internal use, or `__` for **name-mangled** private attributes.

🔹 **Example – Prevent direct access to balance**
```python
class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount("Alice", 1000)
acc.deposit(500)
print(acc.get_balance())  # Output: 1500
```

🔸 Trying to access `acc.__balance` raises an error (due to name mangling).


## 🛠️ The `__init__()` Method

The `__init__()` method is called automatically when a new object is created. It initializes the object's attributes.

🔹 **Example – Default values in `__init__`**
```python
class Product:
    def __init__(self, name, price=0):
        self.name = name
        self.price = price

item1 = Product("Laptop")
item2 = Product("Phone", 499)

print(item1.price)  # Output: 0
print(item2.price)  # Output: 499
```

🔸 You can set default parameter values to make some fields optional.



## 📎 Methods vs Functions

A **method** is a function defined inside a class and is associated with an object.

🔹 **Example – A simple method**
```python
class Greeter:
    def greet(self):
        print("Hello!")

g = Greeter()
g.greet()  # Output: Hello!
```

🔸 `self` refers to the current instance and must be the first argument in every method.



## 📄 Static Methods

Use `@staticmethod` to define utility methods that don't require access to instance or class data.

🔹 **Example – Utility method**
```python
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

result = MathUtils.add(10, 20)
print(result)  # Output: 30
```

🔸 Static methods are not tied to any object and behave like regular functions.



## 🧩 Real-World Example – User Login System

Let’s build a simple user login system to apply what we've learned:

```python
class User:
    active_users = 0  # Class variable

    def __init__(self, username, password):
        self.username = username
        self.__password = password  # Private attribute
        User.active_users += 1

    def login(self, entered_password):
        if self.__password == entered_password:
            print("Login successful!")
        else:
            print("Invalid credentials.")

    def logout(self):
        User.active_users -= 1
        print("User logged out.")

    @staticmethod
    def check_password_strength(password):
        return len(password) >= 8

# Usage
user1 = User("alice", "securepass123")
user1.login("wrongpass")       # Invalid credentials.
user1.login("securepass123")   # Login successful!

print(User.check_password_strength("weak"))  # False
print(User.check_password_strength("stronger"))  # True
```



## 💡 Hidden Tips & Notes

- 🧩 Always use `self` as the first parameter in instance methods.
- 🧱 Class variables should be accessed via the class name (e.g., `ClassName.variable`) instead of `self`, unless overridden.
- 🔐 Prefix sensitive attributes with `__` to prevent accidental modification.
- 📝 Avoid defining methods outside `__init__()` without clear purpose.
- 🧵 Use static methods for logic that belongs to the class but doesn’t modify instance or class data.
- 🧠 Consider using `@property` and setters for better control over attribute access.



## 📌 Summary

| Concept | Description |
|--------|-------------|
| **Class** | Blueprint for creating objects |
| **Object** | Instance of a class |
| **Instance Variables** | Unique per object (e.g., `self.name`) |
| **Class Variables** | Shared among all instances |
| **Private Attributes** | Prefixed with `__` for encapsulation |
| **Constructor `__init__()`** | Initializes object attributes |
| **Methods** | Functions defined inside a class |
| **Static Methods** | Not tied to instance or class |



🎉 Congratulations! You now understand how to define and work with **classes and objects** in Python, including how to manage state, enforce encapsulation, and write reusable logic.

Next up: 🧪 **Section 17: Special Methods** – learn how to customize your objects with `__str__`, `__repr__`, `__eq__`, and more.
