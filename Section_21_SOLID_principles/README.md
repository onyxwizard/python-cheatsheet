# 🧱 Section 21: SOLID Principles  
## Writing Maintainable and Scalable Python Classes

🛠️ **Learn how to apply the SOLID principles in Python** — five fundamental object-oriented design principles that help you write clean, flexible, and maintainable code.

These principles are:
- ✅ **S**ingle Responsibility Principle (SRP)
- ✅ **O**pen/Closed Principle (OCP)
- ✅ **L**iskov Substitution Principle (LSP)
- ✅ **I**nterface Segregation Principle (ISP)
- ✅ **D**ependency Inversion Principle (DIP)

This README gives you a clear understanding of each principle with **custom examples**, so you can **apply them effectively in your Python projects** without relying on theoretical or abstract code.



## 🧠 What You'll Learn

| Principle | Description |
|----------|-------------|
| **Single Responsibility Principle (SRP)** | A class should have only one reason to change |
| **Open/Closed Principle (OCP)** | Open for extension, closed for modification |
| **Liskov Substitution Principle (LSP)** | Child classes must be substitutable for their parent |
| **Interface Segregation Principle (ISP)** | Clients shouldn’t depend on interfaces they don’t use |
| **Dependency Inversion Principle (DIP)** | Depend on abstractions, not concretions |



## ✅ S – Single Responsibility Principle (SRP)

A class should have only **one job or responsibility**. This makes it easier to understand, test, and extend.

🔹 **Violation Example – One class doing too much**
```python
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def format_as_text(self):
        return f"Title: {self.title}\nContent: {self.content}"

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(self.format_as_text())
```

🔸 This class does both formatting and file handling — two responsibilities!



🔹 **Refactored – Separated Concerns**
```python
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def format(self):
        return f"Title: {self.title}\nContent: {self.content}"

class FileReporter:
    def save(self, report, filename):
        with open(filename, 'w') as f:
            f.write(report.format())
```

🔸 Now `Report` handles data, and `FileReporter` handles persistence.



## 📦 O – Open/Closed Principle (OCP)

Software entities (classes, modules, functions) should be **open for extension but closed for modification**.

🔹 **Violation Example – Hardcoded logic**
```python
class InvoicePrinter:
    def print_invoice(self, invoice_type):
        if invoice_type == "PDF":
            print("Printing PDF invoice")
        elif invoice_type == "HTML":
            print("Printing HTML invoice")
```

🔸 Every new invoice type requires modifying this class — violates OCP.



🔹 **Refactored – Extend Without Modifying**
```python
from abc import ABC, abstractmethod

class Invoice(ABC):
    @abstractmethod
    def print(self):
        pass

class PdfInvoice(Invoice):
    def print(self):
        print("Printing PDF invoice")

class HtmlInvoice(Invoice):
    def print(self):
        print("Printing HTML invoice")

class InvoicePrinter:
    def print(self, invoice: Invoice):
        invoice.print()
```

🔸 Now you can add new invoice types without changing existing code.


## 🔄 L – Liskov Substitution Principle (LSP)

Child classes should behave in a way that allows them to substitute the parent class without breaking logic.

🔹 **Violation Example – Invalid substitution**
```python
class Rectangle:
    def set_width(self, width): ...
    def set_height(self, height): ...

class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

def use_rect(r):
    r.set_width(5)
    r.set_height(10)
    assert r.width == 5 and r.height == 10

rect = Rectangle()
use_rect(rect)  # Works fine

square = Square()
use_rect(square)  # ❌ Fails! Height changes width unexpectedly
```

🔸 The `Square` behaves differently than `Rectangle`, which breaks expectations.



🔹 **Refactored – Use a Common Base Class**
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```

🔸 Both `Rectangle` and `Square` inherit from `Shape` and implement `area()` independently — now they’re interchangeable.



## 🧩 I – Interface Segregation Principle (ISP)

Clients shouldn’t be forced to depend on methods they don’t use. Create **small, focused interfaces** instead of large ones.

🔹 **Violation Example – Too many methods**
```python
from abc import ABC, abstractmethod

class MultiFunctionPrinter(ABC):
    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def scan(self):
        pass

class OldPrinter(MultiFunctionPrinter):
    def print(self):
        print("Printing document")

    def scan(self):
        raise NotImplementedError("Old printer can't scan")
```

🔸 `OldPrinter` is forced to implement `scan()`, even though it doesn't support scanning.



🔹 **Refactored – Split into Smaller Interfaces**
```python
class Printer(ABC):
    @abstractmethod
    def print(self):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass

class SimplePrinter(Printer):
    def print(self):
        print("Simple printer printing...")

class AdvancedPrinter(Printer, Scanner):
    def print(self):
        print("Advanced printer printing...")

    def scan(self):
        print("Advanced printer scanning...")
```

🔸 Now, clients only need to depend on what they actually use.



## 🧱 D – Dependency Inversion Principle (DIP)

High-level modules should not depend on low-level modules. Both should depend on **abstractions** (interfaces or abstract base classes).

🔹 **Violation Example – Tight coupling**
```python
class EmailService:
    def send_email(self, message):
        print(f"Sending email: {message}")

class Notification:
    def __init__(self):
        self.email = EmailService()

    def notify(self, msg):
        self.email.send_email(msg)
```

🔸 `Notification` depends directly on `EmailService` — hard to swap out later.



🔹 **Refactored – Depend on Abstraction**
```python
from abc import ABC, abstractmethod

class MessageService(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailService(MessageService):
    def send(self, message):
        print(f"Sending email: {message}")

class SMSService(MessageService):
    def send(self, message):
        print(f"Sending SMS: {message}")

class Notifier:
    def __init__(self, service: MessageService):
        self.service = service

    def notify(self, message):
        self.service.send(message)
```

🔸 Now you can easily switch between different services without modifying `Notifier`.



## 🛠️ Real-World Example – Payment Gateway System

Let’s build a payment system applying all five SOLID principles.

### ✅ SRP – Separate concerns
```python
class Order:
    def __init__(self):
        self.items = []
        self.status = "open"

    def add_item(self, item):
        self.items.append(item)

class PaymentProcessor:
    def pay(self, order):
        order.status = "paid"
```

### 📦 OCP – Add new payment types without modifying core
```python
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass

class CreditCardPayment(PaymentProcessor):
    def pay(self, order):
        print("Paid by credit card")
        order.status = "paid"

class PayPalPayment(PaymentProcessor):
    def pay(self, order):
        print("Paid by PayPal")
        order.status = "paid"
```

### 🔄 LSP – Substitutable implementations
```python
class PaymentSystem(ABC):
    def process(self, order):
        pass

class OnlinePayment(PaymentSystem):
    def process(self, order):
        print("Processing online payment...")
        order.status = "paid"

class OfflinePayment(PaymentSystem):
    def process(self, order):
        print("Processing offline payment...")
        order.status = "paid"
```

### 🧩 ISP – Only relevant interfaces
```python
class Payable(ABC):
    @abstractmethod
    def pay(self, order):
        pass

class Refundable(ABC):
    @abstractmethod
    def refund(self, order):
        pass

class CashOnDelivery(Payable):
    def pay(self, order):
        print("Payment on delivery")
        order.status = "paid"
```

### 🧱 DIP – Depend on abstraction, not implementation
```python
class OrderProcessor:
    def __init__(self, payment_method: Payable):
        self.payment_method = payment_method

    def process_order(self, order):
        self.payment_method.pay(order)
```



## 💡 Hidden Tips & Notes

- 🧩 Apply **SOLID** principles gradually — not every project needs all at once.
- 📁 Keep related responsibilities together, and separate unrelated ones.
- 🧱 Prefer **abstract base classes** (`ABC`) when designing extensible systems.
- 🔁 Design with **inheritance in mind** — always follow Liskov's rule.
- 📦 Use **interface segregation** to avoid bloated dependencies.
- 🧾 Favor **composition over inheritance** where possible.
- 🧰 Use dependency injection to enable flexibility and testing.
- 🧪 SOLID improves **testability**, **maintainability**, and **extensibility** of your code.



## 📌 Summary

| Principle | Purpose |
|----------|---------|
| **Single Responsibility Principle** | One class, one job |
| **Open/Closed Principle** | Extend behavior without modifying code |
| **Liskov Substitution Principle** | Child classes should work like parents |
| **Interface Segregation Principle** | Define small, client-specific interfaces |
| **Dependency Inversion Principle** | Depend on abstractions, not concrete classes |



🎉 Congratulations! You now understand how to apply **SOLID Principles** in Python to create software that is:
- ✅ Easy to maintain
- ✅ Flexible to extend
- ✅ Robust against bugs

Next up: 🧬 **Section 22: Multiple Inheritance** – learn how to inherit from multiple parent classes and understand Python’s Method Resolution Order (MRO).