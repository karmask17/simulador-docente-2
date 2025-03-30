import streamlit as st
import random
import json

st.set_page_config(page_title="Simulador Docente", layout="centered")

# ------------------- Inicialización -------------------
if "idioma" not in st.session_state:
    st.session_state.idioma = "es"
if "perfil" not in st.session_state:
    st.session_state.perfil = {}
if "etapa" not in st.session_state:
    st.session_state.etapa = 0
if "historial" not in st.session_state:
    st.session_state.historial = []

# ------------------- Idioma -------------------
st.markdown("### Idioma / Language")
idioma = st.radio("", ["es", "en"], horizontal=True)
st.session_state.idioma = idioma

# ------------------- Textos -------------------
textos = {
    "es": {
        "crear_perfil": "✏️ Crea tu perfil docente",
        "materia": "Materia",
        "nivel": "Nivel educativo",
        "num_alumnos": "Número de alumnos",
        "experiencia": "Años de experiencia",
        "guardar": "Guardar perfil",
        "continuar": "Continuar",
        "terminar": "🔴 Terminar simulador",
        "titulo": "Etapa",
        "retro": "👩‍🏫 Mentor virtual",
        "consecuencia": "🧠 Consecuencia",
        "impacto": "📊 Impacto"
    },
    "en": {
        "crear_perfil": "✏️ Create your teacher profile",
        "materia": "Subject",
        "nivel": "Educational level",
        "num_alumnos": "Number of students",
        "experiencia": "Years of experience",
        "guardar": "Save profile",
        "continuar": "Continue",
        "terminar": "🔴 End simulation",
        "titulo": "Stage",
        "retro": "👩‍🏫 Virtual mentor",
        "consecuencia": "🧠 Consequence",
        "impacto": "📊 Impact"
    }
}
T = textos[idioma]

# ------------------- Crear perfil -------------------
if not st.session_state.perfil:
    st.markdown(f"## {T['crear_perfil']}")
    with st.form("perfil"):
        materia = st.text_input(f"{T['materia']} / {T['materia']}", "química" if idioma == "es" else "Chemistry")
        nivel = st.selectbox(f"{T['nivel']} / {T['nivel']}", ["Secundaria", "Preparatoria", "Universidad"])
        alumnos = st.slider(f"{T['num_alumnos']} / {T['num_alumnos']}", 5, 60, 30)
        experiencia = st.slider(f"{T['experiencia']} / {T['experiencia']}", 0, 30, 1)
        submitted = st.form_submit_button(T["guardar"])
        if submitted:
            st.session_state.perfil = {
                "materia": materia,
                "nivel": nivel,
                "alumnos": alumnos,
                "experiencia": experiencia
            }
            st.rerun()

# ------------------- Escenarios -------------------
else:
    escenarios_base = [
        {
            "etapa": "Preparación para el ciclo",
            "pregunta": "¿Cómo planeas tus primeras clases?",
            "opciones": [
                {
                    "texto": "Elaboras un plan detallado con base en el contexto y necesidades del grupo.",
                    "consecuencia": "Tienes más claridad para enfrentar tu grupo.",
                    "retroalimentacion": "Planear con base en el contexto fortalece el ambiente de clase.",
                    "impacto": "B"
                },
                {
                    "texto": "Reutilizas tus materiales del año pasado sin adaptarlos.",
                    "consecuencia": "Algunas actividades no funcionan bien con este grupo.",
                    "retroalimentacion": "Adaptar tu planificación al contexto es esencial.",
                    "impacto": "C"
                },
                {
                    "texto": "Esperas a conocer al grupo antes de planear a fondo.",
                    "consecuencia": "Te sientes inseguro el primer día.",
                    "retroalimentacion": "Tener un plan inicial flexible puede ayudarte.",
                    "impacto": "A"
                }
            ]
        }
    ]

    if st.session_state.etapa < len(escenarios_base):
        escenario = escenarios_base[st.session_state.etapa]
        st.markdown(f"## {T['titulo']} {st.session_state.etapa + 1}")
        st.markdown(f"**{escenario['etapa']}**")
        st.write(escenario["pregunta"])

        opcion = st.radio("Selecciona una opción", [o["texto"] for o in escenario["opciones"]])
        if st.button(T["continuar"]):
            seleccion = next(o for o in escenario["opciones"] if o["texto"] == opcion)
            st.session_state.historial.append(seleccion)
            st.session_state.etapa += 1
            st.rerun()
        st.button(T["terminar"], on_click=lambda: st.session_state.clear())
    else:
        st.success("Simulación completada.")
        st.write("Historial de decisiones:")
        for i, h in enumerate(st.session_state.historial, 1):
            st.markdown(f"**Etapa {i}**")
            st.write(f"{T['consecuencia']}: {h['consecuencia']}")
            st.write(f"{T['retro']}: {h['retroalimentacion']}")
            st.write(f"{T['impacto']}: {h['impacto']}")
