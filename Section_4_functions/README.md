# 📦 Section 4: Functions

🧩 **Learn how to define and use functions in Python — reusable blocks of code that help you organize and simplify your programs.**



## 🧠 What is a Function?

A function is a **named block of code** that performs a specific task or returns a value.

### 🔹 **Why Use Functions?**
- Reuse code without repeating yourself.
- Break complex tasks into smaller, manageable parts.
- Improve readability and maintainability.

### 🔹 **Example:**
```python
def greet():
    print("Hello, World!")

greet()
```


## 📌 Defining a Function

Use the `def` keyword followed by the function name and parentheses.

### 🔹 **Syntax:**
```python
def function_name(parameters):
    # function body
    return value
```

### 🔹 **Example:**
```python
def greet(name):
    return f"Hi, {name}!"

print(greet("Alice"))  # Output: Hi, Alice!
```


## 🔄 Calling a Function

To execute a function, simply write its name followed by parentheses and any required arguments.

### 🔹 **Example:**
```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```



## 🎯 Default Parameters

You can assign default values to function parameters.

### 🔹 **Example:**
```python
def greet(name, message='Hi'):
    return f"{message}, {name}!"

print(greet("John"))              # Output: Hi, John!
print(greet("John", "Hello"))     # Output: Hello, John!
```

🔸 **Important:** Parameters with default values must come **after** those without defaults.



## 📝 Keyword Arguments

Pass arguments using parameter names for clarity and flexibility.

### 🔹 **Example:**
```python
def get_net_price(price, discount=0.1, tax_rate=0.07):
    discounted_price = price * (1 - discount)
    return discounted_price * (1 + tax_rate)

print(get_net_price(price=100, discount=0.06))  # Output: 100.58
```

🔸 You can mix positional and keyword arguments, but **keyword arguments must come after positional ones**.



## 🔁 Recursive Functions

A function that calls itself is called a **recursive function**.

### 🔹 **Example – Countdown:**
```python
def count_down(start):
    if start <= 0:
        print(0)
        return
    print(start)
    count_down(start - 1)

count_down(5)
# Output:
# 5
# 4
# 3
# 2
# 1
# 0
```

### 🔸 Make sure there's a base case to avoid infinite recursion!



## 🧊 Lambda Expressions

Create small **anonymous functions** using the `lambda` keyword.

### 🔹 **Syntax:**
```python
lambda arguments: expression
```

### 🔹 **Example:**
```python
double = lambda x: x * 2
print(double(5))  # Output: 10
```

### 🔸 **Use Cases:**
- Short functions passed as arguments (e.g., in `map()`, `filter()`).
- Quick inline operations.

### 🔹 **Lambda with Higher-order Functions:**
```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
```



## 📄 Docstrings – Document Your Functions

Use docstrings to explain what your function does, its parameters, and return values.

### 🔹 **Example:**
```python
def add(a, b):
    """
    Add two numbers and return the result.

    Parameters:
    a (int): First number
    b (int): Second number

    Returns:
    int: Sum of a and b
    """
    return a + b
```

### 🔹 **Access Documentation:**
```python
help(add)
print(add.__doc__)
```

#### 🔸 Follow PEP 257 conventions for clean, readable documentation.



## 🪟 `pass` Statement – Placeholder for Future Code

Use `pass` when you want to define a function but implement it later.

### 🔹 **Example:**
```python
def todo_later():
    pass  # To be implemented later
```


🎉 You now have a solid understanding of **Python Functions**!

Next up: 📋 **Section 5: Lists** – learn how to store and manipulate collections of data.