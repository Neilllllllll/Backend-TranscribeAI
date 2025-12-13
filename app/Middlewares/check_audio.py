from flask import request
from functools import wraps
from app.Helpers.responses import error

def check_audio(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # Vérification si le fichier audio est présent
        if 'audioFile' not in request.files:
            return error("Aucun fichier audio fourni", 400)

        audio_file = request.files['audioFile']

        # Vérifier que le fichier n'est pas vide
        if audio_file.filename == '':
            return error("Le fichier audio est vide", 400)

        # Vérifier le type MIME
        if not audio_file.mimetype.startswith('audio/'):
            return error("Fichier non audio reçu : " + str(audio_file.mimetype), 400)

        # Appel de la fonction route originale
        return f(*args, **kwargs)

    return wrapper