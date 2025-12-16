from flask import request, current_app
from functools import wraps
from app.Helpers.responses import error
from pydub.utils import mediainfo
import io

def check_audio(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # Vérifie la durée minimale de l'audio pour le mode batch
        MIN_DURATION_SEC = current_app.config.get("MIN_DURATION_SEC_BATCH_MODE", 1)
        ALLOWED_FORMATS = current_app.config.get("FORMAT_AUDIO_ALLOWED", {"wav", "mp3", "ogg", "m4a"})
        # Vérifier présence du fichier
        if 'audioFile' not in request.files:
            return error("Aucun fichier audio fourni", 400)

        audio_file = request.files['audioFile']

        if audio_file.filename == '':
            return error("Le fichier audio est vide", 400)

        if not audio_file.mimetype.startswith("audio/"):
            return error(f"Fichier non audio reçu (MIME={audio_file.mimetype})", 400)

        # Lire le fichier en mémoire
        audio_bytes = io.BytesIO(audio_file.read())

        try:
            info = mediainfo(audio_bytes)
        except Exception as e:
            return error(f"Impossible de lire le fichier audio : {e}", 400)

        # Vérifier le format
        audio_format = info.get("format_name", "").lower()
        if audio_format not in ALLOWED_FORMATS:
            return error(f"Format audio non autorisé ({audio_format})", 415)

        # Vérifier la durée
        duration = float(info.get("duration", 0))
        if duration < MIN_DURATION_SEC:
            return error(f"Durée trop courte ({duration:.2f} s)", 400)

        # Remettre le curseur pour réutilisation
        audio_file.seek(0)

        # ✅ Tout est OK
        return f(*args, **kwargs)

    return wrapper
