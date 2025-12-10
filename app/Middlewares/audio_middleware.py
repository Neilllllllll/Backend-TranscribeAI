from flask import request
from ..Helpers.responses import error

def audio_middleware():
    # check if 
    if 'audioFile' not in request.files:
        return error("Aucun fichier audio fourni", 400)

    audio_file = request.files['audioFile']

    # Vérifie que le fichier n'est pas vide
    if audio_file.filename == '':
        error("Le fichier audio est vide", 400)

    # Vérifie le type MIME pour s'assurer que c'est bien un fichier audio
    if not audio_file.mimetype.startswith('audio/'):
        return error("Fichier non audio reçu : " + str(audio_file.mimetype), 400)

    # Si tout est OK, on continue normalement
    print(f"Fichier audio reçu : {audio_file.filename} ({audio_file.mimetype})")
