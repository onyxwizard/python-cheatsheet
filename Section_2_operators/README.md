 # 🔣 Section 2: Operators

## 🛠️ **Learn to manipulate data using operators.**

### ➕ Arithmetic Operators
Perform basic math operations like addition, subtraction, multiplication, division, and more.

| Operator | Description           | Example (`a = 5`, `b = 2`) | Result |
|----------|------------------------|----------------------------|--------|
| `+`      | Addition               | `a + b`                    | `7`    |
| `-`      | Subtraction            | `a - b`                    | `3`    |
| `*`      | Multiplication         | `a * b`                    | `10`   |
| `/`      | Division (float)       | `a / b`                    | `2.5`  |
| `//`     | Floor Division         | `a // b`                   | `2`    |
| `%`      | Modulus (remainder)    | `a % b`                    | `1`    |
| `**`     | Exponentiation         | `a ** b`                   | `25`   |

### 🔹 **Examples:**
```python
a = 10
b = 3
print(a + b)   # 13
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

### 🔸 **Use Cases:**
- Check if a number is even or odd: `num % 2 == 0`
- Calculate compound interest:
  ```python
  principal = 1000
  rate = 0.05
  years = 2
  amount = principal * (1 + rate) ** years
  print(f"Total Amount: ${amount:,.2f}")  # Output: $1,102.50
  ```



### ✍️ Assignment Operators
Assign and update variable values efficiently.

| Operator | Equivalent To        | Example (`a = 5`, `b = 2`) |
|----------|----------------------|----------------------------|
| `=`      | Assign value         | `a = 5`                    |
| `+=`     | Add and assign       | `a += b` → `a = a + b`     |
| `-=`     | Subtract and assign  | `a -= b` → `a = a - b`     |
| `*=`     | Multiply and assign  | `a *= b` → `a = a * b`     |
| `/=`     | Divide and assign    | `a /= b` → `a = a / b`     |
| `//=`    | Floor divide & assign| `a //= b` → `a = a // b`   |
| `%=`     | Modulus & assign     | `a %= b` → `a = a % b`     |
| `**=`    | Exponentiate & assign| `a **= b` → `a = a ** b`   |

### 🔹 **Examples:**
```python
count = 0
count += 1   # Same as count = count + 1

quantity = 5
quantity -= 2  # Now quantity = 3

a = 2
a **= 3      # Same as a = a ** 3 → 8
```



### 🔍 Comparison Operators
Compare two values and return a boolean result (`True` or `False`).

| Operator | Description             | Example (`x = 10`, `y = 20`) | Result |
|----------|--------------------------|-------------------------------|--------|
| `==`     | Equal to                 | `x == y`                      | False  |
| `!=`     | Not equal to             | `x != y`                      | True   |
| `>`      | Greater than             | `x > y`                       | False  |
| `<`      | Less than                | `x < y`                       | True   |
| `>=`     | Greater than or equal to | `x >= y`                      | False  |
| `<=`     | Less than or equal to    | `x <= y`                      | True   |

### 🔹 **Examples:**
```python
x = 10
y = 20
print(x < y)       # True
print(x == y)      # False
print(x != y)      # True
```

### 🔸 **String Comparisons:**
```python
print('apple' < 'orange')  # True ('a' comes before 'o')
print('banana' < 'apple')  # False ('b' comes after 'a')
```


### 🧠 Logical Operators
Combine multiple conditions for complex decision-making.

| Operator | Purpose                            | Truth Table Behavior                             |
|----------|------------------------------------|------------------------------------------------|
| `and`    | Returns `True` if both are `True`  | Only returns `True` if both sides are `True`   |
| `or`     | Returns `True` if at least one is `True` | Returns `False` only if both sides are `False` |
| `not`    | Reverses the logical state         | Converts `True` to `False` and vice versa      |

### 🔹 **Examples:**
```python
price = 9.99
print(price > 9 and price < 10)     # True
print(price > 10 or price < 20)     # True
print(not price > 10)               # True
```

### 🔸 **Truth Tables:**

### `and`:
| A     | B     | A and B |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

### `or`:
| A     | B     | A or B |
|-------|-------|--------|
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

### `not`:
| A     | not A |
|-------|--------|
| True  | False  |
| False | True   |


### 🔸**Operator Precedence:**
- `not` > `and` > `or`
- Use parentheses to control evaluation order:
```python
  result = not (price > 5 and price < 10)
  print(result)  # False
  ```



🎉 You now have a solid understanding of **Python Operators**!

Next up: 🔁 **Section 3: Control Flow** – learn how to make decisions and loop through code!
