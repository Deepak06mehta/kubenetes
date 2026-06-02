import redis
import psycopg2
import time

redis_client = redis.Redis(
    host='redis-service',
    port=6379
)

while True:
    try:
        print("Worker running")
        time.sleep(10)
    except Exception:
        pass