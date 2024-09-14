# app/__init__.py

from flask import Flask
from app.logging_config import configure_logging

app = Flask(__name__)
configure_logging(app)

from app import routes