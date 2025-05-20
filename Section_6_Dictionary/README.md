# 🗂️ Section 6: Dictionaries

🗄️ **Learn how to work with Python dictionaries — a powerful data structure for storing key-value pairs.**

Dictionaries allow you to store and retrieve data efficiently by mapping keys to values, making them ideal for tasks like configuration settings, JSON-like structures, and more.

## 🧠 What is a Dictionary?

A dictionary is an **unordered collection of key-value pairs** where:
- Each key must be **immutable** (e.g., string, number, tuple).
- Values can be any type (including lists, other dictionaries, etc.).

🔹 **Syntax:**
```python
my_dict = {
    'key1': 'value1',
    'key2': 'value2'
}
```

🔹 **Example:**
```python
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}
```

🔸 You can also create an **empty dictionary**:
```python
empty_dict = {}
```



## 🔍 Accessing Values

Use the **square bracket `[]` notation** or `.get()` method to access values by key.

🔹 **Using `[]`:**
```python
print(person['first_name'])  # Output: John
```

🔹 **Using `.get()`:**
```python
print(person.get('age'))            # Output: 25
print(person.get('ssn'))           # Output: None
print(person.get('ssn', '000-00-0000'))  # Output: 000-00-0000
```

🔸 Using `.get()` prevents `KeyError` if the key doesn’t exist.



## ➕ Adding or Updating Key-Value Pairs

You can dynamically add or update entries in a dictionary.

🔹 **Add new key-value pair:**
```python
person['gender'] = 'Male'
```

🔹 **Update existing value:**
```python
person['age'] = 26
```



## 🚫 Removing Key-Value Pairs

Use the `del` statement or `.pop()` method.

🔹 **Using `del`:**
```python
del person['active']
```

🔹 **Using `.pop()`:**
```python
fav_color = person.pop('favorite_colors')
```



## 🔁 Iterating Over a Dictionary

### 📦 Loop Through Key-Value Pairs
Use `.items()` to get both keys and values.

```python
for key, value in person.items():
    print(f"{key}: {value}")
```

### 🔑 Loop Through Keys Only
Use `.keys()` or default iteration behavior.

```python
for key in person.keys():
    print(key)

# Same as:
for key in person:
    print(key)
```

### 📄 Loop Through Values Only
Use `.values()`.

```python
for value in person.values():
    print(value)
```



## 🧩 Dictionary Comprehensions

Create new dictionaries from existing ones using concise and expressive syntax.

🔹 **General Syntax:**
```python
{key: value for (key, value) in dict.items() if condition}
```

### ✅ Example: Transform Values

```python
stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219
}

new_stocks = {s: p * 1.02 for (s, p) in stocks.items()}
print(new_stocks)
# Output: {'AAPL': 123.42, 'AMZN': 3447.6, 'MSFT': 223.38}
```

### 🔍 Example: Filter Items

```python
selected_stocks = {s: p for (s, p) in stocks.items() if p > 200}
print(selected_stocks)
# Output: {'AMZN': 3380, 'MSFT': 219}
```



## ⚠️ Important Notes

- Dictionaries are **mutable**.
- Keys must be **immutable types** (like strings, numbers, tuples).
- Since Python 3.7+, dictionaries preserve **insertion order**.
- Avoid using duplicate keys — only the last value will remain.



## 🧪 Try It Yourself

```python
# Sample dictionary
employee = {
    'name': 'Alice',
    'role': 'Developer',
    'department': 'Engineering',
    'salary': 90000
}

# Add bonus
employee['salary'] = int(employee['salary'] * 1.10)

# Print updated info
for key, value in employee.items():
    print(f"{key.capitalize()}: {value}")
```



🎉 Congratulations! You now have a solid understanding of **Python Dictionaries** — including how to define, access, modify, iterate, and filter them using dictionary comprehensions.

Next up: 🔄 **Section 7: Sets** – learn how to work with unique collections of items!

