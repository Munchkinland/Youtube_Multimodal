import os
import glob
import yt_dlp as youtube_dl
import whisper
import openai
import subprocess
from app import app

# Configuración
AUDIO_FILE = 'audio.mp3'
FFMPEG_PATH = r'C:\ffmpeg\ffmpeg-2024-08-28-git-b730defd52-full_build\bin'

# Añadir FFmpeg al PATH
os.environ["PATH"] += os.pathsep + FFMPEG_PATH

def download_audio(youtube_url):
    """Descarga el audio de un video de YouTube."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'audio',  # Quitamos la extensión completamente
        'ffmpeg_location': FFMPEG_PATH,
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        
        # Buscar el archivo de audio creado
        audio_files = glob.glob('audio.*')
        if audio_files:
            actual_file = audio_files[0]
            os.rename(actual_file, AUDIO_FILE)
            app.logger.info(f"Audio descargado exitosamente: {AUDIO_FILE}")
            return os.path.abspath(AUDIO_FILE)
        else:
            app.logger.error("No se encontró el archivo de audio después de la descarga")
            return None
    except Exception as e:
        app.logger.error(f"Error downloading audio: {e}")
        return None

def transcribe_audio(audio_file):
    """Transcribe el audio usando Whisper."""
    # Verificar si FFmpeg está disponible
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        app.logger.error("FFmpeg no está disponible. Por favor, verifica la instalación.")
        raise RuntimeError("FFmpeg no está disponible. Por favor, verifica la instalación.")
    
    app.logger.info("Iniciando transcripción con modelo tiny de Whisper")
    model = whisper.load_model("tiny")
    result = model.transcribe(os.path.abspath(audio_file))
    app.logger.info("Transcripción completada")
    return result["text"]

def get_answer(question, context):
    """Obtiene una respuesta de OpenAI basada en el contexto y la pregunta."""
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    if not openai.api_key:
        app.logger.error("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    
    try:
        app.logger.info("Enviando solicitud a OpenAI API")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that answers questions based on the given context."},
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"}
            ],
            max_tokens=150,
            n=1,
            temperature=0.7,
        )
        app.logger.info("Respuesta recibida de OpenAI API")
        return response.choices[0].message['content'].strip()
    except openai.error.OpenAIError as e:
        app.logger.error(f"Error in OpenAI API call: {str(e)}")
        return f"An error occurred while processing your request: {str(e)}"

def cleanup():
    """Elimina los archivos temporales."""
    for file in glob.glob('audio*'):
        try:
            os.remove(file)
            app.logger.info(f"Archivo temporal {file} eliminado")
        except Exception as e:
            app.logger.error(f"Error al eliminar archivo temporal {file}: {e}")

def check_ffmpeg():
    """Verifica si FFmpeg está instalado y accesible."""
    try:
        result = subprocess.run([os.path.join(FFMPEG_PATH, "ffmpeg"), "-version"], 
                                check=True, capture_output=True, text=True)
        app.logger.info(f"FFmpeg version: {result.stdout.split('\n')[0]}")
        return True
    except subprocess.CalledProcessError as e:
        app.logger.error(f"Error al ejecutar FFmpeg: {e}")
        return False
    except FileNotFoundError:
        app.logger.error("FFmpeg no encontrado en la ruta especificada.")
        return False

# Verificar FFmpeg al importar el módulo
if not check_ffmpeg():
    app.logger.warning("Advertencia: FFmpeg no está correctamente configurado.")