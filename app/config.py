import os 

AI_URL = os.getenv('AI_URL', 'http://localhost:5001/api/transcribe')
DB_URL = os.getenv('DB_URL', 'sqlite:///app.db')
FRONTEND_URL = os.getenv('FRONTEND_URL', 'http://localhost:3000')
AUDIO_STORAGE_PATH = os.getenv('AUDIO_STORAGE_PATH', './audio_files')
WHISPER_SERVICE_URL = os.getenv('WHISPER_SERVICE_URL', 'http://localhost:5001/api/transcribe')
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
DEBUG = os.getenv('DEBUG', 'True') == 'True'
