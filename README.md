# Redis-Queue-Mini-Project(Mini Project)

A simple Redis-backed task queue built with Python to understand how real backend systems handle **durable background jobs**.

This project demonstrates why **in-memory queues fail** and how Redis is used as a **persistent, shared queue** in production systems.

---

## 🚀 Features

- FIFO task processing using Redis Lists
- Producer–worker architecture
- Tasks persist even if the worker process restarts
- Simple, minimal code focused on core concepts

---

## 🧠 Why this project?

In-memory queues (lists, deques, dicts) lose all data when a server restarts.

This project explores:
- How Redis acts as a durable queue
- How background job systems survive crashes
- How production systems avoid losing tasks

---

## 🛠 Tech Stack

- Python 3
- Redis

---

## 🧪 Testing durability

1- Start worker.py
2- Add tasks using producer.py
3- Stop the worker
4- Restart the worker

✅ Tasks are not lost, proving Redis persistence.

---

## 🔍 Key Learnings

- Redis Lists can be used as reliable queues
- Background jobs should not rely on in-memory storage
- Redis enables durability, concurrency safety, and scalability

---

## 🔜 Next Steps

- Add task metadata using Redis Hashes
- Add retries and failure handling
- Integrate Redis into a FastAPI background job system with per-user concurrency limits

