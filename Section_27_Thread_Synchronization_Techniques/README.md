# 🔐 Section 27: Thread Synchronization  
## Preventing Race Conditions in Python Multithreading

🧩 **Learn how to safely manage shared data across multiple threads** using synchronization techniques like `Lock`, `RLock`, `Event`, and `Semaphore`.

This section explains:
- 🧠 What is a race condition?
- 🔒 Using `threading.Lock` to protect critical sections
- 🔁 Reentrancy with `threading.RLock`
- 📢 Coordinating threads with `threading.Event`
- 🚦 Limiting access with `threading.Semaphore`
- 💡 Hidden notes on when to use each technique
- 🧪 Real-world example – synchronized bank account transfers



## 🧠 What You'll Learn

| Concept | Description |
|--------|-------------|
| **Race Condition** | Occurs when two or more threads access shared data unpredictably |
| **`threading.Lock`** | Simple mutual exclusion lock for thread-safe access |
| **`threading.RLock`** | Recursive lock that can be acquired multiple times by the same thread |
| **`threading.Event`** | Signal-based communication between threads |
| **`threading.Semaphore`** | Limits concurrent access to a shared resource |
| **Best Practices** | When to use which sync mechanism and why |



## 🏃‍♂️ Understanding Race Conditions

A **race condition** occurs when two or more threads try to modify a shared variable simultaneously — leading to inconsistent results.

🔹 **Example – Unsafe Counter**
```python
import threading

counter = 0

def unsafe_increment():
    global counter
    for _ in range(1000):
        counter += 1

threads = [threading.Thread(target=unsafe_increment) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)  # ❌ Likely not 10,000 due to race condition
```

🔸 The final value of `counter` will vary because all threads are reading and writing it at the same time.



## 🔒 Using `threading.Lock()` – Mutual Exclusion

Use `Lock` to ensure only one thread can access a critical section at a time.

🔹 **Safe Counter Example**
```python
import threading

counter = 0
lock = threading.Lock()

def safe_increment():
    global counter
    for _ in range(1000):
        with lock:
            counter += 1

threads = [threading.Thread(target=safe_increment) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(counter)  # ✅ Output: 10000
```

🔸 The `with lock:` statement ensures atomic updates to the shared variable.



## 🔁 Reentrant Locks – `threading.RLock`

An `RLock` allows a thread to acquire the same lock multiple times — useful in recursive functions or nested calls.

🔹 **Example – Recursive function with RLock**
```python
import threading

rlock = threading.RLock()

def recursive_func(n):
    with rlock:
        if n <= 0:
            return
        print(f"Entering {n}")
        recursive_func(n - 1)
        print(f"Exiting {n}")

thread = threading.Thread(target=recursive_func, args=(5,))
thread.start()
thread.join()
```

🔸 Without `RLock`, this would cause a deadlock.



## 📢 Coordinating Threads with `threading.Event`

Use `Event` to signal between threads — great for producer/consumer patterns or background task coordination.

🔹 **Example – Background Task Completion Signal**
```python
import threading
from time import sleep

event = threading.Event()

def background_task(event):
    print("Background task started")
    sleep(3)
    print("Background task completed")
    event.set()  # Notify other threads

def dependent_task(event):
    print("Dependent task waiting...")
    event.wait()
    print("Proceeding after signal received")

t1 = threading.Thread(target=background_task, args=(event,))
t2 = threading.Thread(target=dependent_task, args=(event,))

t2.start()
t1.start()

t1.join()
t2.join()
```

🔸 This pattern is ideal for coordinating download-complete → process tasks.


## 🧾 Advanced Example – Event-based File Downloader & Word Counter

Let’s build a system where one thread downloads a file and signals another thread to count words once done.

### 📥 Download Task with Event
```python
from threading import Thread, Event
from urllib.request import urlopen

def download_file(url, event):
    with open('downloaded.txt', 'w') as f:
        response = urlopen(url).read().decode('utf-8')
        f.write(response)
    print("File downloaded.")
    event.set()
```

### 🧮 Count Words Once Downloaded
```python
def count_words(event):
    event.wait()  # Wait until file is ready
    with open('downloaded.txt', 'r') as f:
        content = f.read()
    word_count = len(content.split())
    print(f"Word count: {word_count}")
```

### 🔀 Run in Two Threads
```python
event = Event()

t1 = Thread(target=download_file, args=("https://www.ietf.org/rfc/rfc793.txt", event))
t2 = Thread(target=count_words, args=(event,))

t1.start()
t2.start()

t1.join()
t2.join()
```

🔸 Thread 2 waits until Thread 1 finishes downloading before counting words.



## 🚦 Bounded Access with `threading.Semaphore`

Use semaphores to control how many threads can access a shared resource at once (e.g., API rate limits, database connections).

🔹 **Example – Limited Resource Access**
```python
import threading

semaphore = threading.Semaphore(3)  # Only 3 threads allowed at once

def limited_task(id):
    with semaphore:
        print(f"Task {id} is running")
        sleep(2)
        print(f"Task {id} is done")

threads = [threading.Thread(target=limited_task, args=(i,)) for i in range(6)]

for t in threads:
    t.start()
for t in threads:
    t.join()
```

🔸 Output shows no more than 3 tasks running at the same time.



## 🧰 Real-World Example – Bank Account Transfer System

Ensure thread-safe money transfers between accounts.

### 🧱 Define Account Class
```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            print(f"Deposited ${amount}, New Balance: ${self.balance}")

    def withdraw(self, amount):
        with self.lock:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew ${amount}, New Balance: ${self.balance}")
            else:
                print(f"Insufficient funds. Current Balance: ${self.balance}")
```

### 🔄 Transfer Function
```python
def transfer(from_acc, to_acc, amount):
    from_acc.withdraw(amount)
    to_acc.deposit(amount)

acc1 = BankAccount(1000)
acc2 = BankAccount(500)

threads = [
    threading.Thread(target=transfer, args=(acc1, acc2, 100)) for _ in range(5)
]

for t in threads:
    t.start()
for t in threads:
    t.join()
```

🔸 Ensures consistent state even with multiple concurrent transfers.


## 🧩 Other Synchronization Tools

| Tool | Purpose |
|------|---------|
| `Condition` | Coordinate based on a condition (like `wait()` / `notify()`) |
| `Barrier` | Synchronize threads at a common point |
| `Queue.Queue` | Thread-safe FIFO queue for producer-consumer patterns |
| `Timer` | Delay thread execution by a set time |



## 💡 Hidden Tips & Notes

- 🧠 Use locks **only around shared resources**, not the whole function.
- 🔁 Prefer `RLock` when you might call locking code recursively.
- 📢 Use `Event` to coordinate **start/done** signals between threads.
- 🚦 Use `Semaphore` to simulate connection pools, rate limiting, or batch processing.
- 🧵 Always release locks manually or use `with` context manager.
- 🧾 Avoid deadlocks by always releasing semaphores and events properly.
- 🧱 Never share complex mutable objects across threads without protection.
- 🛑 If possible, prefer immutable data structures or message passing over shared memory.



## 📌 Summary

| Feature | Purpose |
|--------|---------|
| **Race Condition** | Unpredictable behavior when threads modify shared data |
| **`Lock`** | Ensure only one thread modifies data at a time |
| **`RLock`** | Same as `Lock`, but re-entrant (can be locked multiple times) |
| **`Event`** | Signal between threads — `set()`, `wait()` |
| **`Semaphore`** | Control number of threads accessing a resource |
| **Best Practice** | Use `with` statements to avoid forgetting to unlock |



🎉 Congratulations! You now understand how to **prevent race conditions and synchronize threads effectively** in Python using tools like `Lock`, `RLock`, `Event`, and `Semaphore`.

Next up: 🧬 **Section 28: Multiprocessing** – learn how to run CPU-bound tasks in parallel using Python's `multiprocessing` module.
