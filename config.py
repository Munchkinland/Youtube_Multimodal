import os
from dotenv import load_dotenv

load_dotenv()  # Esto carga las variables del archivo .env

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
  OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

  @staticmethod
  def init_app(app):
      if not Config.OPENAI_API_KEY:
          raise ValueError("No se ha configurado la clave API de OpenAI. Por favor, configura la variable de entorno OPENAI_API_KEY.")