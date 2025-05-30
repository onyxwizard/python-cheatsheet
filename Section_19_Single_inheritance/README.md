# 🔄 Section 19: Single Inheritance  
## Reuse Code with Python Inheritance

🧩 **Learn how to reuse code from one class in another using single inheritance**, a powerful object-oriented programming feature that promotes code reusability, modularity, and clean design.

This section will guide you through:
- 🧱 The basics of inheritance in Python
- 🔁 Method overriding to customize child behavior
- 🚶 Using `super()` to call parent class methods
- 🧱 Using `__slots__` in inherited classes for memory efficiency
- 🧻 Creating abstract base classes for interface design
- 💡 Hidden notes and best practices for writing clean, maintainable class hierarchies


## 🧠 What You'll Learn

| Concept | Description |
|--------|-------------|
| **Inheritance** | A mechanism where a class inherits attributes and methods from another class |
| **Base Class (Parent)** | The class being inherited from |
| **Derived Class (Child)** | The class that inherits from the parent |
| **Method Overriding** | Redefine a method in the child class |
| **`super()`** | Call parent class’s implementation |
| **`__slots__`** | Improve memory usage by restricting allowed attributes |
| **Abstract Base Class** | Define an interface or enforce method implementation |



## 🧱 Introduction to Inheritance

Inheritance allows a class to inherit properties and behaviors from another class — enabling code reuse and hierarchical relationships.

🔹 **Example – Parent and Child Class**
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

dog = Dog("Buddy")
dog.speak()  # Output: Animal speaks
```

🔸 The `Dog` class inherits all methods and attributes from `Animal`.



## 🔁 Method Overriding

Override methods in the child class to change their behavior.

🔹 **Example – Customizing `speak()`**
```python
class Cat(Animal):
    def speak(self):
        print("Meow!")

cat = Cat("Whiskers")
cat.speak()  # Output: Meow!
```

🔸 This is known as **polymorphism** — the same method behaves differently in different subclasses.



## 🚶 Using `super()` to Access Parent Methods

Use `super()` to delegate work to the parent class without duplicating logic.

🔹 **Example – Extending parent initialization**
```python
class Employee(Animal):
    def __init__(self, name, role):
        super().__init__(name)  # Call parent's __init__
        self.role = role

    def speak(self):
        super().speak()
        print(f"{self.name} says: I'm working as {self.role}")

emp = Employee("Alice", "Developer")
emp.speak()
# Output:
# Animal speaks
# Alice says: I'm working as Developer
```

🔸 `super()` ensures you're calling the parent version safely and clearly.



## 🧰 Real-World Example – Document Parser System

Let’s build a parser system using inheritance to extract email and phone numbers from text.

### 🧱 Base Class – `TextParser`
```python
import re

class TextParser:
    def __init__(self, content):
        self.content = content

    def extract_email(self):
        match = re.search(r'[a-z0-9._%+-]+@[a-z0-2._%+-]+\.[a-z]+', self.content)
        return match.group(0) if match else None

    def extract_phone(self):
        match = re.search(r'\d{3}-\d{3}-\d{4}', self.content)
        return match.group(0) if match else None
```

### 🐶 Derived Class – `ResumeParser`
```python
class ResumeParser(TextParser):
    def extract_experience(self):
        years_match = re.search(r'Experience:\s*(\d+)\s*years', self.content)
        return int(years_match.group(1)) if years_match else 0
```

🔹 **Usage:**
```python
sample_resume = """
Contact: john.doe@example.com
Phone: 555-123-4567
Experience: 5 years
"""

parser = ResumeParser(sample_resume)
print(parser.extract_email())         # john.doe@example.com
print(parser.extract_phone())         # 555-123-4567
print(parser.extract_experience())    # 5
```



## 🧱 Use `__slots__` for Memory Efficiency

Use `__slots__` to reduce memory usage and prevent accidental attribute creation.

🔹 **Example – 2D and 3D Point Classes**
```python
class Point2D:
    __slots__ = ('x', 'y')
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point2D):
    __slots__ = ('z',)
    
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
```

🔸 Benefits:
- Faster attribute access
- Reduced memory footprint
- Prevents accidental attribute creation (`point.new_attr = 10` raises error)



## 🧻 Abstract Base Classes – Enforce Interface Design

Use `abc.ABC` and `@abstractmethod` to define abstract base classes that cannot be instantiated directly and require implementation in child classes.

🔹 **Example – Payment Processor Interface**
```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} via credit card...")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} via PayPal...")
```

🔹 **Instantiation Attempt Raises Error**
```python
processor = PaymentProcessor()  # ❌ TypeError: Can't instantiate abstract class
```

🔸 Forces developers to implement required methods before creating objects.


## 📌 Key Concepts Summary

| Feature | Description |
|--------|-------------|
| **Inheritance** | Child class reuses attributes/methods from parent |
| **Method Overriding** | Modify behavior of parent methods in child class |
| **`super()`** | Call parent class methods or constructor |
| **`__slots__`** | Reduce memory usage and restrict allowed attributes |
| **Abstract Base Class** | Define interfaces and enforce implementation |
| **Polymorphism** | Same method name behaves differently across classes |



## 💡 Hidden Tips & Notes

- 🧩 Always use `super()` when extending `__init__` — avoids repetition and keeps your hierarchy flexible.
- 🧱 Avoid deep inheritance chains; prefer shallow, meaningful hierarchies.
- 📦 Use `issubclass()` and `isinstance()` to check class relationships.
- 🧾 If you override a method, ensure it maintains the same signature unless necessary.
- 🧵 Prefer composition over inheritance when possible — but inheritance is still valuable for modeling real-world relationships.
- 🧠 Use `__slots__` in performance-critical applications or large-scale systems.
- 🧪 Never instantiate abstract base classes — they’re meant to be extended.



## 🧪 Advanced Example – Shape Renderer System

Build a shape renderer using inheritance and method overriding:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle 🟢")

class Square(Shape):
    def draw(self):
        print("Drawing a square ⬛")

class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle 🔺")

shapes = [Circle(), Square(), Triangle()]
for shape in shapes:
    shape.draw()
```

🔹 **Output:**
```
Drawing a circle 🟢
Drawing a square ⬛
Drawing a triangle 🔺
```


🎉 Congratulations! You now understand how to effectively use **single inheritance** in Python to create modular, reusable, and maintainable class hierarchies.

Next up: 🧬 **Section 20: Multiple Inheritance** – learn how to inherit from multiple parent classes and understand method resolution order (MRO).
