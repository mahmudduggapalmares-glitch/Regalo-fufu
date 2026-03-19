import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="Misión Especial: Fufu", page_icon="🎮")

# Estilos personalizados
st.markdown("""
    <style>
    .main {
        background-color: #1a1a1a;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    .big-font {
        font-size:30px !important;
        font-weight: bold;
        color: #ff4b4b;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="big-font">🎮 NIVEL: EL PERDÓN DE FUFU 🎮</p>', unsafe_allow_html=True)

# Inicializar el estado del juego
if 'level' not in st.session_state:
    st.session_state.level = 1

# --- NIVEL 1 ---
if st.session_state.level == 1:
    st.subheader("Etapa 1: El Acertijo")
    st.info("No se puede ver, pero tú lo llenas por completo. Es lo que siento al escucharte. ¿Qué es?")
    
    respuesta = st.text_input("Escribe aquí:").lower().strip()
    if st.button("Verificar"):
        if "amor" in respuesta:
            st.success("¡Correcto!")
            time.sleep(1)
            st.session_state.level = 2
            st.rerun()
        else:
            st.error("Inténtalo de nuevo...")

# --- NIVEL 2 ---
elif st.session_state.level == 2:
    st.subheader("Etapa 2: El Inventario")
    st.write("Marca lo que es real:")
    
    c1 = st.checkbox("Eres increíble.")
    c2 = st.checkbox("Tu sonrisa es lo mejor.")
    c3 = st.checkbox("Eres lo mejor que me ha pasado.")
    
    if st.button("Continuar"):
        if c1 and c2 and c3:
            st.balloons()
            st.session_state.level = 3
            st.rerun()
        else:
            st.warning("¡Marca todas!")

# --- NIVEL 3 ---
elif st.session_state.level == 3:
    st.subheader("Etapa Final: El Mensaje")
    st.write("Fufu, te amo muchísimo. Eres mi mundo y lamento cualquier error. ¿Me perdonas?")
    
    opcion = st.radio("Elige una opción:", ["...", "Sí, te perdono", "Claro que sí"])
    
    if "perdono" in opcion or "Claro" in opcion:
        st.markdown("### **¡Misión cumplida! 🏆**")
        st.markdown("## **¿Quieres que juguemos algo juntos ahora?**")
        if st.button("REINICIAR"):
            st.session_state.level = 1
            st.rerun()
