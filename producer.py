import redis
import uuid

r = redis.Redis(decode_responses=True)

task_id = str(uuid.uuid4())
r.lpush("task_queue", task_id)

print("Task added:", task_id)
