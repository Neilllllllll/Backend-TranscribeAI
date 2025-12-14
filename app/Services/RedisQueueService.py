import redis

# Service pour gérer une file Redis simple (FIFO)
class RedisQueueService:
    def __init__(self, redis_url: str, queue_name: str = "job_queue"):
        self.redis = redis.Redis.from_url(redis_url, decode_responses=True)
        self.queue_name = queue_name

    # Enfile un job_id
    def enqueue_job(self, job_id: str):
        self.redis.lpush(self.queue_name, job_id)
        return job_id

    # Défile un job (bloquant)
    def pop_job_blocking(self) -> str:
        _, job_id = self.redis.brpop(self.queue_name)
        return job_id

    # Voir le contenu de la queue (debug)
    def list_jobs(self):
        return self.redis.lrange(self.queue_name, 0, -1)
