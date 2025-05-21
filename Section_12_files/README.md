# 📄 Section 12: Working with Files

📂 **Learn how to read from and write to files in Python**, including text files, CSV files, and how to check if a file exists. This section also includes best practices for handling files safely and efficiently.



## 🧠 What You'll Learn

- 📖 How to **read** from text files using `open()`, `read()`, `readline()`, and `readlines()`
- ✍️ How to **write** to text files using `write()` and `writelines()`
- ➕ How to **append** data to existing files
- 🆕 How to **create** new files
- 🔍 How to **check if a file exists**
- 📊 How to **read and write CSV files** using the built-in `csv` module
- 🗑️ How to **rename and delete files**
- 💡 Hidden tips and best practices for working with files in Python



## 📖 Reading from a Text File

Python provides several ways to read from a file using the built-in `open()` function.

### ✅ Using `with open()` – Best Practice
The `with` statement ensures the file is closed automatically after use.

🔹 **Example – Read entire file:**
```python
with open('readme.txt') as f:
    content = f.read()
    print(content)
```

🔸 Use `f.readlines()` to get all lines as a list:
```python
with open('readme.txt') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
```

🔸 Use `f.readline()` to read one line at a time:
```python
with open('readme.txt') as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()
```



## ✍️ Writing to a Text File

Use the `'w'` mode to create or overwrite a file.

🔹 **Example – Write a string to a file:**
```python
with open('readme.txt', 'w') as f:
    f.write("This is a new file.")
```

🔹 **Write multiple lines:**
```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open('readme.txt', 'w') as f:
    f.writelines(lines)
```

🔸 To ensure proper formatting, manually add newline characters (`\n`) when needed.



## ➕ Appending to a Text File

Use the `'a'` mode to append to an existing file without overwriting it.

🔹 **Example – Append text to the end of a file:**
```python
with open('readme.txt', 'a') as f:
    f.write("\nThis line was appended.")
```


## 🆕 Creating a New Text File

Use the `'w'` or `'x'` mode to create a new file.

🔹 **Using `'w'`:**
```python
with open('newfile.txt', 'w') as f:
    f.write("New file created!")
```

🔹 **Using `'x'` (exclusive creation):**
```python
try:
    with open('newfile.txt', 'x') as f:
        f.write("New file created!")
except FileExistsError:
    print("File already exists.")
```

🔸 The `'x'` mode prevents accidental overwriting.


## 🔍 Check If a File Exists

You can use either `os.path.exists()` or `pathlib.Path().is_file()`.

🔹 **Using `os.path.exists()`:**
```python
import os

if os.path.exists('readme.txt'):
    print("File exists.")
else:
    print("File does not exist.")
```

🔹 **Using `pathlib`:**
```python
from pathlib import Path

file = Path('readme.txt')
if file.is_file():
    print("File exists.")
```


## 📊 Reading and Writing CSV Files

Use the built-in `csv` module to handle comma-separated values (CSV) files.

### 📥 Reading from a CSV File

🔹 **Example – Read and display CSV rows:**
```python
import csv

with open('countries.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
```

🔸 You can also use `DictReader` to map each row to a dictionary:
```python
with open('countries.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['area'])
```

### 📤 Writing to a CSV File

🔹 **Example – Write a single row:**
```python
import csv

header = ['name', 'area', 'country_code2']
data = ['Afghanistan', 652090, 'AF']

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
```

🔹 **Write multiple rows:**
```python
rows = [
    ['Albania', 28748, 'AL'],
    ['Algeria', 2381741, 'DZ']
]
writer.writerows(rows)
```

🔸 Don’t forget `newline=''` to avoid extra blank lines in some OS environments.



## 🔄 Rename a File

Use `os.rename(old_name, new_name)` to rename a file.

🔹 **Example:**
```python
import os
os.rename('oldfile.txt', 'newfile.txt')
```



## 🗑️ Delete a File

Use `os.remove(filename)` to delete a file.

🔹 **Example:**
```python
import os
os.remove('oldfile.txt')
```

🔸 Always check if the file exists before deleting:
```python
if os.path.exists('oldfile.txt'):
    os.remove('oldfile.txt')
```



## 📁 Common Errors & Fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `FileNotFoundError` | Trying to read/write a file that doesn't exist | Ensure file path is correct |
| `PermissionError` | No permission to access the file | Run script with elevated privileges |
| Extra blank lines in CSV | Missing `newline=''` | Add `newline=''` in `open()` |
| `FileExistsError` with `'x'` | File already exists | Use `'w'` to overwrite or handle the exception |



## 💡 Hidden Tips & Notes

- 🔒 Always use the `with` statement to open files — it ensures files are closed properly.
- 📁 When writing to a subdirectory like `docs/readme.txt`, make sure the folder exists first.
- ⚠️ Opening too many files without closing them may lead to **race conditions** or resource exhaustion.
- 🧩 Use `encoding='utf-8'` when dealing with non-ASCII characters.
- 🧪 Use `try...except` blocks to handle errors gracefully (e.g., missing directories).
- 🧹 Avoid hardcoding paths — use `os.path` or `pathlib` for cross-platform compatibility.



## 🧪 Real-World Examples

### ✅ Example 1: Create and Write to a File

```python
try:
    with open('docs/report.txt', 'w', encoding='utf-8') as f:
        f.write("Sales Report\n")
        f.write("-----------\n")
        f.write("Total Revenue: $100,000\n")
except FileNotFoundError:
    print("Directory 'docs' does not exist. Please create it first.")
```

### ✅ Example 2: Read and Display CSV Data

```python
import csv

try:
    with open('data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"{row['Product']} - ${row['Price']}")
except FileNotFoundError:
    print("CSV file not found.")
```



## 📌 Summary

| Task | Code |
|------|------|
| Read file | `with open('file.txt') as f: content = f.read()` |
| Write file | `with open('file.txt', 'w') as f: f.write(...)` |
| Append file | `with open('file.txt', 'a') as f: f.write(...)` |
| Create file safely | `'x'` mode with error handling |
| Check file exists | `os.path.exists('file.txt')` or `Path('file.txt').is_file()` |
| Read CSV | `csv.reader()` or `csv.DictReader()` |
| Write CSV | `csv.writer()` or `csv.DictWriter()` |
| Rename file | `os.rename(old, new)` |
| Delete file | `os.remove(filename)` |



🎉 Congratulations! You now have a solid understanding of how to **work with files in Python**, including reading, writing, renaming, and deleting files, and handling CSV data effectively.

Next up: 📁 **Section 13: Working Directories** – learn how to interact with your file system, list files, and manage directory structures.
