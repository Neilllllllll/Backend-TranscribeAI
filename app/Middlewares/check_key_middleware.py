from flask import request, jsonify
from ..config.setting import X_API_KEY

def check_key_middleware():
    if request.method == "OPTIONS":
        return '', 200
    
    api_key_sent = request.headers.get("X-API-KEY")
    api_key = X_API_KEY
    if api_key_sent != api_key:
        # 🛑 Avortement du pipeline → aucun controller n'est exécuté
        return jsonify({"error": "Utilisateur non authorisé"}), 401
