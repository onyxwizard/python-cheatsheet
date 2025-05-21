# 📁 Section 11: Modules & Packages

🧩 **Learn how to organize and reuse Python code using modules and packages — essential tools for building scalable, maintainable applications.**

This section explains how to:
- Break your program into multiple files (modules)
- Organize modules into packages
- Use `import` effectively
- Understand the module search path
- Control script vs module behavior using `__name__`
- Create private functions in modules
- Work with subpackages and nested imports


## 🧠 What is a Module?

A **module** is a `.py` file that contains reusable Python code — such as functions, classes, or variables.

🔹 **Why use modules?**
- Reuse code across multiple programs.
- Keep your codebase organized.
- Improve readability and maintainability.
- Share functionality across teams.

🔹 **Example: pricing.py**
```python
# pricing.py
def get_net_price(price, tax_rate, discount=0):
    discounted_price = price * (1 - discount)
    return discounted_price * (1 + tax_rate)

def get_tax(price, tax_rate=0):
    return price * tax_rate
```

🔹 **Using the Module in Another File:**
```python
# main.py
import pricing

net_price = pricing.get_net_price(100, 0.1)
print(f"Net Price: {net_price}")
```



## 📦 How to Import Modules

There are several ways to import modules depending on what you need:

### ✅ Basic Import
```python
import module_name
```

### ✅ Import with Alias
```python
import module_name as alias
```

### ✅ Import Specific Objects
```python
from module import function, variable
```

### ✅ Import All (Not Recommended)
```python
from module import *
```

🔸 **Best Practices:**
- Avoid `import *` — it pollutes the namespace and can cause conflicts.
- Use explicit imports like `from module import function` for clarity.
- Use aliases when importing long/namespaced modules:
  ```python
  import very_long_module_name as mod
  ```


## 🔍 Module Search Path

When you import a module, Python searches for it in the following order:
1. The current directory.
2. Directories listed in the `PYTHONPATH` environment variable.
3. Installation-dependent standard library paths.

🔹 You can view the search path with:
```python
import sys
for path in sys.path:
    print(path)
```

🔸 **Modifying the Path at Runtime:**
```python
sys.path.append('/path/to/your/module')
```

⚠️ This change is temporary and only affects the current session.



## 🚫 Private Functions in Modules

Python doesn’t have true private functions, but there are conventions and techniques to simulate privacy.

### 🎯 Using `_` Prefix
Prefix a function name with an underscore `_` to indicate it's intended as private.

🔹 Example:
```python
# mail.py
def send(email, message):
    print(f'Sending "{message}" to {email}')

def _attach_file(filename):
    print(f'Attach {filename} to message')
```

🔸 Now, `send()` is public; `_attach_file()` signals internal use.

### 📦 Using `__all__` List
Define `__all__` in your module to specify which names should be exported by `import *`.

🔹 Example:
```python
# mail.py
__all__ = ['send']

def send(email, message):
    ...

def attach_file(filename):
    ...
```

🔸 With this setup, `from mail import *` will only expose `send()`.



## 🧱 Understanding `__name__` and `__main__`

Every Python module has a built-in variable called `__name__`. It tells you whether the module is being run directly or imported.

🔹 **Use Case – Run Code Only When Script is Executed:**
```python
# hello.py
def greet():
    print("Hello from Hello module!")

if __name__ == "__main__":
    greet()
```

🔸 Behavior:
- If run directly: `python hello.py` → "Hello from Hello module!"
- If imported: `import hello` → no output

💡 This pattern is widely used in testable modules and CLI scripts.



## 📁 What is a Package?

A **package** is a way to organize related modules into a directory hierarchy.

🔹 To create a package:
- Make a folder
- Add an `__init__.py` file (can be empty)
- Place your module files inside

📁 Folder structure:
```
sales/
├── __init__.py
├── order.py
├── delivery.py
└── billing.py
```

🔹 Importing from a Package:
```python
import sales.order
from sales.billing import generate_invoice
```

🔸 You can also rename imports:
```python
from sales.delivery import ship_order as start_shipping
```



## 🧰 Initializing a Package with `__init__.py`

The `__init__.py` file makes Python treat a directory as a package.

🔹 You can define:
- Default variables
- Auto-import modules
- Define `__all__` for wildcard imports

🔹 Example:
```python
# sales/__init__.py
TAX_RATE = 0.07

from .order import place_order
from .delivery import schedule_delivery
```

🔸 Now, these are available directly from the package:
```python
import sales
sales.place_order(...)
```



## 📦 Subpackages

Packages can contain **subpackages**, allowing deeper levels of organization.

📁 Example:
```
sales/
├── __init__.py
├── order/
│   ├── __init__.py
│   └── process.py
├── delivery/
│   ├── __init__.py
│   └── logistics.py
```

🔹 Importing from subpackages:
```python
from sales.order.process import new_order
```

🔸 Just like top-level packages, subpackages can also have their own `__init__.py` files for initialization logic.



## 📦 Controlling Exports with `__all__` in Packages

You can control what gets exposed when someone uses `from package import *`.

🔹 Example:
```python
# sales/__init__.py
__all__ = ['order', 'delivery']
```

Now only `order` and `delivery` will be available via:
```python
from sales import *
```



## 📦 Creating Reusable Libraries

Modules and packages help you build modular, reusable codebases.

🔹 **Benefits:**
- Reusability: write once, use everywhere.
- Maintainability: isolate changes to one file.
- Readability: group related functionality together.
- Scalability: manage large projects more easily.

🔹 **Best Practices:**
- Group related modules into packages.
- Keep each module focused on one task.
- Use descriptive naming.
- Document each module and function.



## 🛠️ Real-World Examples

### 📦 Example 1: Sales Tax Calculator

📁 Structure:
```
pricing/
├── __init__.py
├── tax.py
└── discount.py
```

🔹 `tax.py`:
```python
def calculate_tax(amount, rate):
    return amount * rate
```

🔹 `discount.py`:
```python
def apply_discount(amount, percent):
    return amount * (1 - percent / 100)
```

🔹 Usage:
```python
from pricing.tax import calculate_tax
from pricing.discount import apply_discount

price = apply_discount(100, 10)  # $90
tax = calculate_tax(price, 0.10)  # $9.00
```



## 🧠 Hidden Tips & Notes

- 🧩 A module can be both executable and importable — use the `if __name__ == '__main__':` idiom.
- 📁 Starting with Python 3.3+, you can have **namespace packages** without `__init__.py`.
- 🧵 Avoid deep nesting — keep your package structure shallow and logical.
- 🔒 Use `_` prefix or `__all__` to make functions "private".
- 🔄 Use relative imports within packages (`from . import module`) for better portability.
- 📂 Always include `__init__.py` unless you're intentionally creating a namespace package.
- 🧹 Don't abuse `import *` — it reduces clarity and increases bugs.


## 📌 Summary

| Concept | Description |
|--------|-------------|
| **Module** | A single `.py` file containing Python definitions |
| **Package** | A folder containing modules and an `__init__.py` |
| **Import Statement** | `import module`, `from module import function`, etc. |
| **Search Path** | Where Python looks for modules — controlled by `sys.path` |
| **`__name__ == '__main__'** | Check if file is run directly or imported |
| **Private Functions** | Use `_function` or `__all__` to hide internals |
| **Subpackages** | Nested packages for organizing larger applications |



🎉 Congratulations! You now understand how to **organize your Python code into modules and packages**, **control visibility**, and **create reusable libraries**.

Next up: 📄 **Section 12: Working with Files** – learn how to read from and write to files, work with CSV data, and interact with your filesystem.
