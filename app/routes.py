import os
from flask import render_template, request, jsonify
from app import app
from app.utils import download_audio, transcribe_audio, get_answer, cleanup
from app.models import save_transcript, get_transcript

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
  youtube_url = request.json['url']
  app.logger.info(f"Iniciando transcripción para URL: {youtube_url}")
  
  audio_file = download_audio(youtube_url)
  if audio_file and os.path.exists(audio_file):
      try:
          app.logger.info(f"Archivo de audio encontrado: {audio_file}")
          transcript = transcribe_audio(audio_file)
          save_transcript(youtube_url, transcript)
          cleanup()  # Limpia los archivos temporales
          app.logger.info("Transcripción completada con éxito")
          return jsonify({'success': True, 'transcript': transcript})
      except Exception as e:
          app.logger.error(f"Error durante la transcripción: {str(e)}")
          cleanup()  # Asegúrate de limpiar incluso si hay un error
          return jsonify({'success': False, 'error': f"Transcription failed: {str(e)}"}), 500
  else:
      app.logger.error("Fallo al descargar el audio o archivo no encontrado")
      cleanup()  # Limpia cualquier archivo parcial que pueda haberse creado
      return jsonify({'success': False, 'error': 'Failed to download audio or file not found'}), 400

@app.route('/ask', methods=['POST'])
def ask():
  youtube_url = request.json['url']
  question = request.json['question']
  app.logger.info(f"Recibida pregunta para URL: {youtube_url}")
  
  transcript = get_transcript(youtube_url)
  if transcript:
      try:
          answer = get_answer(question, transcript)
          app.logger.info("Respuesta generada con éxito")
          return jsonify({'success': True, 'answer': answer})
      except Exception as e:
          app.logger.error(f"Error al generar respuesta: {str(e)}")
          return jsonify({'success': False, 'error': f"Failed to generate answer: {str(e)}"}), 500
  else:
      app.logger.error("Transcripción no encontrada")
      return jsonify({'success': False, 'error': 'Transcript not found'}), 404

@app.errorhandler(Exception)
def handle_exception(e):
  # Manejar cualquier excepción no capturada
  app.logger.error(f"Error no manejado: {str(e)}")
  return jsonify({'success': False, 'error': 'An unexpected error occurred'}), 500