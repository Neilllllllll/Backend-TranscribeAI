from flask import request, jsonify
from ..config.setting import API_KEY

def auth_middleware():
    api_key_sent = request.headers.get("X-API-KEY")
    api_key = API_KEY
    if api_key_sent != api_key:
        # 🛑 Avortement du pipeline → aucun controller n'est exécuté
        return jsonify({"error": "Utilisateur non authorisé"}), 401
