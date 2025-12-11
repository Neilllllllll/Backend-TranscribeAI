from flask import request
from ..Helpers.responses import error

def checkIsAudio():
    # Check if the 'audioFile' key is here
    if 'audioFile' not in request.files:
        return error("Aucun fichier audio fourni", 400)

    audio_file = request.files['audioFile']

    # Check si the file isn't empty
    if audio_file.filename == '':
        return error("Le fichier audio est vide", 400)

    # check the meta data
    if not audio_file.mimetype.startswith('audio/'):
        return error("Fichier non audio reçu : " + str(audio_file.mimetype), 400)

    print(f"Fichier audio reçu : {audio_file.filename} ({audio_file.mimetype})")

