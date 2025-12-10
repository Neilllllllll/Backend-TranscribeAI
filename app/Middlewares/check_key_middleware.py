from flask import request, jsonify
from ..Helpers.responses import success, error
from ..config.setting import X_API_KEY

def check_key_middleware():
    if request.method == "OPTIONS":
        return success()
    
    api_key_sent = request.headers.get("X-API-KEY")
    api_key = X_API_KEY
    if api_key_sent != api_key:
        # 🛑 Avortement du pipeline → aucun controller n'est exécuté
        return error("error: Utilisateur non authorisé", 401)
