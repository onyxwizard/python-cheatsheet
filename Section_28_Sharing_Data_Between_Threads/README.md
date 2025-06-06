# 🧾 Section 28: Sharing Data Between Threads  
## Using Thread-Safe Queues in Python

📦 **Learn how to safely share data between threads using the `queue.Queue` module**, a built-in thread-safe structure that handles all locking and synchronization for you.

This section explains:
- 🧠 What is a thread-safe queue?
- 📥 How to add (`put()`) and retrieve (`get()`) items
- ⏳ Blocking, timeouts, and non-blocking operations
- 🧰 Managing task completion with `task_done()` and `join()`
- 💡 Hidden notes and best practices for safe multithreaded communication
- 🧪 Real-world example – Producer/Consumer pattern for concurrent processing



## 🧠 What You'll Learn

| Concept | Description |
|--------|-------------|
| **Thread-safe Queue** | Built-in queue that automatically manages locks |
| **Producer-Consumer Pattern** | One thread produces data, another consumes it |
| **`put()` method** | Adds an item to the queue |
| **`get()` method** | Retrieves an item from the queue |
| **`task_done()`** | Marks an item as processed |
| **`join()` method** | Waits until all tasks are done |
| **Queue size methods** | `qsize()`, `empty()`, `full()` |
| **Best Practices** | Use daemon threads, manage timeouts, avoid deadlocks |



## 🧱 Introduction to `queue.Queue`

The `queue.Queue` class provides a **thread-safe FIFO (First-In-First-Out)** queue ideal for sharing data across threads without worrying about race conditions.

🔹 **Basic Usage**
```python
from queue import Queue
from threading import Thread
import time

def producer(queue):
    for i in range(1, 6):
        print(f"Producing item {i}")
        queue.put(i)
        time.sleep(0.5)

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:
            break
        print(f"Consuming item {item}")
        time.sleep(1)
        queue.task_done()

queue = Queue()

producer_thread = Thread(target=producer, args=(queue,))
consumer_thread = Thread(target=consumer, args=(queue,), daemon=True)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
queue.join()
```

🔸 This ensures **safe data exchange** even when multiple threads read or write simultaneously.



## 📥 Adding Items with `put()`

Use `.put(item)` to insert an item into the queue.

🔹 **Blocking Example – Wait Until Space Available**
```python
queue.put("Data Packet")
```

🔹 **Non-blocking Example – Raise Exception if Full**
```python
try:
    queue.put("Urgent", block=False)
except Queue.Full:
    print("Queue full — unable to add item")
```

🔹 **With Timeout – Wait up to N seconds**
```python
try:
    queue.put("Urgent", timeout=2)
except Queue.Full:
    print("Timed out waiting to put item")
```



## 📤 Retrieving Items with `get()`

Use `.get()` to retrieve and remove an item from the queue.

🔹 **Blocking Example – Wait Until Item Is Available**
```python
item = queue.get()
print(f"Got item: {item}")
```

🔹 **Non-blocking Example – Raise if No Item**
```python
try:
    item = queue.get(block=False)
except Queue.Empty:
    print("No item available in queue")
```

🔹 **With Timeout – Wait up to N seconds**
```python
try:
    item = queue.get(timeout=3)
except Queue.Empty:
    print("No item retrieved within 3 seconds")
```



## 🔄 Mark Task as Done – `task_done()`

Call `queue.task_done()` after retrieving and processing an item to inform the queue that the task is complete.

🔹 **Example – Safe Task Processing**
```python
def consumer(queue):
    while True:
        item = queue.get()
        if item == "STOP":
            break
        print(f"Processing {item}")
        time.sleep(1)
        queue.task_done()
```

🔸 Always call `task_done()` if you're using `queue.join()` later.



## 🧩 Wait for All Tasks to Complete – `join()`

The `queue.join()` method blocks until all items in the queue have been received and processed.

🔹 **Example – Main waits until all items are handled**
```python
queue = Queue()

producer = Thread(target=producer_func, args=(queue,))
consumer = Thread(target=consumer_func, args=(queue,), daemon=True)

producer.start()
consumer.start()

producer.join()
queue.join()
print("All tasks completed.")
```

🔸 This ensures your program doesn't exit before background threads finish their work.



## 🧰 Real-World Example – Concurrent Web Scraper

Let’s build a web scraper where one thread adds URLs to a queue and others process them concurrently.

### 🌐 Step 1: Define Producer Function

```python
import requests
from queue import Queue
from threading import Thread
import time

def url_producer(queue, urls):
    for url in urls:
        print(f"Queuing URL: {url}")
        queue.put(url)
        time.sleep(0.5)  # Simulate slow input
```

### 🕸️ Step 2: Define Consumer Function

```python
def url_consumer(queue):
    while True:
        try:
            url = queue.get(timeout=2)  # Wait up to 2s
            response = requests.get(url)
            print(f"Fetched {url} - Status {response.status_code}")
        except Queue.Empty:
            print("No more URLs to fetch.")
            return
        finally:
            queue.task_done()
```

### 🔀 Step 3: Run with Multiple Consumers

```python
urls = [
    'https://example.com',
    'https://httpbin.org/get',
    'https://jsonplaceholder.typicode.com'
] * 3

queue = Queue(maxsize=5)

# Start producer
producer_thread = Thread(target=url_producer, args=(queue, urls))

# Start consumers
consumer_threads = [Thread(target=url_consumer, args=(queue,), daemon=True) for _ in range(3)]

producer_thread.start()
for t in consumer_threads:
    t.start()

producer_thread.join()
queue.join()
print("All URLs fetched and processed.")
```

🔸 This demonstrates a **scalable architecture** where producers and consumers run independently and efficiently.



## 🧮 Queue Size & State Methods

| Method | Purpose |
|--------|---------|
| `qsize()` | Returns approximate number of items in the queue |
| `empty()` | Returns `True` if queue is empty |
| `full()` | Returns `True` if queue is at maxsize |

🔹 **Example – Monitor Queue Status**
```python
while not queue.empty():
    print(f"Remaining items: {queue.qsize()}")
    time.sleep(1)
```

🔸 These methods are useful for monitoring but should be used carefully — they provide approximate info since other threads may modify the queue.


## 🧩 Advanced Use Case – Dynamic Worker Pool

Create a dynamic worker pool that pulls from a shared queue.

```python
def worker(queue):
    while True:
        try:
            job = queue.get(timeout=2)
            print(f"Worker processing job {job}")
            time.sleep(1)
            queue.task_done()
        except Queue.Empty:
            return

job_queue = Queue()

# Add jobs
for job_id in range(10):
    job_queue.put(job_id)

# Create and start workers
workers = []
for _ in range(4):
    w = Thread(target=worker, args=(job_queue,), daemon=True)
    workers.append(w)
    w.start()

# Wait for all jobs to complete
job_queue.join()
print("All jobs completed.")
```

🔸 Each worker runs in parallel, pulling from the same queue.



## 🧨 Best Practices & Hidden Notes

| Practice | Description |
|---------|-------------|
| 🧠 Prefer `queue.Queue` over manual synchronization | It's already thread-safe |
| 🧩 Limit queue size with `maxsize=N` | Prevent memory overload |
| 📦 Use `None` or sentinel value to signal end | Like `queue.put(None)` to stop consumers |
| 🛑 Avoid infinite blocking | Always use `timeout` or `block=False` when necessary |
| 🧯 Use daemon threads for consumers | So program can exit cleanly |
| 🧼 Call `task_done()` after every `get()` | Otherwise `queue.join()` will hang |
| 📈 Scale with thread pools | Don’t create too many threads manually |
| 🧪 Monitor queue state | Use `qsize()`, `empty()`, and `full()` for debugging |



## 📌 Summary

| Feature | Purpose |
|--------|---------|
| `queue.Queue()` | Thread-safe FIFO queue for inter-thread communication |
| `put()` | Insert items into the queue |
| `get()` | Retrieve items from the queue |
| `task_done()` | Inform queue that item was processed |
| `join()` | Block until all items are processed |
| Daemon Threads | Allow main thread to exit without waiting |
| Sentinel Values | Signal threads to stop gracefully |
| Best Practices | Use timeouts, monitor queue state, scale smartly |



🎉 Congratulations! You now understand how to **share data between threads safely using `queue.Queue`**, including:
- How to produce and consume items
- How to wait for all tasks to finish
- How to control queue size and handle full/empty states
- Best practices for building scalable, thread-safe systems

Next up: 🧬 **Section 29: Multiprocessing** – learn how to run CPU-bound tasks in parallel using the `multiprocessing` module.
