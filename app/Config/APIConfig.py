from app.Config import BaseConfig
import os 
# Configuration spécifique à l'API Flask
class APIConfig(BaseConfig.BaseConfig):
    FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:3000")
    PORT = 5000
    HOST = "0.0.0.0"

