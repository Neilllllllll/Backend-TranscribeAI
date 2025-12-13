import redis
from rq import Queue

# Service pour gérer la file d'attente Redis (FIFO : First In First Out)
class RedisQueueService:
    def __init__(self, redis_url: str, queue_name: str = "job_queue"):
        self.redis = redis.from_url(redis_url)
        self.queue = Queue(queue_name, connection=self.redis)

    # Push simplement l'ID du job dans Redis
    def enqueue_job(self, job_uuid: str):
        self.queue.enqueue(job_uuid)

    def dequeue_job(self):
        pass
