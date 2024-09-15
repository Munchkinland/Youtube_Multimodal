 Youtube Multimodal

 ![image](https://github.com/user-attachments/assets/41e4af06-e95e-4158-9536-8e9f1202f6e6)

Este proyecto desarrolla una aplicación Flask que permite descargar audio de videos de YouTube, transcribirlo utilizando el modelo Whisper de OpenAI y responder preguntas basadas en la transcripción.

## Características

- Descarga de audio de videos de YouTube.
- Transcripción de audio utilizando el modelo Whisper.
- Respuestas a preguntas basadas en el contenido transcrito utilizando la API de OpenAI.

## Requisitos

- Python 3.7 o superior
- pip
- ffmpeg
- Clave de API de OpenAI

## Instalación

1. **Clona el repositorio:**

git clone https://github.com/Munchkinland/Youtube_Multimodal.git
cd Youtube_Multimodal


2. **Crea un entorno virtual (opcional pero recomendado):**

python -m venv venv
source venv/bin/activate  # En Linux o Mac
venv\Scripts\activate  # En Windows


3. **Instala las dependencias:**

pip install -r requirements.txt


4. **Configura las variables de entorno:**

Crea un archivo `.env` en la raíz del proyecto y añade tu clave de API de OpenAI:

OPENAI_API_KEY=tu_clave_de_api

5. **Asegúrate de que FFmpeg esté instalado y accesible en tu PATH.**

Puedes descargar FFmpeg desde [aquí](https://ffmpeg.org/download.html) y seguir las instrucciones de instalación.

## Uso

1. **Ejecuta la aplicación:**

python run.py


2. **Accede a la aplicación en tu navegador:**

Abre `http://127.0.0.1:5000` en tu navegador.

3. **Descarga y transcribe un video de YouTube:**

   - Proporciona la URL del video de YouTube en el campo correspondiente y haz clic en "Transcribir".
   - Una vez completada la transcripción, podrás hacer preguntas sobre el contenido.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -m 'Añadir nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Si tienes alguna pregunta o sugerencia, no dudes en contactarme
