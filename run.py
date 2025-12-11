# Charge les variables d'environnement
from dotenv import load_dotenv
load_dotenv(".env.dev")

from app import create_app
from flask_socketio import SocketIO

# Lance l'app
if __name__ == "__main__":
    app = create_app()
    socketio = SocketIO(app)
    socketio.run(app)