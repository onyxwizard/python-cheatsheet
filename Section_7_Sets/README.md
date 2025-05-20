# 🧮 Section 7: Sets

🧩 **Learn how to work with sets in Python — an unordered collection of unique, immutable elements.**

Sets are powerful for tasks like removing duplicates, performing mathematical set operations (union, intersection, difference), and checking membership efficiently.



## 🧠 What is a Set?

A **set** is an **unordered collection of unique items**. It supports:
- Membership testing (`in`)
- Iteration
- Mathematical operations like union, intersection, and difference

### 🔹 **Key Characteristics:**
- Elements must be **immutable** (e.g., numbers, strings, tuples)
- Elements are **not duplicated**
- Order of elements is **not guaranteed**

#### 🔹 **Syntax:**
```python
skills = {'Python programming', 'Databases', 'Software design'}
```

🔸 You can also create a set from an iterable:
```python
chars = set('letter')  # {'l', 'e', 't', 'r'}
```



## 🚫 Creating Empty Sets

⚠️ Don’t use `{}` – it creates an empty **dictionary**, not a set.

#### 🔹 **Correct way:**
```python
empty_set = set()
```



## 🔍 Accessing Elements

Since sets are **unordered**, you **cannot access elements by index**.

🔹 Use a `for` loop or `in` operator:

### ✅ Loop Through Elements:
```python
for skill in skills:
    print(skill)
```

### ✅ Check Membership:
```python
print('Python programming' in skills)  # True
```



## ➕ Adding Elements

Use `.add()` to insert a new element.

#### 🔹 **Example:**
```python
skills.add('Problem solving')
```

🔸 If the element already exists, no error is raised and nothing changes.



## 🚫 Removing Elements

There are several methods to remove elements based on your needs:

| Method        | Behavior                                  |
|---------------|-------------------------------------------|
| `.remove(x)`  | Removes `x`, raises `KeyError` if missing |
| `.discard(x)` | Removes `x`, no error if missing          |
| `.pop()`      | Removes and returns an arbitrary element   |
| `.clear()`    | Removes all elements                      |

### 🔹 **Examples:**
```python
skills.remove('Databases')     # May raise KeyError
skills.discard('Java')         # Safe removal
skills.pop()                   # Remove random item
skills.clear()                 # Empty the set
```


## 🧱 Set Operations

### 🌐 Union (`|` or `.union()`)
Returns a new set containing **all elements from both sets**.

### 🔹 **Example:**
```python
set1 = {'Python', 'Java'}
set2 = {'C++', 'JavaScript'}
combined = set1 | set2
# OR
combined = set1.union(set2)
```

🔸 `.union()` accepts any iterable, while `|` only works with sets.



### 🔵 Intersection (`&` or `.intersection()`)
Returns elements **common to all sets**.

### 🔹 **Example:**
```python
s1 = {'Python', 'Java'}
s2 = {'Java', 'C++'}
common = s1 & s2  # {'Java'}
```


### 🔺 Difference (`-` or `.difference()`)
Returns elements in the first set that are **not in the second**.

### 🔹 **Example:**
```python
s1 = {'Python', 'Java'}
s2 = {'Java', 'C++'}
diff = s1 - s2  # {'Python'}
```



### 🟡 Symmetric Difference (`^` or `.symmetric_difference()`)
Returns elements present in **either set but not both**.

### 🔹 **Example:**
```python
s1 = {'Python', 'Java'}
s2 = {'Java', 'C++'}
result = s1 ^ s2  # {'Python', 'C++'}
```



## 📐 Subset and Superset Checks

### ✅ Is Subset?
Check if all elements of one set are in another.

### 🔹 **Methods:**
```python
a = {1, 2}
b = {1, 2, 3}

print(a.issubset(b))  # True
print(a <= b)          # True
print(a < b)           # True (proper subset)
```



### ✅ Is Superset?
Check if a set contains all elements of another.

### 🔹 **Methods:**
```python
print(b.issuperset(a))  # True
print(b >= a)            # True
print(b > a)             # True (proper superset)
```



## 🔁 Disjoint Sets

Two sets are **disjoint** if they have **no elements in common**.

### 🔹 **Method:**
```python
set1 = {1, 2}
set2 = {3, 4}
print(set1.isdisjoint(set2))  # True
```



## 🧼 Set Comprehensions

Create sets using concise syntax.

### 🔹 **Syntax:**
```python
{expression for element in iterable if condition}
```

### 🔹 **Example – Lowercase Tags:**
```python
tags = {'Django', 'Pandas', 'Numpy'}
lower_tags = {tag.lower() for tag in tags}
```

### 🔹 **Filter Example:**
```python
numbers = {1, 2, 3, 4, 5}
evens = {n for n in numbers if n % 2 == 0}
```



## 🧊 Frozen Sets (Immutable Sets)

To make a set **immutable**, wrap it in `frozenset()`.

### 🔹 **Example:**
```python
skills = frozenset({'Python', 'SQL'})
```

🔸 Attempting to modify will raise an error:
```python
skills.add('Git')  # ❌ AttributeError
```



## 📏 Useful Built-in Functions

| Function | Description                         |
|---------|-------------------------------------|
| `len()` | Get number of elements              |
| `in`    | Check for membership                |
| `set()` | Convert to a set                    |

### 🔹 **Example:**
```python
skills = {'Problem solving', 'Design', 'Python'}
print(len(skills))  # Output: 3
print('Design' in skills)  # True
```


## 📝 Notes & Tips

- **Order is not preserved** – don’t rely on element position.
- **Duplicates are removed automatically** when creating or updating a set.
- Use `set()` with lists/tuples to easily remove duplicates.
- `frozenset` is useful for keys in dictionaries or as elements in other sets.
- Use `set.intersection()` over `&` if working with non-set iterables.



🎉 Congratulations! You now have a solid understanding of **Python Sets** — including how to define them, perform set operations, and use them effectively in real-world scenarios.

Next up: ⚠️ **Section 8: Exception Handling** – learn how to handle errors gracefully in your programs!
