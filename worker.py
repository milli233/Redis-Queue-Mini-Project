import redis
import time

r = redis.Redis(decode_responses=True)

while True:
    task = r.rpop("task_queue")
    if task:
        print("Processing:", task)
        time.sleep(2)
        print("Done:", task)
    else:
        time.sleep(1)
