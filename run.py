# Charge les variables d'environnement
from dotenv import load_dotenv
load_dotenv(".env.dev")

from app import create_app
import os

# Créer l'app
app = create_app()
# Lance l'app 
if __name__ == "__main__":
    debug = os.getenv("DEBUG")
    port = os.getenv("PORT")
    app.run(debug=debug, host='0.0.0.0', port=port)