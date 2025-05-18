
# 🐍 Python Fundamentals Cheatsheet

A quick reference guide to basic Python syntax, data types, and operations.



## 🔤 Variables & Assignment
- **Syntax:** `variable_name = value`
- **What it does:** Stores a value (number, string, etc.) in a variable.
- **Example:**
  ```python
  name = "Alice"
  age = 25
  ```



## 📚 Naming Rules for Variables
- **What it does:** Helps avoid errors by following valid naming conventions.
- **Rules:**
  - Start with a letter or underscore `_`.
  - Can contain letters, numbers, and underscores.
  - Cannot use Python keywords.
- **Examples:**
  ```python
  user_name = "Bob"     # Valid
  _private = True       # Valid
  2nd_place = 99        # ❌ Invalid (starts with number)
  ```


## 🧮 Basic Operators
### ➕ Addition
- **Syntax:** `a + b`
- **Example:**
  ```python
  print(5 + 3)  # Output: 8
  ```

### ➖ Subtraction
- **Syntax:** `a - b`
- **Example:**
  ```python
  print(10 - 4)  # Output: 6
  ```

### ✖️ Multiplication
- **Syntax:** `a * b`
- **Example:**
  ```python
  print(6 * 7)  # Output: 42
  ```

### ➗ Division (float)
- **Syntax:** `a / b`
- **Example:**
  ```python
  print(10 / 3)  # Output: 3.333...
  ```

### 🟰 Integer Division
- **Syntax:** `a // b`
- **Example:**
  ```python
  print(10 // 3)  # Output: 3
  ```

### 💥 Exponentiation
- **Syntax:** `a ** b`
- **Example:**
  ```python
  print(2 ** 5)  # Output: 32
  ```

### 🧮 Modulus
- **Syntax:** `a % b`
- **Example:**
  ```python
  print(10 % 3)  # Output: 1
  ```



## 📄 Strings
### Single/Double Quotes
- **What it does:** Defines a string. Use one or the other unless escaping is needed.
- **Example:**
  ```python
  s1 = 'Hello'
  s2 = "World"
  ```

### Triple Quotes for Multiline
- **Syntax:** `'''...'''` or `"""..."""`
- **Example:**
  ```python
  message = '''This is a
  multiline string.'''
  ```

### 🧵 String Concatenation
- **Syntax:** `str1 + str2`
- **Example:**
  ```python
  greeting = "Hello" + ", " + "World!"
  print(greeting)  # Output: Hello, World!
  ```

### 🔢 String Repetition
- **Syntax:** `str * n`
- **Example:**
  ```python
  line = "-" * 20
  print(line)  # Output: --------------------
  ```

### 📍 Accessing Characters
- **Syntax:** `string[index]`
- **Example:**
  ```python
  word = "Python"
  print(word[0])   # Output: P
  print(word[-1])  # Output: n
  ```

### 🧃 Slicing Strings
- **Syntax:** `string[start:end]`
- **Example:**
  ```python
  text = "Fundamental"
  print(text[3:6])  # Output: dam
  ```

### 📏 Length of String
- **Syntax:** `len(string)`
- **Example:**
  ```python
  print(len("Hello"))  # Output: 5
  ```

### 🧼 Raw Strings
- **Syntax:** `r"raw string"`
- **Example:**
  ```python
  path = r'C:\Users\Name'
  print(path)  # Output: C:\Users\Name
  ```

### 🎯 F-Strings (Formatted Strings)
- **Syntax:** `f"{variable}"`
- **Example:**
  ```python
  name = "Alice"
  print(f"Hello, {name}!")  # Output: Hello, Alice!
  ```



## 🔢 Numbers
### Integers
- **Example:**
  ```python
  x = 100
  y = -25
  ```

### Floats
- **Example:**
  ```python
  pi = 3.14
  temp = -2.5
  ```

### Underscores in Large Numbers
- **What it does:** Improves readability without affecting value.
- **Example:**
  ```python
  population = 10_000_000
  print(population)  # Output: 10000000
  ```



## 🔁 Booleans
- **Values:** `True`, `False`
- **Used in comparisons:**
  ```python
  print(5 > 3)        # Output: True
  print(10 == 9)      # Output: False
  ```



## 🧷 Constants
- **Convention:** Use uppercase variable names.
- **Example:**
  ```python
  MAX_USERS = 100
  print(MAX_USERS)
  ```


## 📝 Comments
### Single-line Comment
- **Syntax:** `# comment`
- **Example:**
  ```python
  # This is a comment
  print("Hello")
  ```

### Inline Comment
- **Example:**
  ```python
  print("World")  # Greeting
  ```

### Multi-line Comment (Docstrings)
- **Syntax:** `"""comment"""` or `'''comment'''`
- **Example:**
  ```python
  """
  This is a multi-line
  comment used as a docstring.
  """
  def greet():
      """Prints a greeting."""
      print("Hi")
  ```



## 🔁 Type Conversion
### To Integer
- **Syntax:** `int(value)`
- **Example:**
  ```python
  num = int("123")
  print(num + 10)  # Output: 133
  ```

### To Float
- **Syntax:** `float(value)`
- **Example:**
  ```python
  price = float("19.99")
  print(price)  # Output: 19.99
  ```

### To String
- **Syntax:** `str(value)`
- **Example:**
  ```python
  age = str(25)
  print("Age: " + age)  # Output: Age: 25
  ```

### To Boolean
- **Syntax:** `bool(value)`
- **Example:**
  ```python
  print(bool(0))         # Output: False
  print(bool("Hello"))   # Output: True
  ```



## 🧐 Get Type of Value
- **Syntax:** `type(value)`
- **Example:**
  ```python
  print(type(100))        # <class 'int'>
  print(type("Hello"))    # <class 'str'>
  print(type(True))       # <class 'bool'>
  ```



## 📦 Keywords (Reserved Words)
- **What it does:** These words have special meaning and cannot be used as identifiers.
- **Example:**
  ```python
  import keyword
  print(keyword.kwlist)
  ```
  Output:
  ```
  ['False', 'None', 'True', 'and', 'as', 'assert',
   'break', 'class', 'continue', 'def', 'del',
   'elif', 'else', 'except', 'finally', 'for',
   'from', 'global', 'if', 'import', 'in',
   'is', 'lambda', 'nonlocal', 'not', 'or',
   'pass', 'raise', 'return', 'try', 'while',
   'with', 'yield']
  ```



## 📁 File Handling (Basic Read)
- **Syntax:**
  ```python
  with open("file.txt", "r") as file:
      content = file.read()
  ```
