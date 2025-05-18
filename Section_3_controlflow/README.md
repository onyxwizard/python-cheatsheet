# 🔁 Section 3: Control Flow

🧠 **Learn how to make decisions and control the flow of your Python programs.**

Control flow allows you to execute different blocks of code based on conditions, loop through data, and manage program execution more effectively.



## ❓ `if` Statement

Use the `if` statement to run a block of code if a condition is **True**.

🔹 **Syntax:**
```python
if condition:
    # code to run if condition is True
```

🔹 **Example:**
```python
age = input('Enter your age:')
if int(age) >= 18:
    print("You're eligible to vote.")
```

🔸 **Important Notes:**
- Use indentation (`4 spaces`) to define the code block.
- A colon `:` is required after the condition.
- If the condition is false, the block is skipped.



## 🎯 `if...else` Statement

Run one block of code if the condition is **True**, and another if it's **False**.

🔹 **Syntax:**
```python
if condition:
    # code if True
else:
    # code if False
```

🔹 **Example:**
```python
age = input('Enter your age:')
if int(age) >= 18:
    print("You're eligible to vote.")
else:
    print("You're not eligible to vote.")
```



## 🧩 `if...elif...else` Statement

Check multiple conditions in sequence and execute the first matching block.

🔹 **Syntax:**
```python
if condition1:
    # code for condition1
elif condition2:
    # code for condition2
else:
    # default code
```

🔹 **Example:**
```python
your_age = int(input('Enter your age: '))
if your_age < 5:
    ticket_price = 5
elif your_age < 16:
    ticket_price = 10
else:
    ticket_price = 18
print(f"Ticket price: ${ticket_price}")
```



## 🎯 Ternary Operator

A concise way to write conditional expressions in one line.

🔹 **Syntax:**
```python
value_if_true if condition else value_if_false
```

🔹 **Example:**
```python
age = 20
ticket_price = 20 if age >= 18 else 5
print(f"Ticket Price: ${ticket_price}")
```

🔸 This is great for simple conditions and variable assignment.



## 🔁 `for` Loop with `range()`

Execute a block of code a fixed number of times.

🔹 **Basic Syntax:**
```python
for index in range(n):
    # code to repeat
```

🔹 **Examples:**

### Print numbers from 0 to 4:
```python
for i in range(5):
    print(i)
```

### Print numbers from 1 to 5:
```python
for i in range(1, 6):
    print(i)
```

### Print even numbers from 0 to 10:
```python
for i in range(0, 11, 2):
    print(i)
```

🔸 You can also use `for` loops to calculate sums or process sequences:
```python
total = 0
for num in range(101):
    total += num
print("Sum:", total)  # Output: 5050
```



## ⏳ `while` Loop

Repeat a block of code as long as a condition is **True**.

🔹 **Syntax:**
```python
while condition:
    # code to repeat
```

🔹 **Example:**
```python
counter = 0
max = 5
while counter < max:
    print(counter)
    counter += 1
```

🔸 **Important:**
- Always ensure the loop has a way to terminate.
- The condition is checked before each iteration.

🔹 **Infinite Loop Example (with exit):**
```python
while True:
    command = input('> ').lower()
    if command == 'quit':
        break
    print(f"Echo: {command}")
```


## 🔚 `break` Statement

Exit a loop prematurely when a condition is met.

🔹 **Used with `for` or `while` loops.**

🔹 **Example with `for`:**
```python
for i in range(10):
    print(i)
    if i == 3:
        break
```

🔹 **Example with `while`:**
```python
while True:
    color = input('Enter favorite color: ')
    if color.lower() == 'quit':
        break
```



## ⏭️ `continue` Statement

Skip the current iteration and move to the next one.

🔹 **Used with `for` or `while` loops.**

🔹 **Example – Print only even numbers:**
```python
for i in range(10):
    if i % 2:
        continue
    print(i)
```

🔹 **Example – Skip even numbers:**
```python
count = 0
while count < 10:
    count += 1
    if count % 2 == 0:
        continue
    print(count)
```



## 🪟 `pass` Statement

A placeholder that does nothing — useful for writing empty functions, classes, or incomplete logic.

🔹 **Example – Placeholder for future logic:**
```python
if True:
    pass  # do nothing
```

🔹 **Example – Empty function/class:**
```python
def my_function():
    pass

class MyEmptyClass:
    pass
```

---

🎉 You now have a strong foundation in **Python Control Flow**!

Next up: 📦 **Section 4: Functions** – learn how to create reusable blocks of code.

