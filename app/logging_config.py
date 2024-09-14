# app/logging_config.py

import logging
from logging.handlers import RotatingFileHandler
import os

def configure_logging(app):
    # Asegúrate de que el directorio de logs existe
    if not os.path.exists('logs'):
        os.mkdir('logs')

    # Configura el logging a archivo
    file_handler = RotatingFileHandler('logs/youtube_qa.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)

    # Configura el logging a consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Añade los handlers al logger de la aplicación
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)
    app.logger.setLevel(logging.INFO)

    app.logger.info('YouTube Q&A startup')