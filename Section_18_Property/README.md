# 🔐 Section 18: Property  
## Control Attribute Access in Python Classes

🧩 **Learn how to use properties in Python to control access to attributes**, including how to define getters, setters, and deleters using both the `property()` function and the `@property` decorator.

This section covers:
- 📦 Using `property()` to define property attributes
- 🎀 Using `@property` for clean, readable syntax
- 🧮 Defining read-only properties
- 🗑️ Deleting a property with `@property.deleter`
- 💡 Hidden notes and best practices for safe attribute management



## 🧠 What You'll Learn

| Concept | Description |
|--------|-------------|
| **Property** | Encapsulate attribute access logic inside a class |
| **Getter** | Define how an attribute is retrieved |
| **Setter** | Define validation or behavior when assigning a value |
| **Deleter** | Define what happens when an attribute is deleted |
| **Read-only property** | Getter only – prevents modification |
| **Computed property** | Value derived from other data, not stored directly |


## 🧱 The `property()` Function

Use the `property()` function to define properties that encapsulate attribute access logic.

🔹 **Example – Define a Person class with age validation**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_age(self):
        print("Getting age...")
        return self._age

    def set_age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value

    def del_age(self):
        print("Deleting age")
        del self._age

    age = property(get_age, set_age, del_age, "The person's age")

p = Person("Alice", 30)
print(p.age)  # Calls get_age()
p.age = 25    # Calls set_age()
del p.age     # Calls del_age()
```

🔸 This allows you to add logic around attribute access without breaking backward compatibility.



## 🎀 The `@property` Decorator

A cleaner and more modern way to define properties using decorators.

🔹 **Example – Using `@property` for encapsulation**
```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        print("Fetching price...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price")
        del self._price
```

🔹 **Usage Example:**
```python
prod = Product("Laptop", 999)

print(prod.price)       # Output: Fetching price... 999
prod.price = 950        # OK
prod.price = -100       # Raises ValueError
```



## 📝 Read-only Properties

Define a property with only a getter to make it read-only.

🔹 **Example – Read-only ID**
```python
import uuid

class User:
    def __init__(self, username):
        self.username = username
        self._id = uuid.uuid4()

    @property
    def id(self):
        return self._id
```

🔹 **Usage:**
```python
user = User("john_doe")
print(user.id)   # Works fine
user.id = 100   # ❌ Raises AttributeError
```

🔸 Even though `_id` can still be changed (`user._id = 100`), this discourages accidental modification.



## 🧮 Computed (Dynamic) Properties

Create properties that are computed on-the-fly, rather than stored as instance variables.

🔹 **Example – Compute full name dynamically**
```python
class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
```

🔹 **Usage:**
```python
emp = Employee("John", "Doe")
print(emp.full_name)  # John Doe
emp.first_name = "Jane"
print(emp.full_name)  # Jane Doe
```

🔸 The `full_name` property doesn't store any value — it’s always up-to-date based on current values.



## 🗑️ Delete a Property

Use `@property.deleter` to define behavior when deleting an attribute.

🔹 **Example – Controlled deletion of a property**
```python
class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
        self._active = True

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, value):
        if not isinstance(value, bool):
            raise ValueError("Value must be boolean")
        self._active = value

    @active.deleter
    def active(self):
        print("Archiving account...")
        self._active = False
```

🔹 **Usage:**
```python
acc = Account("A1234", 1000)
del acc.active
print(acc.active)  # Now False
```



## 🧪 Real-World Example – Temperature Sensor Class

Let’s build a class that uses properties to validate and compute values.

```python
class TemperatureSensor:
    def __init__(self, sensor_id, initial_temp):
        self.sensor_id = sensor_id
        self._temp = initial_temp

    @property
    def temperature(self):
        print(f"[{self.sensor_id}] Getting temperature: {self._temp}°C")
        return self._temp

    @temperature.setter
    def temperature(self, value):
        print(f"[{self.sensor_id}] Setting temperature to {value}°C")
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is invalid")
        self._temp = value

    @property
    def status(self):
        if self._temp > 100:
            return "Overheating"
        elif self._temp < 0:
            return "Freezing"
        else:
            return "Normal"
```

🔹 **Usage:**
```python
sensor = TemperatureSensor("T1", 25)
sensor.temperature = 80
sensor.temperature = 120  # Triggers overheating warning
sensor.temperature = -10  # Sets freezing status
```


## 💡 Hidden Tips & Notes

- 🧩 Always prefix internal attributes with `_` when using properties — it signals they’re protected.
- 🧱 Avoid side effects in property getters — keep them lightweight.
- 📏 Use properties to enforce constraints like minimum/maximum values.
- 🧾 If you want to document your property, include a docstring inside the getter.
- 🚫 Be cautious with deleters — they may cause undefined state if not handled carefully.
- 🧵 Prefer `@property` over `property()` for better readability.
- 🧰 Use computed properties to avoid storing redundant data.



## 📌 Summary

| Feature | Purpose |
|--------|---------|
| `property()` | Legacy-style way to create properties |
| `@property` | Modern, decorator-based property definition |
| `@property.setter` | Define validation logic when setting a value |
| `@property.deleter` | Define behavior when deleting a property |
| Read-only | Only a getter — prevents assignment |
| Computed property | Not stored; calculated from other data |



🎉 Congratulations! You now understand how to **control attribute access using properties**, including how to:
- Validate input values
- Make attributes read-only
- Compute dynamic values
- Define custom behaviors on deletion

Next up: 🔄 **Section 19: Inheritance** – learn how to extend classes and reuse code through inheritance.

