from app.Services.AudioManager import AudioManager
from app.config import AUDIO_STORAGE_FOLDER_NAME, AI_URL, REDIS_URL
from app.Services.BatchWhisper import BatchWhisper
from app.Services.JobService import JobService
from app.Services.RedisManager import RedisQueueService

audio_manager = AudioManager(AUDIO_STORAGE_FOLDER_NAME)
whisper_batch_service = BatchWhisper(AI_URL)
job_service = JobService()
redis_queue_service = RedisQueueService(REDIS_URL)

