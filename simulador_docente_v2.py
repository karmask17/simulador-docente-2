
import streamlit as st
import json
import random
import uuid

# Configuración de la página
st.set_page_config(page_title="Simulador Docente", layout="centered")

# Cargar escenarios base según idioma
@st.cache_data
def cargar_escenarios(idioma):
    archivo = "escenarios_es.json" if idioma == "es" else "escenarios_en.json"
    with open(archivo, "r", encoding="utf-8") as f:
        return json.load(f)

# Inicialización
if "idioma" not in st.session_state:
    st.session_state.idioma = "es"
if "perfil" not in st.session_state:
    st.session_state.perfil = {}
if "historial" not in st.session_state:
    st.session_state.historial = []
if "etapa" not in st.session_state:
    st.session_state.etapa = 0
if "impacto" not in st.session_state:
    st.session_state.impacto = {"estrés": 0, "motivación": 0, "clima": 0, "vínculo": 0}

# Traducción básica
def t(clave):
    textos = {
        "es": {
            "idioma": "Idioma / Language",
            "crear_perfil": "Crea tu perfil docente",
            "materia": "Materia / Subject",
            "nivel": "Nivel educativo / Educational level",
            "alumnos": "Número de alumnos / Number of students",
            "experiencia": "Años de experiencia / Years of experience",
            "guardar": "Guardar perfil",
            "iniciar": "Iniciar simulador",
            "continuar": "Continuar",
            "terminar": "Terminar simulador",
            "impacto": "Impacto",
            "mentor": "Mentor virtual",
            "consecuencia": "Consecuencia",
            "etapa": "Etapa",
            "reporte": "Resumen final de tu carrera docente"
        },
        "en": {
            "idioma": "Idioma / Language",
            "crear_perfil": "Create your teacher profile",
            "materia": "Subject / Materia",
            "nivel": "Educational level / Nivel educativo",
            "alumnos": "Number of students / Número de alumnos",
            "experiencia": "Years of experience / Años de experiencia",
            "guardar": "Save profile",
            "iniciar": "Start simulator",
            "continuar": "Continue",
            "terminar": "Finish simulator",
            "impacto": "Impact",
            "mentor": "Virtual mentor",
            "consecuencia": "Consequence",
            "etapa": "Stage",
            "reporte": "Final summary of your teaching journey"
        }
    }
    return textos[st.session_state.idioma].get(clave, clave)

# Selector de idioma
st.radio(t("idioma"), ["es", "en"], key="idioma", horizontal=True)

# Crear perfil docente
with st.form("perfil"):
    st.subheader("📝 " + t("crear_perfil"))
    materia = st.text_input(t("materia"))
    nivel = st.selectbox(t("nivel"), ["Primaria", "Secundaria", "Preparatoria"])
    alumnos = st.slider(t("alumnos"), 5, 60, 30)
    experiencia = st.slider(t("experiencia"), 0, 30, 1)
    if st.form_submit_button(t("guardar")):
        st.session_state.perfil = {
            "materia": materia,
            "nivel": nivel,
            "alumnos": alumnos,
            "experiencia": experiencia
        }
        st.session_state.historial = []
        st.session_state.etapa = 0
        st.success("✅ Perfil guardado correctamente.")

# Iniciar simulador
if st.session_state.perfil:
    if st.button(t("iniciar")):
        st.switch_page("simulador_carrera_docente.py")
