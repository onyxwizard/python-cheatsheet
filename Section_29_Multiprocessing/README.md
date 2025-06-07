# 🧬 Section 29: Multiprocessing  
## Running CPU-bound Tasks in Parallel with Python

🚀 **Learn how to use the `multiprocessing` module** to run tasks in parallel and improve performance for CPU-bound operations like heavy computations, image processing, or data transformation.

This section covers:
- 🔍 The difference between threading and multiprocessing
- 📦 Using `Process` to create individual processes
- 🔄 Sharing work across multiple cores using `Pool`
- 🧰 Managing process pools with `ProcessPoolExecutor`
- 🧪 Real-world example – parallel image resizing
- 💡 Hidden notes and best practices for safe multiprocessing



## 🧠 What You'll Learn

| Concept | Description |
|--------|-------------|
| **Multiprocessing** | Run code in separate processes (not threads) |
| **CPU-bound vs I/O-bound** | When to choose multiprocessing over multithreading |
| **`multiprocessing.Process`** | Create and manage individual processes |
| **`multiprocessing.Pool`** | Distribute tasks across multiple CPU cores |
| **`concurrent.futures.ProcessPoolExecutor`** | High-level interface for managing process pools |
| **Shared State & IPC** | Share data safely between processes |
| **Best Practices** | Avoiding bottlenees, managing resources, debugging |


## 🔍 Processes vs Threads – Key Differences

| Feature              | Thread                          | Process                         |
|----------------------|----------------------------------|----------------------------------|
| Memory Sharing       | Shared within a process           | Each has its own memory space    |
| Communication        | Easy via shared memory            | Requires inter-process communication |
| Overhead             | Low                              | Higher due to new process creation |
| Execution Model      | Cooperative (GIL limits true parallelism) | True parallelism on multi-core CPUs |
| Ideal For            | I/O-bound tasks                  | CPU-bound tasks                   |

🔹 In Python, **threads are great for waiting**, but not for computing — due to the **Global Interpreter Lock (GIL)**.
🔹 Use **multiprocessing** when you want real **parallel execution** for compute-heavy jobs.



## 🧱 Basic Example – Running Two CPU-bound Tasks in Parallel

Let’s build a simple example that performs two heavy calculations in parallel.

### 🚀 Define a Heavy Task

```python
import time

def cpu_intensive_task(n):
    print(f"Starting task {n}")
    result = sum(i * i for i in range(10**6))
    time.sleep(2)  # Simulate computation time
    print(f"Task {n} completed")
    return result
```

### 🧩 Create and Start Processes

```python
from multiprocessing import Process
import time

start_time = time.perf_counter()

p1 = Process(target=cpu_intensive_task, args=(1,))
p2 = Process(target=cpu_intensive_task, args=(2,))

p1.start()
p2.start()

p1.join()
p2.join()

end_time = time.perf_counter()
print(f"Total time taken: {end_time - start_time:.2f}s")
```

🔸 Output will show both tasks running concurrently and completing faster than sequential runs.



## 🧰 Advanced Example – Resize Images in Parallel

Use multiprocessing to resize images using `Pillow`.

### 🖼️ Install Pillow First
```bash
pip install pillow
```

### 🛠️ Image Resizing Script

```python
from PIL import Image
import os
from multiprocessing import Pool
import time

IMAGES_DIR = "images"
OUTPUT_DIR = "resized"

def resize_image(filename):
    img_path = os.path.join(IMAGES_DIR, filename)
    with Image.open(img_path) as img:
        resized_img = img.resize((300, 300))
        resized_img.save(os.path.join(OUTPUT_DIR, filename))
    print(f"Resized {filename}")

if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    files = [f for f in os.listdir(IMAGES_DIR) if f.endswith(".jpg")]

    start_time = time.time()

    with Pool(processes=4) as pool:
        pool.map(resize_image, files)

    end_time = time.time()
    print(f"Total time: {end_time - start_time:.2f}s")
```

🔸 This script resizes all `.jpg` images in the `images/` folder using 4 worker processes.



## 🧩 Using `ProcessPoolExecutor` – Cleaner Interface

For a higher-level API, use `ProcessPoolExecutor` from `concurrent.futures`.

```python
from concurrent.futures import ProcessPoolExecutor
import time

def square(n):
    time.sleep(1)  # Simulate CPU-bound task
    return n * n

if __name__ == "__main__":
    numbers = list(range(1, 11))

    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(square, numbers))

    print("Squares:", results)
```


### ✅ Best Practices for Safe Multiprocessing

| Practice | Description |
|---------|-------------|
| 🧠 Prefer `ProcessPoolExecutor` unless you need fine-grained control | Use high-level APIs when possible for simplicity and better error handling |
| 🧮 Use `Pool.map()` or `executor.map()` for homogeneous tasks | For uniform function calls across an iterable — clean and efficient |
| 📁 Ensure input files/dirs exist before starting workers | Prevent processes from failing due to missing resources |
| 📦 Don’t share large objects — it increases IPC overhead | Copying large data between processes is expensive; prefer shared memory or avoid sharing entirely |
| 🧾 Always guard `if __name__ == '__main__'` in Windows | Prevents infinite spawning of subprocesses on Windows |
| 🧩 Use `multiprocessing.Queue` or `Manager` to share state | For inter-process communication (IPC) — safe and effective |
| 🧯 Limit number of processes — usually up to number of CPU cores | Avoid overloading the system; match to available hardware |
| 🧽 Clean up output directories after processing | Especially useful in batch jobs like image resizing or file conversion |
| ⚠️ Avoid shared state where possible | Shared memory adds complexity and potential bugs |
| 🧪 Use logging inside processes for debugging | Helps trace execution flow and identify bottlenecks or failures |
| 🕒 Handle timeouts and hanging processes gracefully | Use `.join(timeout)` or `.terminate()` if needed |
| 🧬 Always close or join() processes explicitly | Ensures all background work completes before main process exits |
| 📝 Use daemon=False and explicit joins unless you want background termination | So processes complete their work before program ends |
| 🧼 Use context managers (`with`) for executors and pools | Automatically handles shutdown and cleanup |
| 🧰 Serialize only picklable data | Not all Python objects can be passed between processes — ensure your data is compatible |




## 📦 Inter-Process Communication (IPC)

When processes need to share data, use:

### 🧾 Shared Memory – `Value`, `Array`

```python
from multiprocessing import Process, Value, Array

def modify_values(counter, names):
    with counter.get_lock():  # Atomic update
        counter.value += 1
    names[0] = "Alice"

if __name__ == '__main__':
    counter = Value('i', 0)
    names = Array('c', b'John Doe')

    p = Process(target=modify_values, args=(counter, names))
    p.start()
    p.join()

    print("Counter:", counter.value)
    print("Name:", names.value.decode())
```

🔸 `Value` and `Array` allow sharing primitive types between processes.



### 🧭 Manager – Share Complex Data

Use `Manager()` for more complex structures like lists or dicts.

```python
from multiprocessing import Process, Manager
import time

def update_data(data_dict):
    time.sleep(1)
    data_dict['status'] = 'completed'

if __name__ == '__main__':
    with Manager() as manager:
        shared_data = manager.dict({'status': 'in progress'})

        p = Process(target=update_data, args=(shared_data,))
        p.start()
        p.join()

        print("Final status:", shared_data['status'])
```

🔸 `manager.dict()` creates a dictionary that can be safely shared between processes.


## 🧪 Real-World Example – Parallel File Hashing

Let’s hash multiple files in parallel using multiprocessing.

```python
import hashlib
from multiprocessing import Process
import os

def hash_file(filename):
    hasher = hashlib.sha256()
    with open(filename, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    print(f"{os.path.basename(filename)}: {hasher.hexdigest()}")

if __name__ == '__main__':
    files = ["file1.txt", "file2.txt", "file3.txt"]

    processes = [Process(target=hash_file, args=(f,)) for f in files]

    for p in processes:
        p.start()
    for p in processes:
        p.join()
```

🔸 This is useful for integrity checks, backups, or batch file processing.



## 🧠 Hidden Notes & Tips

- 🧠 On **Windows**, always protect your entry point with `if __name__ == '__main__':`
- 🧲 Use `Manager()` only when needed — it adds overhead.
- 🧏‍♂️ Use `logging` inside processes for better debugging.
- 🧾 `map()` blocks until all processes complete; `imap()` gives partial results early.
- 📦 Prefer `ProcessPoolExecutor` over raw `Process` for simplicity.
- 🧵 Never assume order of process completion — use `pool.apply_async()` for async behavior.
- 🧩 Use `multiprocessing.Value` or `multiprocessing.Array` for low-overhead shared variables.
- 🧰 Monitor CPU usage during multiprocessing — some tasks may not benefit from it.



## 📌 Summary

| Tool | Purpose |
|------|---------|
| `multiprocessing.Process` | Create and manage individual processes |
| `multiprocessing.Pool` | Manage a fixed number of worker processes |
| `concurrent.futures.ProcessPoolExecutor` | High-level interface for process pools |
| `multiprocessing.Value` / `Array` | Share basic types between processes |
| `Manager` | Share complex objects like dicts and lists |
| `map()` / `apply_async()` | Dispatch tasks to worker processes |
| Best Practice | Use `if __name__ == '__main__'` in Windows |
| Real-world | Batch image processing, data crunching, encryption/hash generation |



🎉 Congratulations! You now understand how to use **Python multiprocessing** to execute CPU-bound tasks in parallel, including:
- Creating and managing `Process` instances
- Using `Pool` for efficient parallelization
- Choosing between shared memory and message passing
- Applying multiprocessing in real applications like image resizing and file hashing

This completes our journey through **Python concurrency and parallelism**!
