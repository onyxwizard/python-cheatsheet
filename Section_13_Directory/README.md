# 📁 Section 13: Working Directories

📁 **Learn how to manipulate directories in Python** using the `os` module. This includes getting and changing the current working directory, creating, renaming, and deleting directories, listing files, and traversing directory trees.

This section will help you interact with your file system in a cross-platform way — ideal for automation scripts, data processing, and file management tasks.



## 🧠 What You'll Learn

- 📍 How to get and change the **current working directory**
- 🔗 Use `os.path.join()` and `os.path.split()` for **cross-platform path handling**
- 📂 Check if a path is a valid **directory**
- ➕ Create new directories safely
- 🔄 Rename directories
- 🗑️ Delete empty directories
- 🔍 Traverse directory contents recursively using `os.walk()`
- 📋 List all files (or specific types) from a directory and its subdirectories
- 💡 Hidden tips and best practices for working with directories in Python



## 📍 Get Current Working Directory

Use `os.getcwd()` to find out where your script is currently running.

🔹 **Example:**
```python
import os

cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")
```

🔸 This is useful when working with relative paths or debugging file access issues.



## 🔄 Change Working Directory

Use `os.chdir(path)` to switch to a different directory.

🔹 **Example:**
```python
os.chdir('/script')
print(os.getcwd())  # Output: /script
```

⚠️ If the target directory doesn’t exist, it raises a `FileNotFoundError`.



## 🔗 Join and Split Paths

Use `os.path.join()` to build paths that work across Windows, macOS, and Linux.

🔹 **Join Example:**
```python
import os

path = os.path.join('data', 'files', 'input.txt')
print(path)
# Output: data/files/input.txt (Linux/macOS) or data\files\input.txt (Windows)
```

🔹 **Split Example:**
```python
parts = os.path.split(path)
print(parts)  # ('data/files', 'input.txt') or ('data\\files', 'input.txt')
```

💡 Always use these functions instead of hardcoding slashes (`/` or `\`) to ensure compatibility.



## 🔍 Test If a Path Is a Directory

Use `os.path.exists()` and `os.path.isdir()` to check if a path exists and is a directory.

🔹 **Example:**
```python
dir_path = os.path.join("C:\\", "temp")

if os.path.exists(dir_path) and os.path.isdir(dir_path):
    print(f"{dir_path} is a valid directory.")
else:
    print(f"{dir_path} is not a valid directory.")
```

🔸 These checks prevent errors when trying to access non-existent or invalid paths.



## ➕ Create a New Directory

Use `os.mkdir()` to create a new directory.

🔹 **Best Practice – Only create if it doesn't exist:**
```python
dir = os.path.join("C:\\", "temp", "python")
if not os.path.exists(dir):
    os.mkdir(dir)
    print(f"Directory '{dir}' created.")
```

🔸 To create nested directories at once, use `os.makedirs()`:
```python
os.makedirs(os.path.join("project", "data", "raw"), exist_ok=True)
```



## 🔄 Rename a Directory

Use `os.rename(old_path, new_path)` to rename or move a directory.

🔹 **Example:**
```python
old_dir = os.path.join("C:\\", "temp", "python")
new_dir = os.path.join("C:\\", "temp", "python3")

if os.path.exists(old_dir) and not os.path.exists(new_dir):
    os.rename(old_dir, new_dir)
    print(f"'{old_dir}' was renamed to '{new_dir}'")
```

⚠️ If the new name already exists, it raises a `FileExistsError`.



## 🗑️ Delete a Directory

Use `os.rmdir(path)` to delete an **empty** directory.

🔹 **Example:**
```python
dir = os.path.join("C:\\", "temp", "python")
if os.path.exists(dir):
    os.rmdir(dir)
    print(f"{dir} has been removed.")
```

🔸 To delete a directory **and all its contents**, use `shutil.rmtree()`:
```python
import shutil

shutil.rmtree(dir)  # Removes directory even if not empty
```



## 🔍 Traverse a Directory Tree Recursively

Use `os.walk()` to traverse directories and list files/subdirectories.

🔹 **Example – Print all files and folders:**
```python
for root, dirs, files in os.walk("c:\\temp"):
    print(f"{root} has {len(files)} files")
```

🔸 This function is essential for recursive file operations like searching, copying, or batch processing.



## 📋 List Files from a Directory

### ✅ Basic File Listing

```python
for root, _, files in os.walk("D:\\web"):
    for file in files:
        print(file)
```

### ✅ Filter by Extension

```python
html_files = []

for root, _, files in os.walk("D:\\web"):
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

for f in html_files:
    print(f)
```

### 🧩 Reusable Function – List Files by Extension

```python
def list_files(path, extensions=None):
    """List files in path. If extensions provided, filter by them."""
    for root, _, files in os.walk(path):
        for file in files:
            if extensions is None:
                yield os.path.join(root, file)
            else:
                for ext in extensions:
                    if file.endswith(ext):
                        yield os.path.join(root, file)

# Usage
for f in list_files(r"D:\web", (".html", ".css")):
    print(f)
```

🔸 Using a generator (`yield`) makes this function memory-efficient for large directories.



## 🧪 Real-World Examples

### ✅ Example: Backup All `.txt` Files

```python
import shutil

backup_dir = "D:\\backup"
os.makedirs(backup_dir, exist_ok=True)

for src_file in list_files("D:\\documents", [".txt"]):
    dst_file = os.path.join(backup_dir, os.path.basename(src_file))
    shutil.copy2(src_file, dst_file)
    print(f"Copied {src_file} to {dst_file}")
```



## 💡 Hidden Tips & Notes

- 🧩 Use `exist_ok=True` with `os.makedirs()` to avoid exceptions if the directory already exists.
- 🧵 Prefer generators over lists for large file sets.
- 📁 Avoid hardcoded paths — always use `os.path` functions for portability.
- 🚫 `os.rmdir()` only works on **empty** directories.
- 📦 Use `shutil` for advanced operations like copy, move, or remove entire directory trees.
- 🧪 Wrap file/directory operations in `try...except` blocks to handle permission errors gracefully.



## 📌 Summary

| Task | Code |
|------|------|
| Get current directory | `os.getcwd()` |
| Change directory | `os.chdir('new/path')` |
| Join paths | `os.path.join('folder', 'file.txt')` |
| Split path | `os.path.split(path)` |
| Check if path is dir | `os.path.isdir(path)` |
| Create directory | `os.mkdir(path)` |
| Create nested directories | `os.makedirs(path, exist_ok=True)` |
| Rename directory | `os.rename(old, new)` |
| Delete empty directory | `os.rmdir(path)` |
| Traverse directory tree | `os.walk(path)` |
| List files by extension | Custom function using `os.walk()` and `str.endswith()` |


🎉 Congratulations! You now have a solid understanding of how to **manipulate directories and files in Python**, including how to **list, create, rename, and delete directories**, and how to **search and process files recursively**.

Next up: 💬 **Section 14: Strings** – learn about raw strings, escape characters, and how to work with special characters.
