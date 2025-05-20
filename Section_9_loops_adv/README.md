# 🔁 Section 9: More on Python Loops

🔁 **Learn advanced looping techniques in Python**, including the `for...else` and `while...else` constructs, and how to emulate the classic `do...while` loop using standard Python syntax.

This section is designed to help you **write more expressive and robust loops** by understanding how to control execution flow beyond basic iteration.



## 🧠 What You'll Learn

- ✅ How to use `for...else` and `while...else` statements
- 🔁 How to emulate a `do...while` loop in Python
- 📌 Use cases and best practices for each construct
- 💡 Hidden tips and notes that improve readability and avoid common mistakes



## 🔄 `for...else` Statement

Python allows the `else` clause to be used with the `for` loop — this is **not available in most other programming languages**.

🔹 **Syntax:**
```python
for item in iterable:
    # code to process item
    if condition:
        break
else:
    # code to run if loop completes normally (no break)
```

🔸 The `else` block runs **only if the loop completes all iterations without encountering a `break` statement.**

### ✅ Example – Search Item in List:

```python
fruits = ['apple', 'banana', 'cherry']
search = 'mango'

for fruit in fruits:
    if fruit == search:
        print(f"Found {search}!")
        break
else:
    print(f"{search} not found.")
```

🔹 **Use Cases:**
- Searching for an item in a collection
- Validating input or data before proceeding
- Checking conditions across an entire sequence


## ⏳ `while...else` Statement

Just like `for`, the `while` loop can also have an `else` clause.

🔹 **Syntax:**
```python
while condition:
    # code to execute while condition is True
    if some_condition:
        break
else:
    # code to run if loop exits because condition became False
```

🔸 The `else` block runs **if the loop exited due to the condition becoming `False`**, **not** from a `break`.

### ✅ Example – User Login Attempt:

```python
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    if password == "secret":
        print("Login successful!")
        break
    print("Incorrect password.")
    attempts += 1
else:
    print("Account locked due to too many failed attempts.")
```

🔹 **Use Cases:**
- Retry logic with limits
- Game loops
- Input validation with retries


## 🎯 Emulating `do...while` Loop in Python

Unlike languages like Java or C++, Python **does not have a built-in `do...while` loop**, but you can **emulate it** using a `while` loop with a `break`.

🔹 **Concept:**
The `do...while` loop executes the body **at least once**, then checks the condition at the end of each iteration.

### ✅ Example – Number Guessing Game:

```python
import random

MIN, MAX = 1, 10
secret_number = random.randint(MIN, MAX)

while True:
    guess = int(input(f"Guess a number between {MIN} and {MAX}: "))
    
    if guess > secret_number:
        print("Too high. Try again.")
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Bingo! You guessed it!")
        break
```

🔹 This pattern ensures the user makes at least one guess before checking whether to continue.

### 📝 Key Points:
- Use `while True` to simulate the “do” part.
- Add a `break` when the exit condition is met.
- Ideal for scenarios where the loop must run at least once.



## 🧩 Real-World Use Cases

| Construct       | Use Case                                               |
|------------------|--------------------------------------------------------|
| `for...else`     | Search algorithms, validation, checking all elements   |
| `while...else`   | Game loops, retry logic, login systems               |
| `do...while` emulation | Prompting users, input validation, menu loops |



## 🧠 Hidden Details & Notes

- 🔁 The `else` block in both `for` and `while` loops **runs only when the loop completes naturally** — not when interrupted by `break`, `return`, or exceptions.
- ❗ Avoid putting complex logic inside the `else` block unless necessary — it can reduce readability.
- 🧪 The `else` clause is often misunderstood and underused — but **very useful** in scenarios where you want to handle a “none found” or “loop completed” case.
- 🚫 Using `continue` does **not** affect the `else` clause — only `break` does.
- 🧹 Always test edge cases — especially when working with empty iterables in `for...else`.



## 🧪 Try It Yourself

### ✅ Example – Prime Checker Using `for...else`:

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is divisible by {i}. Not a prime.")
            break
    else:
        print(f"{n} is a prime number.")
        return True
    return False

is_prime(17)
```



🎉 Congratulations! You now have a solid understanding of **advanced loop structures in Python**, including how to use `for...else`, `while...else`, and emulate `do...while` behavior.

Next up: 📦 **Section 10: More on Python Functions** – learn about unpacking tuples, variable arguments (`*args`, `**kwargs`), partial functions, and type hints.

