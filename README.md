# Asistente de Escritura Automática ✍️

Este es un proyecto sencillo de un Asistente de Escritura impulsado por Inteligencia Artificial utilizando **Streamlit** para la interfaz gráfica y **Google Gemini API** como modelo de lenguaje subyacente.

## 🚀 Funcionalidades

El asistente cuenta con tres funciones principales diseñadas para facilitar el proceso de escritura:

1. **Mejorar redacción y ortografía**: Permite pegar un texto existente para que la IA corrija errores gramaticales y mejore el estilo y fluidez del mismo.
2. **Sugerir continuación**: Si te quedas sin ideas, puedes escribir el inicio de un texto y el asistente redactará el siguiente párrafo de forma coherente.
3. **Escribir un texto desde cero**: Solo necesitas ingresar un tema (ej. "Un correo solicitando vacaciones") y seleccionar el tono deseado (Profesional, Casual, Creativo, Persuasivo, etc). El modelo generará el texto completo por ti.

## 🛠 Requisitos Previos

Para utilizar esta aplicación necesitas:

- Python 3.8 o superior instalado en tu sistema.
- Una **API Key de Google Gemini** (Puedes obtenerla gratuitamente en [Google AI Studio](https://aistudio.google.com/)).

## 📦 Instalación

1. Clona el repositorio o navega hasta la carpeta del proyecto en tu terminal:
   ```bash
   cd /ruta/a/tu/proyecto/asistente_escritura
   ```

2. (Recomendado) Crea un entorno virtual para instalar las dependencias sin afectar tu sistema:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Mac/Linux
   # venv\Scripts\activate   # En Windows
   ```

3. Instala las dependencias requeridas usando el archivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

4. Crea un archivo `.env` dentro de `asistente_escritura/` con tu API Key (puedes copiar `.env.example`):
   ```bash
   cp .env.example .env
   ```
   y edítalo para dejar:
   ```
   GEMINI_API_KEY=tu_api_key_aqui
   ```

## ▶️ Uso

Para iniciar la aplicación, asegúrate de tener tu entorno virtual activado y ejecuta el siguiente comando:

```bash
streamlit run app.py
```

- Al ejecutarlo por primera vez, Streamlit podría preguntarte tu correo electrónico. Puedes simplemente presionar **Enter** para omitir ese paso.
- La aplicación se abrirá automáticamente en tu navegador web predeterminado (usualmente en `http://localhost:8501`).
- La API Key se lee automáticamente del archivo `.env` (no se sube al repositorio). Opcionalmente puedes definir `GEMINI_MODEL` para cambiar el modelo (por defecto `gemini-3.8-flash`).

## 📚 Tecnologías Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) (Interfaz de usuario web)
- [Google Gemini API](https://ai.google.dev/) vía `google-genai` (Modelo de IA)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (Variables de entorno)
