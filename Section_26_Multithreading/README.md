# 🧵 Section 26: Multithreading  
## Building Concurrent Programs in Python

🔁 **Learn how to use multithreading in Python** to build concurrent applications that improve performance for I/O-bound tasks.

This section covers:
- 🔍 The difference between processes and threads
- 📦 Using the `threading` module to create and manage threads
- 🔄 Extending the `Thread` class to pass arguments and return values
- 🧰 Thread pools using `ThreadPoolExecutor`
- 🚀 Real-world example – multi-threaded web scraping or file processing
- 💡 Hidden notes and best practices for safe, efficient threading



## 🧠 What You'll Learn

| Concept | Description |
|--------|-------------|
| **Processes vs Threads** | Understand memory sharing and execution differences |
| **`threading.Thread`** | Create and start threads manually |
| **Passing Arguments** | Send data to a thread function |
| **Returning Values** | Extend `Thread` to store results |
| **Thread Pool Executor** | Use `ThreadPoolExecutor` for managing multiple threads efficiently |
| **I/O-bound vs CPU-bound** | When to use threads vs multiprocessing |
| **Daemon Threads** | Background threads that don't block program exit |
| **Best Practices** | Avoid shared state, use locks when needed |



## 🧱 Introduction to Threading in Python

### 🔍 Process vs Thread

| Criteria            | Process                        | Thread                         |
|---------------------|--------------------------------|--------------------------------|
| Memory Sharing      | Not shared                     | Shared within the same process |
| Communication       | Inter-process communication    | Easy via shared memory         |
| Overhead            | High (separate memory space)   | Low                            |
| Start Time          | Slower                         | Faster                         |
| Interruptability    | Yes                            | No                             |
| Ideal For           | CPU-bound tasks                | I/O-bound tasks                |

🔹 A **process** is an independent instance of a running program. <br>
🔹 A **thread** is a unit of execution inside a process — all threads in a process share the same memory space.



## 📌 Using the `threading` Module

Python provides a built-in `threading` module to work with threads.

### ✅ Basic Thread Example

```python
import threading
from time import perf_counter

def task():
    print("Starting a task...")
    print("done")

start_time = perf_counter()

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

end_time = perf_counter()
print(f'It took {end_time - start_time:.2f} seconds to complete.')
```

🔸 This starts two threads and waits for both to finish before measuring total time.



## 🔁 Passing Arguments to Threads

You can pass arguments to the target function using `args` or `kwargs`.

### ✅ Example – Task with ID

```python
def task(id):
    print(f'Starting task {id}...')
    print('done')

t1 = threading.Thread(target=task, args=(1,))
t2 = threading.Thread(target=task, args=(2,))
```

🔸 Each thread runs the same function but with different IDs.


## 📥 Returning Values from a Thread

Since `Thread` doesn't return a value directly, you can extend it and store the result.

### 🛠️ Custom Thread Class with Result

```python
class MyThread(threading.Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.result = None

    def run(self):
        print(f"Task {self.id} started")
        self.result = f"Result from task {self.id}"

# Usage
t1 = MyThread(1)
t2 = MyThread(2)

t1.start()
t2.start()

t1.join()
t2.join()

print(t1.result)
print(t2.result)
```

🔸 This pattern allows you to retrieve results safely after threads complete.



## 🧩 Real-World Example – Multi-threaded File Text Replacement

Let’s say you want to replace text in multiple files concurrently.

### 🧱 Define Thread-safe Function

```python
def replace_in_file(filename, old_text, new_text):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        
        content = content.replace(old_text, new_text)

        with open(filename, 'w') as f:
            f.write(content)

        print(f"Processed {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
```

### 🔁 Run in Multiple Threads

```python
files = ['file1.txt', 'file2.txt', 'file3.txt']

threads = []
for file in files:
    t = threading.Thread(
        target=replace_in_file,
        args=(file, "old", "new")
    )
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

🔸 This speeds up operations like batch file editing, log parsing, or any I/O-heavy task.



## 🧰 Thread Pools with `ThreadPoolExecutor`

Use `ThreadPoolExecutor` from `concurrent.futures` for easier management of many threads.

### ✅ Basic Thread Pool Example

```python
from concurrent.futures import ThreadPoolExecutor

def fetch_url(url):
    import requests
    response = requests.get(url)
    return response.status_code

urls = [
    'https://example.com',
    'https://httpbin.org/get',
    'https://jsonplaceholder.typicode.com'
]

with ThreadPoolExecutor() as executor:
    results = list(executor.map(fetch_url, urls))

print(results)  # [200, 200, 200]
```

🔸 `executor.map()` handles launching threads and collecting results automatically.



## 🚀 Advanced Example – Web Scraper with Thread Pool

Build a multi-threaded scraper to extract titles from multiple websites.

```python
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import requests
from lxml import html

class WebsiteScraper(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.title = None

    def run(self):
        try:
            response = requests.get(self.url)
            tree = html.fromstring(response.content)
            self.title = tree.xpath('//title/text()')[0].strip()
        except Exception as e:
            self.title = f"Error: {str(e)}"

sites = [
    'https://example.com',
    'https://httpbin.org',
    'https://jsonplaceholder.typicode.com'
]

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(fetch_and_scrape, site) for site in sites]
    for future in futures:
        print(future.result())
```

🔸 Uses `lxml` for HTML parsing and `requests` for HTTP calls.



## 🧷 Daemon Threads – Background Tasks

Use daemon threads for background tasks that should not prevent the program from exiting.

```python
def background_task():
    while True:
        print("Running in background...")
        time.sleep(1)

bt = threading.Thread(target=background_task, daemon=True)
bt.start()

time.sleep(3)
print("Main thread done.")
```

🔸 Since `daemon=True`, the program will exit even if this thread is still running.



## 🧭 Best Practices & Notes

| Practice | Description |
|---------|-------------|
| 🧪 Prefer threads for I/O-bound tasks | Like reading/writing files, network calls |
| ⚖️ Avoid threads for CPU-bound tasks | Use `multiprocessing` instead |
| 🧩 Limit number of threads | Too many threads can degrade performance |
| 📦 Use `ThreadPoolExecutor` for large numbers of tasks | Better than manually creating threads |
| 🔐 Protect shared resources | Use `threading.Lock()` if accessing shared data |
| 🧯 Don’t assume order | Threads run concurrently, not necessarily in sequence |
| 🧼 Always call `.join()` | Unless you're using daemon threads |
| 📝 Log errors and progress | Threads can make debugging harder |
| 🧠 Know when to use daemon threads | For non-critical background tasks |


## 🧬 Advanced Pattern – Thread with Return Value

A reusable way to get return values from threads:

```python
from threading import Thread

class ReturnValueThread(Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.result = None

    def run(self):
        try:
            if self._target:
                self.result = self._target(*self._args, **self._kwargs)
        finally:
            del self._target, self._args, self._kwargs

# Usage
def compute(x):
    return x * x

t = ReturnValueThread(target=compute, args=(5,))
t.start()
t.join()
print(t.result)  # Output: 25
```


## 🧠 Hidden Tips & Notes

- 🧩 The Global Interpreter Lock (GIL) prevents true parallelism in CPython — so threads won’t speed up CPU-bound tasks.
- 📦 Threads are useful for waiting on external resources (like APIs, databases, files).
- 🧾 Use `threading.current_thread().name` or `threading.get_ident()` to debug which thread is executing what.
- 🧹 Always clean up resources used by threads — especially open files or network connections.
- 🧯 Never rely on thread execution order unless explicitly synchronized.
- 🧠 Use `map()` over `submit()` when dealing with homogeneous functions across many inputs.
- 📊 Measure performance improvements — sometimes single-threaded code is faster due to overhead.



## 📌 Summary

| Feature | Purpose |
|--------|---------|
| `threading.Thread` | Create and manage individual threads |
| `target`, `args`, `kwargs` | Pass functions and arguments to threads |
| `.start()` and `.join()` | Start and wait for thread completion |
| Daemon threads | Background threads that don't block program exit |
| `ThreadPoolExecutor` | Efficiently manage many threads |
| `submit()` and `map()` | Dispatch tasks to thread pool |
| Extend `Thread` | Store return values and custom logic |
| Best Practices | Use for I/O-bound tasks, avoid for CPU-bound ones |

🎉 Congratulations! You now understand how to use **multithreading in Python**, including:
- Creating and managing threads
- Passing arguments and returning values
- Using thread pools with `ThreadPoolExecutor`
- Writing real-world applications like scrapers and bulk file processors
- Following best practices for safe and performant concurrency

Next up: 🧱 **Section 27: Multiprocessing** – learn how to run CPU-bound tasks in parallel using Python's `multiprocessing` module.
