# 🧵 Section 30: Async IO (asyncio)  
## Writing Asynchronous Python Programs

⚡ **Learn how to write asynchronous programs using the `asyncio` module**, a powerful library for managing **I/O-bound tasks** like network calls, file handling, or system-level operations — all without blocking the main thread.

This section explains:
- 🔍 What is asynchronous programming and when to use it
- 📦 Define `async` functions and `await` results
- 🔄 Run multiple coroutines concurrently
- ⏳ Use `asyncio.sleep()` to simulate async I/O
- 💡 Hidden notes and best practices for writing clean async code
- 🧪 Real-world example – concurrent web requests with `aiohttp`



## 🧠 What You'll Learn

| Concept | Description |
|--------|-------------|
| **Asynchronous IO (`asyncio`)** | Handle many I/O-bound tasks in parallel |
| **`async def`** | Define a coroutine that can be run asynchronously |
| **`await`** | Wait for a coroutine to complete |
| **`asyncio.run()`** | Start and manage an async event loop |
| **`asyncio.create_task()`** | Schedule a coroutine to run in the event loop |
| **`asyncio.gather()`** | Run multiple tasks and wait for all to finish |
| **Best Practices** | When to use async over threads or processes |



## ⚙️ Introduction to Async IO in Python

Python’s `asyncio` module allows you to write **non-blocking** programs that perform **multiple I/O-bound tasks** at once — ideal for:
- Web scraping
- API clients
- Network servers
- Concurrent file reading/writing
- Long-running background jobs

🔹 **Example – Basic Async Function**
```python
import asyncio

async def greet(name):
    print(f"Hello, {name}")
    await asyncio.sleep(1)
    print(f"Goodbye, {name}")

asyncio.run(greet("Alice"))
```

🔸 The `await` keyword tells Python to pause execution until the awaited task completes.



## 📌 Define and Run Coroutines

### ✅ Defining Coroutines

Use `async def` to define a function that returns a **coroutine object** — not executed immediately.

🔹 **Example – Multiple Coroutines**
```python
async def task_one():
    print("Task One Started")
    await asyncio.sleep(2)
    print("Task One Completed")

async def task_two():
    print("Task Two Started")
    await asyncio.sleep(1)
    print("Task Two Completed")
```

### ✅ Running Coroutines

You must run coroutines inside an event loop. Use `asyncio.run()` in Python 3.7+:

```python
asyncio.run(task_one())
```

Or run them concurrently using `create_task()`:

```python
async def main():
    t1 = asyncio.create_task(task_one())
    t2 = asyncio.create_task(task_two())
    await t1
    await t2

asyncio.run(main())
```

🔸 Output will show overlapping execution due to concurrency.


## 🔄 Awaitable Objects

Any object that can be used in an `await` expression is called an **awaitable**.

They include:
- Coroutines
- Tasks (created via `create_task()`)
- Futures (used internally by asyncio)

🔹 **Example – Using `await` on a Task**
```python
async def fetch_data():
    await asyncio.sleep(1)
    return "Data"

async def main():
    task = asyncio.create_task(fetch_data())
    result = await task
    print("Result:", result)

asyncio.run(main())  # Result: Data
```



## 🧰 Real-World Example – Fetching from Multiple URLs

Let’s build a program that fetches data from multiple URLs concurrently using `aiohttp`.

### 🧱 Step 1: Install aiohttp
```bash
pip install aiohttp
```

### 🛠️ Step 2: Define Coroutine for Fetching
```python
import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        content = await response.text()
        print(f"Fetched {url} → {len(content)} bytes")
        return content

async def main(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        print(f"Fetched {len(results)} pages.")

urls = [
    'https://example.com',
    'https://httpbin.org/get',
    'https://jsonplaceholder.typicode.com'
]

asyncio.run(main(urls))
```

🔸 This shows how to make **multiple HTTP requests concurrently** — faster than sequential or even threaded approaches.



## ⏳ Working with Delays and Timeouts

Use `await asyncio.sleep(n)` to simulate I/O delays.

🔹 **Example – Delayed Greeting**
```python
async def delayed_greet(name, delay):
    print(f"{name} is waiting {delay} seconds...")
    await asyncio.sleep(delay)
    print(f"Hello, {name}!")

async def main():
    asyncio.create_task(delayed_greet("Alice", 1))
    asyncio.create_task(delayed_greet("Bob", 2))
    asyncio.create_task(delayed_greet("Charlie", 0.5))
    await asyncio.sleep(3)

asyncio.run(main())
```

🔸 Tasks run concurrently — Charlie finishes first, then Alice, then Bob.



## 🧩 Advanced Example – Concurrent File Reader

Read multiple files asynchronously using `aiofiles`.

### 📁 Step 1: Install aiofiles
```bash
pip install aiofiles
```

### 📖 Step 2: Read Files Without Blocking
```python
import asyncio
import aiofiles

async def read_file(filename):
    async with aiofiles.open(filename, mode='r') as f:
        content = await f.read()
        print(f"Read {filename}: {len(content)} characters")
        return content

async def main():
    files = ["file1.txt", "file2.txt", "file3.txt"]
    tasks = [read_file(f) for f in files]
    await asyncio.gather(*tasks)

asyncio.run(main())
```

🔸 Each file is read without blocking others — great for batch processing large logs or config files.



## 🧯 Best Practices & Notes

| Practice | Description |
|---------|-------------|
| 🧠 Use `async/await` instead of callbacks | Cleaner and easier to maintain |
| 📦 Prefer `asyncio.run()` in Python 3.7+ | It manages the event loop automatically |
| 🔄 Use `create_task()` to schedule work | For true concurrency |
| 🧾 Don’t mix sync and async calls | Can cause performance bottlenecks |
| 🕒 Always use `await` with coroutines | Otherwise they won't execute |
| 🧲 Use `gather()` to collect results from multiple tasks | Clean way to await all results |
| 🧽 Avoid long-running CPU-bound logic inside coroutines | Use multiprocessing if needed |
| 🧩 Use async libraries like `aiohttp`, `aiofiles`, `asyncpg` | Maximize async benefits |
| 🧾 Add timeouts to prevent hanging | `await asyncio.wait_for(task, timeout=5)` |
| 🧠 Use `async for` or `async with` when working with async iterators and context managers |



## 🧬 Using `asyncio` with Threads

Sometimes you need to integrate async with threading — for example, calling async code from a GUI app.

🔹 **Example – Run async code inside a thread**
```python
import asyncio
import threading

def start_async_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

loop = asyncio.new_event_loop()
thread = threading.Thread(target=start_async_loop, args=(loop,), daemon=True)
thread.start()

async def add_to_queue(item):
    await asyncio.sleep(1)
    print(f"Processed {item}")

future = asyncio.run_coroutine_threadsafe(add_to_queue("test"), loop)
future.result()  # Wait for async result
```

🔸 This pattern is useful in apps where the main thread runs a different loop (e.g., Tkinter or Flask).



## 🧪 Real-World Use Case – Async Database Query Pool

Let’s say you want to query multiple database endpoints in parallel.

### 🧱 Sample Async DB Query Function
```python
import asyncio
import random

async def query_db(db_name):
    delay = random.uniform(0.5, 2)
    print(f"Querying {db_name} ({delay:.2f}s)")
    await asyncio.sleep(delay)
    print(f"Finished querying {db_name}")
    return f"Results from {db_name}"

async def main():
    db_list = ["users", "orders", "inventory", "logs"]
    tasks = [query_db(db) for db in db_list]
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)

asyncio.run(main())
```

🔸 Simulates querying multiple databases concurrently — real use cases might involve actual async drivers like `asyncpg` or `motor`.



## 💡 Hidden Tips & Notes

- 🧠 On Windows, you may need to set the event loop policy:
  ```python
  asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  ```
- 🧱 Always wrap your top-level async logic inside `main()` and call `asyncio.run(main())`
- 📦 Prefer `create_task()` over `ensure_future()` or manual scheduling
- 🧾 Use `await asyncio.sleep(0)` to yield control to other coroutines (for cooperative multitasking)
- 🧐 Use `asyncio.all_tasks()` and `asyncio.current_task()` for debugging running tasks
- 🧵 Use `run_coroutine_threadsafe()` to interact with async code from threads
- 🧩 Use `asyncio.Queue` for producer/consumer patterns within async
- 🧾 Use `asyncio.TimeoutError` and `wait_for()` to avoid infinite waits



## 📌 Summary

| Feature | Purpose |
|--------|---------|
| `async def` | Define a coroutine |
| `await` | Execute and wait for a coroutine |
| `asyncio.run()` | Start and manage the event loop |
| `create_task()` | Schedule a coroutine for execution |
| `gather()` | Collect results from multiple tasks |
| `sleep()` | Simulate I/O delays |
| `aiohttp`, `aiofiles` | External async libraries for real-world use |
| Best Practice | Don’t block inside coroutines — keep I/O non-blocking |



🎉 Congratulations! You now understand how to write **asynchronous programs in Python** using `asyncio`, including:
- How to define and run coroutines
- How to schedule and await multiple tasks
- Real-world applications like web scraping and file reading
- Best practices for avoiding blocking calls and managing timeouts

This completes our full roadmap from **Python fundamentals to advanced topics like OOP, metaprogramming, and concurrency models**!
