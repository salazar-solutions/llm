import os

import streamlit as st
from dotenv import load_dotenv
from google import genai

# Carga las variables del archivo .env (GEMINI_API_KEY)
load_dotenv()

MODELO = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

st.set_page_config(page_title="Asistente de Escritura", page_icon="✍️", layout="centered")

st.title("✍️ Asistente de Escritura Automática")
st.write(
    "¡Hola! Soy tu asistente de escritura. Puedo ayudarte a sugerir oraciones, "
    "corregir tu gramática, mejorar tu estilo o incluso redactar textos completos."
)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error(
        "No se encontró `GEMINI_API_KEY`. Crea un archivo `.env` en esta carpeta "
        "con el contenido `GEMINI_API_KEY=tu_clave` (ver `.env.example`) y reinicia la app."
    )
    st.stop()

client = genai.Client(api_key=api_key)


def generar(prompt: str, mensaje_spinner: str, titulo: str) -> None:
    """Envía el prompt al modelo y muestra el resultado."""
    with st.spinner(mensaje_spinner):
        try:
            respuesta = client.models.generate_content(model=MODELO, contents=prompt)
            st.subheader(titulo)
            st.write(respuesta.text)
        except Exception as e:
            st.error(f"Error: {e}")


tarea = st.selectbox(
    "¿En qué te puedo ayudar hoy?",
    ("Mejorar redacción y ortografía", "Sugerir continuación", "Escribir un texto desde cero"),
)

if tarea == "Mejorar redacción y ortografía":
    texto = st.text_area("Pega aquí tu texto:", height=150)
    if st.button("Mejorar texto"):
        if texto.strip():
            generar(
                "Corrige la ortografía y mejora la redacción y estilo del siguiente texto. "
                f"Devuelve solo el texto corregido:\n\n{texto}",
                "Revisando tu texto...",
                "Texto Mejorado:",
            )
        else:
            st.warning("Por favor, ingresa un texto para mejorar.")

elif tarea == "Sugerir continuación":
    texto = st.text_area("Escribe el inicio de tu texto aquí:", height=150)
    if st.button("Sugerir continuación"):
        if texto.strip():
            generar(
                "Continúa escribiendo el siguiente texto de forma coherente y creativa "
                f"(agrega un párrafo más):\n\n{texto}",
                "Pensando en ideas...",
                "Sugerencia:",
            )
        else:
            st.warning("Por favor, ingresa el inicio de tu texto.")

else:
    tema = st.text_input(
        "¿Sobre qué tema quieres escribir? (Ej. Un correo pidiendo vacaciones, un artículo sobre IA, etc.)"
    )
    tono = st.selectbox("Elige el tono del texto:", ("Profesional", "Casual", "Creativo", "Persuasivo"))
    if st.button("Generar texto"):
        if tema.strip():
            generar(
                f"Escribe un texto sobre: '{tema}'. El tono del texto debe ser {tono.lower()}.",
                "Escribiendo...",
                "Texto Generado:",
            )
        else:
            st.warning("Por favor, ingresa un tema.")
