# 📦 Section 10: More on Python Functions

🧩 **Dive deeper into advanced function features in Python**, including tuple unpacking, variable-length arguments (`*args`, `**kwargs`), partial functions, and type hints.

This section builds upon the basics of Python functions and introduces powerful tools that make your code more flexible, expressive, and maintainable.



## 🧠 What You'll Learn

- 🔁 How to unpack tuples into multiple variables
- 📥 Use `*args` to accept a variable number of positional arguments
- 📎 Use `**kwargs` for variable keyword arguments
- 🛠️ Define **partial functions** using `functools.partial`
- 🧮 Add **type hints** to improve code clarity and enable static analysis
- 💡 Hidden tips, best practices, and common pitfalls to avoid



## 📥 Tuple Unpacking

Tuple unpacking allows you to assign individual elements of a tuple to multiple variables.

🔹 **Basic Example:**
```python
x, y = 10, 20
print(x)  # Output: 10
print(y)  # Output: 20
```

🔹 **Unpacking with Remaining Elements:**
Use `*` to capture extra values into a list:
```python
x, y, *z = 10, 20, 30, 40
print(z)  # Output: [30, 40]
```

🔹 **Real-world Use Case – Function Return Values:**
```python
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
```

🔸 **Note:** The number of variables must match the number of elements unless using `*`.



## 📥 Variable-Length Arguments: `*args`

Use `*args` to pass a **variable number of positional arguments** to a function.

🔹 **Syntax:**
```python
def add(x, y, *args):
    total = x + y
    for num in args:
        total += num
    return total
```

🔹 **Example:**
```python
result = add(10, 20, 30, 40)
print(result)  # Output: 100
```

🔸 Inside the function, `args` is a **tuple** of extra arguments.

### ⚠️ Best Practices:
- Place `*args` after required parameters.
- Avoid mixing `*args` with too many positional arguments.
- Don’t use `*args` if you expect a fixed number of arguments.



## 📎 Keyword Arguments: `**kwargs`

Use `**kwargs` to pass a **variable number of keyword arguments** to a function.

🔹 **Syntax:**
```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

🔹 **Example:**
```python
display_info(name="Alice", age=30, city="New York")
```

🔸 Inside the function, `kwargs` is a **dictionary** of keyword arguments.

### ✅ Use Cases:
- Configurable settings or options
- Passing arguments through layers of functions
- Building generic wrappers/decorators


## 🔄 Combining `*args` and `**kwargs`

You can combine both to create highly flexible functions.

🔹 **Example:**
```python
def demo_function(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

demo_function(1, 2, 3, 4, name="Alice", role="Developer")
```

🔹 **Output:**
```
a: 1
b: 2
args: (3, 4)
kwargs: {'name': 'Alice', 'role': 'Developer'}
```

🔸 This pattern is especially useful when writing **decorators**, **wrappers**, or **generic utility functions**.



## 🧱 Partial Functions with `functools.partial`

Use `functools.partial` to **fix some arguments** of a function and create a new function with fewer parameters.

🔹 **Example – Fixing One Argument:**
```python
from functools import partial

def multiply(x, y):
    return x * y

double = partial(multiply, x=2)
print(double(y=5))  # Output: 10
```

🔹 **Example – Fixing Multiple Args:**
```python
power_of_2 = partial(pow, 2)
print(power_of_2(5))  # Output: 32
```

🔸 **Why Use Partial Functions?**
- Reduce boilerplate by fixing commonly used values
- Improve readability and reusability
- Create specialized versions of general-purpose functions



## 🧐 Type Hints

Type hints help developers write clearer code and allow tools like `mypy` to perform **static type checking** — catching bugs before runtime!

🔹 **Basic Type Annotations:**
```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

🔹 **Function with Multiple Types:**
```python
from typing import Union

def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y
```

🔹 **Using Literal Types (Python 3.8+):**
```python
from typing import Literal

def set_mode(mode: Literal["read", "write"]) -> None:
    print(f"Setting mode to {mode}")

set_mode("read")   # OK
set_mode("execute") # mypy error
```

🔸 **Static Type Checking with `mypy`:**
Install `mypy`:
```bash
pip install mypy
```

Run it:
```bash
mypy app.py
```

🔹 **Benefits:**
- Improved code readability
- Better IDE support (autocompletion, warnings)
- Early detection of bugs
- Easier refactoring and debugging



## 🧪 Real-World Examples

### ✅ Using `*args` for Logging:
```python
def log(*values):
    print("Log:", values)

log("User login", "success", "IP: 192.168.1.1")
# Output: Log: ('User login', 'success', 'IP: 192.168.1.1')
```

### ✅ Using `**kwargs` for Configuration:
```python
def configure(**options):
    for key, value in options.items():
        print(f"Setting {key} = {value}")

configure(theme="dark", autosave=True)
```

### ✅ Partial Functions for Reusable Utilities:
```python
from functools import partial

def format_message(prefix, suffix, text):
    return f"{prefix} {text} {suffix}"

alert = partial(format_message, prefix="[ALERT]", suffix="!")
print(alert(text="System Overload"))  
# Output: [ALERT] System Overload !
```



## 🧠 Hidden Details & Notes

- 🔁 **Order Matters:** In function definitions, `*args` must come before `**kwargs`.
- ❌ No Extra Positional Args After `*args`: Once you use `*args`, all following arguments must be keyword-only.
  ```python
  def func(*args, z): ...
  ```
  Must be called as:
  ```python
  func(1, 2, z=3)
  ```
- 📦 `*args` is not a magic syntax — it's just a convention. But always use `*args` and `**kwargs` for consistency.
- 📝 Type hints are **optional** but highly encouraged in larger projects.
- 🧩 You can annotate return types even if inputs don't have them:
  ```python
  def parse_data(data) -> dict:
      return json.loads(data)
  ```
- 🔍 Use `Final` from `typing` for constants:
  ```python
  from typing import Final

  PI: Final[float] = 3.14159
  ```



## 🧪 Try It Yourself

### ✅ Example – Flexible Data Formatter:

```python
from functools import partial

def format_line(separator, *parts):
    return separator.join(parts)

dash_line = partial(format_line, "-")
print(dash_line("Header", "Body", "Footer"))  
# Output: Header-Body-Footer
```



🎉 Congratulations! You now have a solid understanding of **advanced Python functions**, including how to use tuple unpacking, handle variable arguments, define partial functions, and apply type hints for better code quality.

Next up: 📁 **Section 11: Modules & Packages** – learn how to organize your code into reusable modules and packages.
