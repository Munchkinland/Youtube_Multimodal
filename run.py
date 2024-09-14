import os
from app import app

# Configuración
DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() in ['true', '1', 't']
HOST = os.environ.get('FLASK_HOST', '127.0.0.1')
PORT = int(os.environ.get('FLASK_PORT', 5000))

if __name__ == '__main__':
    try:
        app.logger.info(f"Iniciando la aplicación en {HOST}:{PORT}")
        app.run(host=HOST, port=PORT, debug=DEBUG)
    except Exception as e:
        app.logger.error(f"Error al iniciar la aplicación: {str(e)}")