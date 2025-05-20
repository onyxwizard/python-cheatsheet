# ⚠️ Section 8: Exception Handling

🛡️ **Learn how to handle exceptions gracefully in Python and prevent your programs from crashing due to unexpected errors.**

Python uses a robust exception handling mechanism that allows you to catch and manage runtime errors, making your applications more resilient and user-friendly.



## 🧠 What is an Exception?

An **exception** is an event that occurs during the execution of a program that disrupts the normal flow of instructions.

Exceptions can occur due to:
- Invalid user input
- File not found
- Division by zero
- Network or database issues
- Any unexpected condition

Unlike **syntax errors**, which are caught before execution, **exceptions happen at runtime**.



## 🛑 Syntax Errors vs Exceptions

### 🔤 Syntax Error
Occurs when Python cannot parse the code correctly.
```python
if True
    print("Hello")
```
🔹 Output:
```
SyntaxError: expected ':'
```

### 💥 Runtime Exception
Occurs during execution:
```python
x = 10 / 0
```
🔹 Output:
```
ZeroDivisionError: division by zero
```



## 🧱 The `try...except` Statement

Use `try...except` to catch and handle exceptions gracefully.

🔹 **Basic Syntax:**
```python
try:
    # code that may cause an exception
except ExceptionType:
    # code to handle the exception
```

### ✅ Example – Handle Division by Zero:
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### ✅ Example – Handle Invalid Input:
```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input! Please enter a number.")
```



## 🔄 Catching Multiple Exceptions

You can handle multiple exceptions using multiple `except` blocks or grouping them together.

### 📦 Multiple Exceptions, Separate Blocks:
```python
try:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    result = x / y
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

### 🧩 Grouped Exceptions:
```python
try:
    x = int(input("Enter a number: "))
    print(100 / x)
except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero.")
```


## 🎯 General Exception Handling

To catch all types of exceptions, use a generic `except` clause — but it's best practice to log the error for debugging.

🔹 **Example:**
```python
try:
    x = int(input("Enter a number: "))
    print(100 / x)
except Exception as e:
    print(f"An error occurred: {e}")
```

🔸 This is useful for logging or displaying general error messages while still allowing specific handlers for known issues.



## 🧼 Finally Clause – Always Execute Cleanup Code

The `finally` block always executes, whether an exception occurs or not. It’s ideal for closing files, network connections, or releasing resources.

🔹 **Example:**
```python
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Cleaning up...")
    try:
        file.close()
    except:
        pass
```

🔸 Even if an exception occurs, the `finally` block runs after the `try` and `except` blocks.



## 🌟 Else Clause – Run Code When No Exception Occurs

Use the `else` block to run code only **if no exception was raised**.

🔹 **Example:**
```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Can't divide by zero.")
else:
    print(f"Result: {result}")
```

🔸 The `else` block helps separate logic that should only execute on success.



## 🔄 Complete `try...except...else...finally` Flow

This structure gives you full control over exception handling and resource management.

🔹 **Example:**
```python
try:
    x = int(input("Enter a number: "))
    result = 100 / x
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(f"Result: {result}")
finally:
    print("Program finished.")
```

🔸 **Execution Order:**
1. `try`
2. If exception → `except` → `finally`
3. If no exception → `else` → `finally`



## 🧩 Raising Exceptions Manually

You can raise exceptions manually using the `raise` keyword.

🔹 **Example:**
```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Age is valid.")

try:
    validate_age(-5)
except ValueError as e:
    print(f"Caught error: {e}")
```

🔸 Useful for enforcing business rules or data validation.



## 🧹 Best Practices for Exception Handling

- ❌ Don’t use bare `except:` without specifying an exception type.
- ✅ Prefer catching specific exceptions to avoid hiding bugs.
- 📝 Use `finally` for cleanup operations like closing files or database connections.
- 📊 Use `else` to isolate code that doesn’t need exception handling.
- 📌 Log exceptions in production apps instead of just printing them.
- 🛡️ Validate inputs before risky operations to reduce exceptions.



## 🧪 Real-World Examples

### 🧮 Sales Growth Calculator with Exception Handling

```python
print('Enter the net sales for')
try:
    previous = float(input('- Prior period: '))
    current = float(input('- Current period: '))
    change = (current - previous) * 100 / previous
    status = 'increase' if change > 0 else 'decrease'
    print(f"Sales {status} by {abs(change):.2f}%")
except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Prior period value cannot be zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```



🎉 Congratulations! You now have a solid understanding of **Python Exception Handling** — including how to use `try...except`, `else`, and `finally` blocks, raise custom exceptions, and apply best practices to make your programs more robust.

Next up: 🔁 **Section 9: More on Python Loops** – learn advanced loop techniques like `for...else`, `while...else`, and emulate do-while behavior.
